from agents.fact_agent import verify_claim

def run_fact_check_pipeline(claim: str) -> dict:
    """
    Pipeline to handle end-to-end fact verification for a given claim.

    Args:
        claim (str): The statement to be fact-checked.

    Returns:
        dict: {
            "verdict": str,
            "justification": str,
            "contexts": List[str]
        }
    """
    try:
        result = verify_claim(claim)
        return {
            "verdict":result.get("verdict","Error"),
            "justification":result.get("justification","No justification provided."),
            "contexts":result.get("contexts",[])

        }
        
    except Exception as e:
        return {
            "verdict": "Error",
            "justification": str(e),
            "contexts": []
        }
