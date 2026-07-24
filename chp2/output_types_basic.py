from pydantic import BaseModel
from agents import Agent

class ResearchPlanModel(BaseModel):
    tasks: List[str]
    """A list of tasks to perform for research."""

instructions = """
You are a research planning assistant.

**TASK INSTRUCTIONS**
- You will be given a research topic.
- Your task is to provide a plan on how to research this topic.
- Output 5 concise tasks (5 words or less) to your plan.
"""

agent = Agent(name="Research Planner", instructions=instructions, output_type=ResearchPlanModel)

#EXAMPLE OUTPUT