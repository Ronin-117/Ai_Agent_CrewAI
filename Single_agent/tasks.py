from crewai import Task

from agents import Agent

# Research task
Agent_task = Task(
  description=(
    "Give instructions for the symptoms to be checked for identifying {topic}."
    "Focus of recovering from the illnes in such a way the it does'nt over rely on medicine"
    "Your final report should clearly articulate symptoms"
    "recovery plan, medication"
  ),
  expected_output='A comprehensive 3 paragraphs long report on {topic}',
  agent=Agent,
  output_file='op.md'
)

