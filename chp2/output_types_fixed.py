from agents import Agent
from pydantic import BaseModel, ConfigDict
from typing_extensions import TypedDict

class Task(TypedDict):
    id: int
    description: str

class ResearchPlanModel(BaseModel):
    tasks: list[Task]
    """Numbered tasks for research."""

    model_config = ConfigDict(extra='forbid')

instructions = """
You are a research planning assistant.

**TASK INSTRUCTIONS**
- You will be given a research topic.
- Your task is to provide a plan on how to research this topic.
- Output 5 concise tasks (5 words or less) to your plan.
"""

agent = Agent(name="Research Planner", instructions=instructions, output_type=ResearchPlanModel)