from dotenv import load_dotenv
from openai import OpenAI
import os

from ania_rid.excel_extract import extract_pdf_text
from ania_rid.save_output import save_response_to_excel
from prompts.project_desc import PROJECT_CONTEXT, LITERATURE_CONTEXT
from prompts.review_questions import REVIEW_QUESTIONS
from prompts.system_prompt import system_prompt
from prompts.pydantic_review import QuantitativeReviewEntry

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

article_name = input("Wpisz nazwę pliku do sparsowania:")

ARTICLE_PATH = f"articles/{article_name}"
ARTICLE_TEXT = extract_pdf_text(ARTICLE_PATH)

response = client.responses.parse(
    model="gpt-5",
    input=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"""
Project context:
{PROJECT_CONTEXT}

Additional theoretical background:
{LITERATURE_CONTEXT}

Fill the structured form:
{REVIEW_QUESTIONS}

Article text:
---
{ARTICLE_TEXT}
---
        """}
    ],
    text_format=QuantitativeReviewEntry,
    timeout=180
)

save_response_to_excel(response)
print("DONE!!!")