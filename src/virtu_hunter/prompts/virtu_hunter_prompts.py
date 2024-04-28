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