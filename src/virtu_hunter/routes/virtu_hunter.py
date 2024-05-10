from typing import Awaitable, Callable, List
from fastapi import APIRouter, UploadFile, File, Depends
import base64
from src.virtu_hunter.models.virtu_hunter_models import CoverLetter, CoverLetterRequest
from src.auth.model.user_auth_models import User
import src.auth.service.user_auth_service as uas
import src.virtu_hunter.service.coverletter_service as vhs
from fastapi import WebSocket
from openai import AsyncOpenAI, OpenAI
import os
from dotenv import load_dotenv
from openai.types.chat import ChatCompletionMessageParam, ChatCompletionChunk


load_dotenv()

client = OpenAI()

router = APIRouter(tags=["Virtu.hunter"])

# @router.post("/coverletter")#response_model=CoverLetter
# async def generate_coverletter(request: CoverLetterRequest, current_user: User = Depends(uas.get_current_user)):
#     # Read the image file
#     coverletter = vhs.get_coverletter(request) 
#     # CoverLetter = CoverLetter(coverletter=coverletter)
#     return coverletter



# WebSocket route to handle cover letter generation
@router.websocket("/coverletter")
async def generate_cover_letter(websocket: WebSocket):
    
    await websocket.accept()
    data = await websocket.receive_text()
    job_title, company_name, job_description = data.split(",")

    # await websocket.send_text("Generating code...")

    async def process_chunk(content: str):
        await websocket.send_text(str(content))

    prompt = f"""

    You are a specialist writing cover letter and you are applying for the position of {job_title} at {company_name}. 
    Here is the description of the job: {job_description}.
    
    With all that information, write a cover letter for this job application. 
    In this process research the company and include a sentence about what would excites me to work on this company.
    Make it look professional.
    Make it unique.
    Dont use the same words from the resume, make it look like a human wrote it.
    Dont use unusual words, make it look like a human wrote it.
   
    Return just the cover letter text.
    
    """

    messages = [
        {
            "role": "user",
            "content": prompt,
        }
    ]

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    stream = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            # print(chunk.choices[0].delta.content, end="")
            await websocket.send_text(chunk.choices[0].delta.content)

    await websocket.close()