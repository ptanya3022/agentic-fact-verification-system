

import wikipedia

def search_wikipedia(query: str, sentences: int = 3) -> str:
    try:
        summary = wikipedia.summary(query, sentences=sentences)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error. Try being more specific. Options: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return "No page found for the given query."
    except Exception as e:
        return f"An error occurred during Wikipedia search: {str(e)}"

