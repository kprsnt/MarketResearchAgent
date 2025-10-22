import google.generativeai as genai
import os
import argparse
from rich.console import Console
from rich.markdown import Markdown

def main():
    """
    Main function to run the market research agent.
    """
    parser = argparse.ArgumentParser(description="Market Research Agent")
    parser.add_argument("topic", help="The topic or keyword for market research.")
    parser.add_argument("--length", default="medium", choices=["short", "medium", "long"], help="The desired length of the report.")
    parser.add_argument("--sections", nargs='+', default=["all"], help="Specific sections to include in the report. 'all' includes every section.")
    parser.add_argument("--audience", default="business executives", help="The target audience for the report.")
    args = parser.parse_args()

    # Get the API key from the environment variable
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return

    # Configure the generative AI model
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Generate the market research report

    sections_str = ""
    if "all" in args.sections:
        sections_str = """
        - **Executive Summary:** A high-level overview of the market.
        - **Market Size and Growth:** Analysis of the current market size and projected growth.
        - **Key Trends:** Emerging trends and patterns in the market.
        - **Competitive Landscape:** A look at the key players and their market share.
        - **Opportunities and Challenges:** Potential opportunities for new entrants and existing challenges.
        - **Target Audience:** A description of the ideal customer profile."""
    else:
        sections_str = "\n".join([f"- **{section.replace('_', ' ').title()}**" for section in args.sections])


    prompt = f"""
    Generate a market research report on "{args.topic}" with a {args.length} length.
    The target audience for this report is {args.audience}.

    Please include the following sections in the report:
    {sections_str}

    Format the report using Markdown for clear readability.
    """
    console = Console()
    console.print("Generating market research report... Please wait.")
    try:
        response = model.generate_content(prompt)
        # Print the report
        markdown = Markdown(response.text)
        console.print(markdown)
    except Exception as e:
        console.print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
