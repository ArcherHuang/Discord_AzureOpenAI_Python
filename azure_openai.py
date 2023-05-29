import os
import sys
import json
import requests
from dotenv import load_dotenv

load_dotenv()

headers = {
    "content-type": "application/json",
    "api-key": os.getenv('AZURE_OPENAI_KEY'),
}
    
def openai_prompt(user_prompt):
    try:
        req_body = {
            "messages":[
                {
                    "role": "system",
                    "content": "你是一個名叫「OpenAI ChatGPT」的角色。請用小於6歲的孩子能夠聽懂的語言和親切、容易親近的口吻來講話。"
                },
                {
                    "role": "user",
                    "content": user_prompt
                },
                {
                    "role": "assistant",
                    "content": ""
                }
            ],
            "temperature": 0.7,
            "top_p": 0.95,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "max_tokens": 800,
            "stop": None,
        }

        response = requests.post(f"{os.getenv('AZURE_OPENAI_ENDPOINT')}openai/deployments/{os.getenv('AZURE_OPENAI_MODEL_DEPLOYMENT_NAME')}/chat/completions?api-version=2023-03-15-preview",
                                 data=json.dumps(req_body),
                                 headers=headers)
        json_obj = json.loads(response.content.decode('utf8').replace("'", '"'))
        return json_obj['choices'][0]['message']['content']
    except:
        print(f"Unexpected error: {sys.exc_info()}")