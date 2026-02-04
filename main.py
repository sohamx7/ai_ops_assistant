from agents.planner import planner
from agents.executor import executor
from agents.verifier import verifier

task = input("Enter your task")


plan = planner(task)

execution_result = executor(plan)


final_result = verifier(task, execution_result)

print(final_result)
