# from docx import Document
# import os
# from dotenv import load_dotenv
# from openai import OpenAI
# # import src.virtu_hunter.prompts.virtu_hunter_prompts as prompts

# load_dotenv()

# def get_resumeanalisys_prompt(resume: str):
    
#     json_response ="""{"suggestions":[{"description": "Explore art, history, or science at your local museum."},{"description": "Experiment with cooking something you've never made before."},"""    },
      
#     return f"""

#     You are a specialist writing resume and you are analyzing a resume.
#     Here is the resume separated by paragraphs: {resume}.
#     Analyse improvements that can be made to the resume and return ONE suggestions for each paragraph in the following json format:
#     {json_response}

#     Dont skip any paragraph.    
#     If a paragraph has no suggestions, return an empty string.

#     return just the json. 
#     Make sure it is a valid json.

#     """


# # Function to extract text from a Word document
# def extract_text_from_docx(docx_file):
#     doc = Document(docx_file)
#     text = ""
#     for paragraph in doc.paragraphs:
#         text += paragraph.text + "\n\n"
#     print (str(len(doc.paragraphs)))
#     return text

# # Function to call OpenAI API and get suggestions
# def get_openai_suggestions(text):

#   model = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#   model.timeout = 30

#   messages = [
#       {
#           "role": "user",
#           "content": get_resumeanalisys_prompt(resume=text),
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


# # Function to integrate suggestions into the document
# def annotate_docx_with_suggestions(docx_file, suggestions):
#     doc = Document(docx_file)
#     for paragraph in doc.paragraphs:
#         # Assuming each paragraph corresponds to a suggestion
#         paragraph.text += "\nSuggestion: " + suggestions
#     return doc

# # Main function
# def main():
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     docx_file_path = os.path.join(script_dir, "resume.docx")
    
#     # Step 1: Extract text from the document
#     text = extract_text_from_docx(docx_file_path)
    
#     # Step 2: Call OpenAI API to get suggestions
#     # suggestions = get_openai_suggestions(text)
    
#     # Step 3: Integrate suggestions into the document
#     # annotated_doc = annotate_docx_with_suggestions(docx_file_path, suggestions)
    
#     # Step 4: Save the modified document
#     # annotated_doc.save("annotated_document.docx")
#     print("Annotations added successfully.")

# if __name__ == "__main__":
#     main()
