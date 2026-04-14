from langchain_core.prompts import PromptTemplate

# Define the template for evaluation
template = """
You are an expert recruiter. Evaluate the following resume against the job description.
Do NOT assume skills that are not explicitly mentioned in the resume. 

Job Description: {job_description}
Resume: {resume_text}

Provide the output in the following JSON format: 
{{
    "extracted_skills": [],
    "experience_summary": "",
    "fit_score": 0,
    "explanation": "Why this score was assigned"
}}
"""

screening_prompt = PromptTemplate(
    input_variables=["job_description", "resume_text"],
    template=template
)