import google.generativeai as genai # type: ignore
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

configuration = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain"
}  

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=configuration
)
def analyse_resumee_gemini(resume_content, job_description):
    prompt =  f"""
    You are a professional resume analyzer.

    Resume:
    {resume_content}

    Job Description:
    {job_description}

    Task:
    -Analyze the resume against the job description.
    -Give a match score out of 100.
    -Highlight missing skills or experiences.
    -Suggest improvements.

    Return the result in structured format:
    Match Score: XX/100
    Missing Skills:
    - ...
    Suggestions:
    - ...
    Summary:
    ...
    """
    
    response = model.generate_content(prompt)
    
    return response.text