

from utils.llm_utils import query_llm
from utils.retrieval_utils import search_wikipedia

def verify_claim(claim: str) -> dict:
    """
    Verify a factual claim by retrieving relevant context and analyzing with LLM.

    Args:
        claim (str): The factual statement or claim to verify.

    Returns:
        dict: A dictionary containing the original claim, verdict, justification, and supporting evidence.
    """
    # Step 1: Retrieve relevant documents
    context = search_wikipedia(claim)

    # Step 2: Query the LLM with the claim and context
    verdict, explanation = query_llm(claim, context)

    # Step 3: Return structured result
    return {
        "claim": claim,
        "verdict": verdict,
        "justification": explanation,
        "contexts": [context]
    }
