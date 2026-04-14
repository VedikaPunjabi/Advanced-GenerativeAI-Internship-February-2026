import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from prompts.screening_prompt import screening_prompt

load_dotenv()

def get_evaluation_chain():
    # Initialize Gemini model
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    
    # Build the pipeline using LCEL: Prompt -> Gemini -> JSON Parser
    chain = screening_prompt | model | JsonOutputParser()
    return chain