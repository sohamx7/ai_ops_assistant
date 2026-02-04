# AI Operations Assistant

An AI-powered operations assistant that accepts a natural-language task, converts it into a structured execution plan, calls real-world APIs, and returns a validated result using a multi-agent architecture.

---

## Overview
This project demonstrates an **agent-based AI system** that separates reasoning, execution, and validation into independent components.

The system:
- Accepts a natural language task
- Plans execution steps using an AI-style planner
- Executes real third-party API calls
- Returns a structured and validated output

The focus of this project is **AI orchestration and system design**, not UI development or model training.

---

## Architecture

The system follows a **Planner – Executor – Verifier** design to avoid monolithic prompts and ensure clear separation of responsibilities.

### Planner Agent
- Converts a natural language task into a structured JSON execution plan
- Determines which tools (APIs) should be used and with what parameters
- Designed to be compatible with LLMs using schema-constrained outputs

### Executor Agent
- Iterates through the execution plan
- Calls the appropriate tools (APIs)
- Collects raw results from each API call

### Verifier Agent
- Validates completeness of execution results
- Handles partial failures gracefully
- Formats the final structured response

---




## Folder Structure 

```text
ai_ops_assistant/
│
├── agents/
│   ├── planner.py        # Planner Agent: converts task into execution steps
│   ├── executor.py       # Executor Agent: runs tools based on the plan
│   └── verifier.py       # Verifier Agent: validates and formats output
│
├── tools/
│   ├── weather_tool.py   # WeatherTool: fetches weather using OpenWeather API
│   └── github_tool.py    # GitHubTool: fetches repositories using GitHub API
│
├── llm/
│   └── llm_client.py     # LLM interface (mocked for local execution)
│
├── main.py               # Entry point to run the application
├── requirements.txt      # Python dependencies
├── .env.example          # Example environment variables
├── README.md             # Project documentation
└── venv/                 # Virtual environment (not committed)
```




## Installation

Follow the steps below to install and run the project locally on your machine.

### 1. Clone the repository
```bash
git clone <your-github-repository-url>
cd ai_ops_assistant 
## Create a virtual environment
```bash python -m venv venv```

## Windows
```bash
venv\Scripts\activate
```


## macOS / Linux

```source venv/bin/activate```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Configure environment variables

Create a .env file from the example file:

```cp .env.example .env```
(Edit .env and add your API keys.)

## Run the application
```python main.py```

## Integrated APIs

- GitHub REST API – Used to fetch repository details such as name, stars, and URL
- OpenWeather API – Used to fetch current weather information by city


## Example Prompts

You can test the system using the following natural language tasks:

1. Get Bangalore weather and top FastAPI GitHub repositories
2. Fetch weather for Delhi and popular Django repositories
3. Show current weather in Mumbai and trending Python GitHub projects
4. Get Pune weather and trending React repositories


## Known Limitations / Tradeoffs

- The planner currently uses rule-based logic for intent extraction; a live LLM can be plugged in for more robust natural language understanding.
- Tool execution is sequential; parallel execution is not implemented.
- API responses are not cached, which may lead to repeated external API calls.
- Weather data retrieval depends on a valid API key; when unavailable, the system returns a graceful error message instead of failing.






