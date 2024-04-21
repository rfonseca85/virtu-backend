from fastapi import APIRouter, UploadFile, File
from fastapi.responses import HTMLResponse
from src.model.virtu_chef_models import Receipe
import src.prompts.virtu_chef_prompts as prompts
import os
from dotenv import load_dotenv
from openai import OpenAI
import tempfile
import base64
import json

load_dotenv()

router = APIRouter(tags=["virtu_chef"])

@router.post("/get_receipe", response_model=Receipe)
async def get_receipe(file: UploadFile = File(...)):
    # Read the image file
    image_data = await file.read()
    image_base64 = base64.b64encode(image_data).decode("utf-8")

    # Analyze the image using OpenAI
    model = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    model.timeout = 30

    # Get the image analysis response
    response = model.chat.completions.create(
		model="gpt-4-vision-preview",
		messages=[
			{
				"role": "user",
				"content": [
					{
						"type": "image_url",
						"image_url": f"data:image/png;base64,{image_base64}",
					},
					{
						"type": "text",
						"text": prompts.user_prompt,
					}
				]
			}
		],
		max_tokens=1024,
	)
    message = response.choices[0].message

    if message is None:
        return "No response from the model"

    receipe = Receipe(**message.content)

    print (message.content)
    # receipe = Receipe(food_name="Pizza", receipe="Bake", ingredients=["Flour", "Tomato", "Cheese"], cooking_time="30 minutes", cooking_instructions="Bake the pizza")
    return receipe