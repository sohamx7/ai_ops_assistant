def planner(task: str):
    task_lower = task.lower()
    steps = []

    # Detect weather intent
    if "weather" in task_lower:
        words = task_lower.split()

        try:
            city_index = words.index("weather") - 1
            city = words[city_index].capitalize()
            
        except Exception:
            city = "Bangalore"

        steps.append({
            "tool": "WeatherTool",
            "city": city
        })

    
    if "github" in task_lower or "repository" in task_lower or "repositories" in task_lower:
        if "react" in task_lower:
            
            query = "react"
        elif "django" in task_lower:
            
            query = "django"
        elif "fastapi" in task_lower:
            query = "fastapi"


        else:
            query = "python"

        steps.append({
            "tool": "GitHubTool",
            "query": query
        })

    return {"steps": steps}
