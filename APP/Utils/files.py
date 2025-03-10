import base64
import os
import textwrap
from typing import cast
import uuid
import requests
from Gemini.Schemas import JSON_SCHEMAS, CodeProj
from Gemini.Schemas import Task
from GoogleAppScripts.gap import sendAppScriptsRequest


def generate_code(task:Task, id):
    readme = generate_cover_page(**task)
    
    code = cast(CodeProj, task["work"])
    readme += code.get('explanation') + '\n'
    for file in code.get('files'):
        readme += gen_code_md_image(**file) + '\n'
        create_file(**file, **task)
        
    path = create_file(file_name="README.md", content=readme, **task)           
    sendAppScriptsRequest(path, task, id)

def generate_essay(task:Task, id):
    doc = generate_cover_page(**task)


    markdown = textwrap.dedent(f"""
        ---
        # {task['work']['title']}

        ## Introduction:
        {task['work']['introduction']}

        ---

        ## Development:
        {task['work']['development']}

        ---

        ## Conclusion:
        {task['work']['conclusion']}
        
        ---
        
        ## References:
        {task['work']['references']}
    """)

    doc += f'\n{markdown}'
    print(f'Ellie: \n {doc}')    
    path = create_file(file_name=f"{task['title']}.md", content=textwrap.dedent(doc), **task)           
    sendAppScriptsRequest(path, task, id)


def generate_cover_page(title: str, author: str, register: str, date: str, subject: str, desc: str, professor: str, **kwargs) -> str:
    """
    Generates a cover page in Markdown format with the provided information.

    Args:
    - title (str): The title of the work.
    - author (str): The author of the work.
    - register (str): The registration number.
    - date (str): The date of creation.
    - subject (str): The subject the work is related to.
    - desc (str): A description of the work.
    - professor (str): The professor overseeing the work.

    Returns:
    - str: A Markdown-formatted cover page.
    """
    cover_page_md = textwrap.dedent(f"""
    # {title}

    **Elaborado por**: {author}  
    **Registro**: {register}  
    **Fecha**: {date}  
    **Materia**: {subject}  
    **Profesor**: {professor}  
    **Indicaciones**: {desc}  
    """)


    return cover_page_md


def create_file(file_name, content, subject, title = f"task_{str(uuid.uuid4())}", **kwargs):
    os.makedirs(f"Academic_Work/{subject}/{title}", exist_ok=True) 
    
    with open(f"Academic_Work/{subject}/{title}/{file_name}", 'w', encoding='utf-8') as f: 
        f.write(content)
    
    return f"Academic_Work/{subject}/{title}"


def read_task(data) -> list[Task]: 
    tasks: list[Task] = [
        {
            **task_data,
            "resources": [
                {**resource} for resource in task_data["resources"]
            ]
        }
        for task_data in data
    ]
    
    return tasks # Return the parsed JSON data


def parse_json(file): 
    import json
    
    # Read and parse the JSON file
    with open(file, 'r',  encoding='utf-8') as f:
        data = json.load(f)

    return data 


def load_tasks(path = 'Tasks/*.json'):
    import glob
    # Get a list of all JSON files in the 'Tasks' folder
    task_files = glob.glob(path)
    
    if not task_files:
        print("No JSON files found in the 'Tasks' folder.")
        return []

     # Sort the files by modification time (newest first)
    task_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

    # Take the most recently modified file or the first file if only one exists
    latest_file = task_files[0]

    data = parse_json(latest_file)
    return read_task(data["tasks"]), data["id"]


def generate_task(task: Task, id):

    if task["cat"] == JSON_SCHEMAS.CODE_PROJ.value:
        generate_code(task, id)
    elif task["cat"] == JSON_SCHEMAS.DOC.value:
        generate_essay(task, id)
    elif task["cat"] == JSON_SCHEMAS.SLIDES.value:
        pass
    else:
        generate_essay(task, id)


def gen_code_md_image(file_name, content):
    if (not content) or (not file_name): return ''
    # Set up the payload for the API request
    carbon_req = {
        "code": content,
        "paddingVertical": "56px",
        "paddingHorizontal": "56px",
        "backgroundImage": None,
        "backgroundImageSelection": None,
        "backgroundMode": "color",
        "backgroundColor": "rgba(171, 184, 195, 1)",
        "dropShadow": True,
        "dropShadowOffsetY": "20px",
        "dropShadowBlurRadius": "68px",
        "theme": "seti",
        "windowTheme": "none",
        "language": "auto",
        "fontFamily": "Hack",
        "fontSize": "14px",
        "lineHeight": "133%",
        "windowControls": True,
        "widthAdjustment": True,
        "lineNumbers": False,
        "firstLineNumber": 1,
        "exportSize": "2x",
        "watermark": False,
        "squaredImage": False,
        "hiddenCharacters": False,
        "name": "",
        "width": 680
    }

    headers = {
        "Content-Type": "application/json"
    }

    # Make the POST request
    try:
        response = requests.post("https://carbonara.solopov.dev/api/cook", json=carbon_req, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx/5xx responses
        
        # The image will be returned as raw bytes
        image = response.content  
        image_base64 = base64.b64encode(image).decode('utf-8')  # Encode and decode to a string
                # Prepare the markdown image URL
        return f"![{file_name}](data:image/png;base64,{image_base64})"

        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return ''
