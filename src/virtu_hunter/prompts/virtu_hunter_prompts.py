from src.virtu_hunter.models.virtu_hunter_models import CoverLetterRequest


def get_coverletter_prompt(coverletter_request: CoverLetterRequest):
    return f"""

    You are a specialist writing cover letter and you are applying for the position of {coverletter_request.jobTitle} at {coverletter_request.companyName}. 
    Here is the description of the job: {coverletter_request.jobDescription}.
    
    With all that information, write a cover letter for this job application. 
    In this process research the company and include a sentence about what would excites me to work on this company.
    Make it look professional.
    Make it unique.
    Dont use the same words from the resume, make it look like a human wrote it.
    Dont use unusual words, make it look like a human wrote it.
   
    Return just the cover letter text.
    
    """

def get_uploadresume_prompt(resume: str):
    return """
    Based on the resume uploaded, please add all the information in the json format below:
    Return just the json.
    This is the resume: """ + resume + """
    
    Please return a json with the following structure:

    { 
        'name' : "", 
           'lastName' : '',
            'title': '',
            'contact': {
                'city': '',
                'province': '',
                'phone': '',
                'email': '',
                'linkedin': ''
                },
             'summary': '', 
             'experiences': [
                  {
                      'companyName': '',
                      'title': '',
                      'startDate': '',
                      'endDate': '',
                      'description': [{'point': ''}, {'point': ''}]
                  },
             ], 
            'skills': [
                {
                    'category': '',
                    'description': ''
                },
            ],
             'education': [
                 {
                     'degree': '',
                     'school': '',
                     'startDate': '',
                     'endDate': ''
                 }
             ],    
            }

    """


def get_resumeanalisys_prompt(resume: str):
    return f"""

    You are a specialist writing resume and you are analyzing a resume.
    Here is the resume separated by paragraphs (2 lines separation): {resume}.
    
    please return a json with the following structure:
    {
        "paragraph": "This is the first paragraph",
        "suggestions": ["Suggestion 1", "Suggestion 2", "Suggestion 3"]
    },
    {
        "paragraph": "This is the second paragraph",
        "suggestions": ["Suggestion 1", "Suggestion 2", "Suggestion 3"]
    },
    {
        "paragraph": "This is the third paragraph",
        "suggestions": ["Suggestion 1", "Suggestion 2", "Suggestion 3"]
    },
    {
        "paragraph": "This is the fourth paragraph",
        "suggestions": ["Suggestion 1", "Suggestion 2", "Suggestion 3"]
    },
    
    for each one of those paragraphs.
    If a paragraph has no suggestions, return an empty list.

    return just the json.

    """

