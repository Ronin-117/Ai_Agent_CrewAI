from crewai import Crew,Process
from tasks import Agent_task
from agents import Agent

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[Agent],
    tasks=[Agent_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'Fever'})

print(result)