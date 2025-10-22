# Market Research Agent

This is a command-line tool that uses the Gemini API to generate market research reports on a given topic or keyword.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/market-research-agent.git
    cd market-research-agent
    ```

2.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API key:**
    - Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
    - Set it as an environment variable:
      ```bash
      export GEMINI_API_KEY="YOUR_API_KEY"
      ```

## Usage

To generate a market research report, run the `main.py` script with a topic as an argument:

```bash
python main.py "electric vehicles"
```

### Customization

You can customize the report using the following command-line arguments:

-   `--length`: The desired length of the report (`short`, `medium`, or `long`). Default is `medium`.
-   `--sections`: The specific sections to include in the report. You can list multiple sections separated by spaces. The default is `all`.
    -   Available sections: `executive_summary`, `market_size_and_growth`, `key_trends`, `competitive_landscape`, `opportunities_and_challenges`, `target_audience`
-   `--audience`: The target audience for the report. The default is `business executives`.

**Example:**

```bash
python main.py "artificial intelligence in healthcare" --length long --sections market_size_and_growth key_trends --audience "healthcare professionals"
```
