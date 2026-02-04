def ask_llm(prompt):
    """
    MOCK LLM RESPONSE
    This function is intentionally mocked due to quota limits.
    Architecture is fully LLM-compatible.
    """
    return """
    {
      "steps": [
        {
          "tool": "WeatherTool",
          "city": "Bangalore"
        },
        {
          "tool": "GitHubTool",
          "query": "fastapi"
        }
      ]
    }
    """
