from tools.weather_tool import get_weather


from tools.github_tool import search_repos



def executor(plan):

    #It does NOT make decisions, it only executes stepsss
    
    results = {}

    for step in plan["steps"]:


        if step["tool"] == "WeatherTool":


            results["weather"] = get_weather(step["city"])

        elif step["tool"] == "GitHubTool":


            results["github"] = search_repos(step["query"])

    return results
