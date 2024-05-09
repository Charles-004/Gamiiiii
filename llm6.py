import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv() 
client = AzureOpenAI(
  azure_endpoint = "https://hkust.azure-api.net",
  api_version = "2024-02-01",
  api_key = os.getenv("AZURE_API_KEY") 
)


def get_response(message, instruction):
    response = client.chat.completions.create(
		model = 'gpt-35-turbo',
        temperature = 1,
        messages = [
            {"role": "system", "content": instruction},
            {"role": "user", "content": message}
        ]
    )
   
    print(response.usage)
    # return the response(Prob: Not showing in terminal)
    return response.choices[0].message.content

message=input("What you wanna ask?")
get_response(message, "You are a killer.")
