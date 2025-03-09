import json
import google.generativeai as ai_client
from google import genai as ai_client_new
from google.genai.types import HttpOptions, GenerateContentConfig
from Gemini.Instructions import ModelInstructions
from Gemini.Schemas import JSON_SCHEMAS, MimeTypes, Task, schema_types, schema_mapping


class geminiAssistant():
    def __init__(self, apiKey= "AIzaSyDIGT36TVzhqaBp_FBtq4SHkULRqJ1xmgQ", version = '1.5'):
        self.version = version 
        self.request = []
        self.schema  = None
        self.mime_type = None

        self.client = self.getClient(apiKey)
        self.safety_settings= self.get_safety_settings()

    def setReturnType(self, workType):
        self.mime_type = workType
    
    def sendSimpleTask(self, prompt):
        self.addPromptData(prompt)
        return self.sendRequest()

    def addPromptData(self, data, schema = None, mimeType = None):
        self.request.append(data)
        if schema:
            self.schema = schema_types[schema] 
        if mimeType:
            self.mime_type = mimeType.value


    def getTasks(self, task):
        self.addPromptData(task, JSON_SCHEMAS.TASK, MimeTypes.JSON)
        return self.sendRequest(ModelInstructions.WRITE_SUBTASKS)

    def executeTasks(self, task:Task):
        tasks = json.loads(self.getTasks(task['desc']))
        for subTask in tasks:
            cat, answer = self.executeSubTask(subTask)
            task["cat"] = cat
            task['work'] = answer 
        return task

    def executeSubTask(self, subTask):
        steps = f"{'Instrucciones: \n' + subTask['Task']}"
        self.addPromptData(steps, schema_mapping.get(subTask['workType']), MimeTypes.JSON)
        return subTask['workType'], json.loads(self.sendRequest(ModelInstructions[str.upper(subTask['workType'])]))



    def sendRequest(self, instructions = None):
        response = ''

        if self.version == '1.5':
            if instructions: 
                model = ai_client.GenerativeModel("gemini-1.5-pro", system_instruction=instructions.value)
            model = ai_client.GenerativeModel("gemini-1.5-flash")    
        
            if self.schema and self.mime_type: 
                response = model.generate_content(self.request[0],safety_settings = self.safety_settings, generation_config=ai_client.GenerationConfig(response_mime_type=self.mime_type, response_schema=self.schema)).text
            else:
                response = model.generate_content(self.request[0],  safety_settings = self.safety_settings).text
            self.clearRequest()
            return response

        if instructions:
            response = self.client.models.generate_content( 
                model='gemini-2.0-flash-001',
                contents=self.request[0], 
                config={
                    # "system_instruction": [instructions.value], 
                    "safety_settings": self.safety_settings,
                    # "response_mime_type":self.mime_type,
                    # "response_schema": self.schema
                    }
                ).text
        else:
            response = self.client.models.generate_content(
                model="gemini-2.0-pro-exp-02-05",
                contents=self.request[0],
                config=GenerateContentConfig(
                    safety_settings= self.safety_settings,
                    # system_instruction=[instructions.value], 
                    # response_mime_type=self.mime_type,
                    # response_schema= self.schema
                ),
            ).text
      

        self.clearRequest()
        return response


    def get_safety_settings(self):
        from google.genai.types import (HarmCategory,HarmBlockThreshold,SafetySetting,)
        if self.version == '1.5':
            return {
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }


        return [
            SafetySetting(
                category=HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=HarmBlockThreshold.OFF,
            ),
            SafetySetting(
                category=HarmCategory.HARM_CATEGORY_HARASSMENT,
                threshold=HarmBlockThreshold.OFF,
            ),
            SafetySetting(
                category=HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                threshold=HarmBlockThreshold.OFF,
            ),
            SafetySetting(
                category=HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                threshold=HarmBlockThreshold.OFF,
            ),
            # SafetySetting(
            #     category=HarmCategory.HARM_CATEGORY_UNSPECIFIED,
            #     threshold=HarmBlockThreshold.OFF,
            # ),
            # SafetySetting(
            #     category=HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY,
            #     threshold=HarmBlockThreshold.OFF,
            # ),
        ]

    


    def getClient(self, api_key):
        if self.version == '1.5':
            ai_client.configure(api_key=api_key)
            return ai_client

        return ai_client_new.Client(api_key=api_key, http_options=HttpOptions(api_version="v1")) 


    def clearRequest(self):
        self.request.clear()
        self.mime_type = None
        self.schema = None
