# Market Research Agent

This is a web application that uses the Gemini API to generate market research reports on a given topic or keyword.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/market-research-agent.git
    cd market-research-agent
    ```

2.  **Navigate to the app directory:**
    ```bash
    cd app
    ```

3.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up your API key:**
    - Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
    - Set it as an environment variable:
      ```bash
      export GEMINI_API_KEY="YOUR_API_KEY"
      ```

## Running Locally

To run the web application locally, use `uvicorn`:

```bash
uvicorn main:app --reload
```

Then, open your browser and navigate to `http://127.0.0.1:8000`.

## Deployment

This project is configured for deployment on Vercel. To deploy, you can use the Vercel CLI or connect your GitHub repository to your Vercel account.

### Using Vercel CLI

1.  **Install the Vercel CLI:**
    ```bash
    npm install -g vercel
    ```

2.  **Deploy:**
    ```bash
    vercel
    ```

### Using GitHub

1.  Push your repository to GitHub.
2.  Go to your Vercel dashboard and create a new project.
3.  Connect your GitHub repository to Vercel.
4.  Vercel will automatically detect the `vercel.json` file and deploy your application.
