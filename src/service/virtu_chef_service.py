import os
from openai import OpenAI
import json
from dotenv import load_dotenv
import src.prompts.virtu_chef_prompts as prompts
from src.model.virtu_chef_models import Receipe

load_dotenv()

def get_receipe(image_base64):  
    if os.getenv("ENVIRONMENT") == "dev":
        return MOCK_get_receipe_from_gtp_vision(image_base64)
    else:
        return get_receipe_from_gtp_vision(image_base64)


def get_receipe_from_gtp_vision(image_base64):  
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

  print (message.content)
  receipe = Receipe(**json.loads(message.content))

  return receipe

def MOCK_get_receipe_from_gtp_vision(image_base64):  
  message = """{
    "food_name": "Chicken Biryani",
    "receipe": "Chicken Biryani Recipe",
    "ingredients": [
        "basmati rice",
        "chicken pieces",
        "cooking oil or ghee",
        "onions",
        "tomatoes",
        "ginger garlic paste",
        "yogurt",
        "lemon juice",
        "green chillies",
        "mint leaves",
        "coriander leaves",
        "biryani masala powder",
        "red chili powder",
        "turmeric powder",
        "salt",
        "whole spices (cardamom, cloves, cinnamon, bay leaves, star anise)",
        "saffron strands (optional)",
        "milk (for saffron soaking, optional)",
        "fried onions (for garnish, optional)"
    ],
    "cooking_time": "1 hour 30 minutes",
    "cooking_instructions": "Rinse basmati rice until water runs clear and soak for 30 minutes. Heat oil or ghee in a pot, add whole spices, and then fry sliced onions until golden. Add ginger garlic paste, followed by chopped tomatoes, and cook until soft. Add chicken pieces, biryani masala, chili powder, turmeric, salt, and cook until chicken is browned. Add yogurt, lemon juice, green chilies, mint, and coriander leaves; cook the chicken until it's nearly done. Boil rice until it's 70% cooked. Layer the cooked chicken and partially cooked rice in a pot. Optionally, sprinkle saffron-soaked milk for color and aroma. Cover with a lid and cook on a low flame for a final 20 minutes until rice is fully cooked. Let it rest for 15 minutes, then fluff with a fork. Garnish with coriander, mint, and fried onions before serving."
    }"""
    
  receipe = Receipe(**json.loads(message))

  return receipe