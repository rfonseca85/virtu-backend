import os
from openai import OpenAI
import json
from dotenv import load_dotenv
import src.virtu_hunter.prompts.virtu_hunter_prompts as prompts
from src.virtu_hunter.models.virtu_hunter_models import CoverLetter, CoverLetterRequest

load_dotenv()






# def analise_resume(resume_request: ResumeRequest):  
    # if os.getenv("ENVIRONMENT") == "dev":
    #     return MOCK_get_coverletter_from_gtp(coverletter_request)
    # else:
    #     return get_coverletter_from_gtp(coverletter_request)


# def get_coverletter_from_gtp(coverletter_request):  

#   # TODO:# Retrieve resume from the database
#   # resume_text = get_resume_text(st.session_state["username"])
#   # if resume_text:
#   #     st.write("Retrieved Resume:")
#   #     st.write(resume_text)

#   model = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#   model.timeout = 30

#   messages = [
#       {
#           "role": "user",
#           "content": prompts.get_coverletter_prompt(coverletter_request),
#       }
#   ]

#   response = model.chat.completions.create(
#       model="gpt-3.5-turbo-1106",
#       messages=messages,
#       max_tokens=1024,
#       stop=None,
#       temperature=0.7,
#   )
  
#   message = response.choices[0].message

#   if message is None:
#       return "No response from the model"

#   return message.content


# def MOCK_resume_from_gtp(coverletter_request):  
#   message = """{"coverLetter": "Cover Letter"}"""
  
    
#   coverLetter = CoverLetter(**json.loads(message))

#   return coverLetter