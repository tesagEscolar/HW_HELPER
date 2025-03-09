def sendAppScriptsRequest(path, task):
    import requests
    import os
    from base64 import b64encode

    url = os.getenv('APP_SCRIPT_ENDPOINT')
    files_data = {}


    

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
    
        # Only consider files (skip directories)
        if os.path.isfile(file_path):
            # Read the file as binary and encode it as Base64
            with open(file_path, 'rb') as file:
                encoded_file = b64encode(file.read()).decode('utf-8')
                files_data[filename] = encoded_file  # Add the file to the dictionary
    
    task['files'] = files_data

    res = requests.post(url, json=task)

    if res.status_code == 200:
        pass
    else:
        print("Error:", res.status_code, res.text)
    
