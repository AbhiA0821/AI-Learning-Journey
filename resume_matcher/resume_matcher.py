import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
from pypdf import PdfReader

# ==========================
# Load Environment Variables
# ==========================
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found!")

client = Groq(api_key=api_key)

MODEL = "llama-3.3-70b-versatile"

# ==========================
# Pydantic Schema
# ==========================
class Student(BaseModel):
    experience: str | None
    skills: list[str] | None

schema = Student.model_json_schema()

# ==========================
# Read Resume PDF
# ==========================
def read_resume(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text + "\n"

    return resume_text


# ==========================
# Extract Resume Information
# ==========================
def extract_resume_info(resume_text: str):

    system_prompt = f"""
You are an HR assistant.

Extract the information according to this JSON schema:

{schema}

Return ONLY valid JSON.

If any field is missing, return null.
"""

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": f"""
This is a student's resume.

Extract ONLY the experience and skills.

Resume:

{resume_text}
"""
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0,
        response_format={"type": "json_object"}
    )

    return response.choices[0].message.content


# ==========================
# Main Function
# ==========================
def main():

    pdf_file = "Resume (AIML).pdf"

    print("=" * 50)
    print("Reading Resume...")
    print("=" * 50)

    resume_text = read_resume(pdf_file)

    print(resume_text)

    print("\n" + "=" * 50)
    print("Extracting Information...")
    print("=" * 50)

    result = extract_resume_info(resume_text)

    print(result)
print("ok")

# ==========================
# Run Program
# ==========================
if __name__ == "__main__":
    main()