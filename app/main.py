import google.generativeai as genai
import os
import markdown2
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Get the absolute path to the directory containing main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mount the static files directory
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


class ResearchRequest(BaseModel):
    topic: str
    length: str = "medium"
    sections: Optional[List[str]] = ["all"]
    audience: str = "business executives"


def generate_report_content(topic: str, length: str, sections: List[str], audience: str) -> str:
    """
    Generates the market research report content using the Gemini API.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY environment variable not set."

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    sections_str = ""
    if "all" in sections:
        sections_str = """
        - **Executive Summary:** A high-level overview of the market.
        - **Market Size and Growth:** Analysis of the current market size and projected growth.
        - **Key Trends:** Emerging trends and patterns in the market.
        - **Competitive Landscape:** A look at the key players and their market share.
        - **Opportunities and Challenges:** Potential opportunities for new entrants and existing challenges.
        - **Target Audience:** A description of the ideal customer profile."""
    else:
        sections_str = "\n".join([f"- **{section.replace('_', ' ').title()}**" for section in sections])

    prompt = f"""
    Generate a market research report on "{topic}" with a {length} length.
    The target audience for this report is {audience}.

    Please include the following sections in the report:
    {sections_str}

    Format the report using Markdown for clear readability.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate_report")
async def generate_report(request: ResearchRequest):
    report_markdown = generate_report_content(request.topic, request.length, request.sections, request.audience)
    report_html = markdown2.markdown(report_markdown, extras=["tables", "fenced-code-blocks", "spoiler"])
    return {"report": report_html}
