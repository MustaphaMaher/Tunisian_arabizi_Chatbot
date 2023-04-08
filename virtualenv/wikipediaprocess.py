import wikipedia
def search_wikipedia(topic="France(pays)"):
    try:
        wikipedia.set_lang("fr")
        
        # Get the summary of search
        summary = wikipedia.summary(topic, sentences=2)
        
        return "🤖"+summary
    except wikipedia.exceptions.WikipediaException as e:
        return(f"Error: {e}")


