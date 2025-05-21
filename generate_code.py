# GPT-4 call + code generation
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from gpt_prompt import BASE_PROMPT
from manim_file_tools import generate_manim_file, edit_manim, run_manim

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API"))
file_path= os.getcwd()+"/my-project/main.py"

def generate_code(prompt: str):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
        ),
        contents=prompt
    )

    return response

response = generate_code(f'''{BASE_PROMPT}---This is user input:create an demo of forward neural network, use animation 
                         and transformation along with colors make sure nothing is overlapping and import neccasory libraires ''')

print("\nCode generated.\n")

generate_manim_file(file_path, response.text)

edit_manim(file_path)

run_manim(file_path)