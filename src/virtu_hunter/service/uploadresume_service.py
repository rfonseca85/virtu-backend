import os
from openai import OpenAI
import json
from dotenv import load_dotenv
import src.virtu_hunter.prompts.virtu_hunter_prompts as prompts
from src.virtu_hunter.models.virtu_hunter_models import CoverLetter, CoverLetterRequest

load_dotenv()


def upload_resume(resume):  


  model = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
  model.timeout = 30

  messages = [
      {
          "role": "user",
          "content": prompts.get_uploadresume_prompt(resume),
      }
  ]

  response = model.chat.completions.create(
      model="gpt-3.5-turbo-1106",
      messages=messages,
      max_tokens=1024,
      stop=None,
      temperature=0.7,
  )
  
  message = response.choices[0].message

  if message is None:
      return "No response from the model"

  return message.content


