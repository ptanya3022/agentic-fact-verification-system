

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the Gemini Pro 1.5 model
model = genai.GenerativeModel("gemini-1.5-flash")

def query_llm(claim: str, context: str) -> tuple:
    """
    Uses Google Gemini 1.5 Flash to verify the claim against the given context.

    Args:
        claim (str): The factual claim to verify.
        context (str): The supporting or refuting context text.

    Returns:
        Tuple[str, str]: Verdict ("True"/"False") and explanation.
    """
    prompt = f"""
    You are a fact-checking agent.

    Given the following CONTEXT and CLAIM, determine if the claim is supported by the context.
    
    CONTEXT:
    {context}

    CLAIM:
    {claim}

    Respond in the format:
    Verdict: True/False
    Explanation: <Your explanation here>
    """

    try:
        response = model.generate_content(prompt)
        text = response.text

        # Simple parsing logic (refine as needed)
        lines = text.strip().splitlines()
        verdict = "Unknown"
        explanation = ""

        for line in lines:
            if line.lower().startswith("verdict:"):
                verdict = line.split(":", 1)[1].strip()
            elif line.lower().startswith("explanation:"):
                explanation = line.split(":", 1)[1].strip()

        return verdict, explanation

    except Exception as e:
        return "Error", f"LLM processing failed: {str(e)}"
