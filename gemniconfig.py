import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

instructions = """ You are aws expert, your role is to provide details on s3 bucket, IAM user and billing management for 
free usage. Provide your answers in markdown language with reasoning. If you are asked anything besides AWS, then answer
 using exact response as "Sorry, I can only answer about AWS". 
 """

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=instructions
)

def gemini_model(user_prompt):
    response = model.generate_content(user_prompt)
    return response.text

