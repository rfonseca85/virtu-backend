from src.model.virtu_chef_models import Receipe
user_prompt = """
You are a master chef and you have been asked to create the same dish as the image sent

Answer the following questions about the image:
What is the food_name?
What is the receipe?
What are the ingredients?
What is the cooking_time?
What are the cooking_instructions?

Always answer in the json format below: 
{
    "food_name": "Food Name",
    "receipe": "Receipe",
    "ingredients": ["ingredient1", "ingredient2", "ingredient1"],
    "cooking_time": "30 minutes",
    "cooking_instructions": "cooking instructions"
}

bring the json not the schema, also not need the ```json in the beginning and end of the json
"""