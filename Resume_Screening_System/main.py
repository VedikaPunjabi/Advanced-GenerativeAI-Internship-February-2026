from itertools import chain
from chains.evaluator import get_evaluation_chain
import json

# Task Requirement: 1 Job Description 
job_desc = "Data Scientist with experience in Python, NLP, and LangChain."

# Task Requirement: 3 Resumes (Strong, Average, Weak) - These are simple text snippets representing different candidate profiles.
resumes = {
    "Strong": "Senior Data Scientist with 5 years in Python. Expert in LangChain and NLP.",
    "Average": "Software Developer proficient in Python and Java. Interested in AI.",
    "Weak": "Graphic Designer with 2 years experience in Adobe Creative Suite."
}

def run_screening():
    chain = get_evaluation_chain()
    
    for category, text in resumes.items():
        # Added extra newlines for clear separation between candidates
        print(f"\n{'='*20}") 
        print(f" EVALUATING: {category} Candidate")
        print(f"{'='*20}\n")
        
        result = chain.invoke({
            "job_description": job_desc,
            "resume_text": text
        })
        
        # indent=4 makes every JSON key start on a new line
        pretty_result = json.dumps(result, indent=4)
        print(pretty_result)
        print("\n")

if __name__ == "__main__":
    run_screening()