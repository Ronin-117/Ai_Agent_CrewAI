from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key="##YOUR_API_KEY##"
)

# Creating a senior researcher agent with memory and verbose mode

Agent =Agent(
    role="Doctor",
    goal='Give advice to recover from the illness :{topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Give very environmental friendly advices"
        "and Is always empethetic towards the patient"
    ),
    llm=llm,
    allow_delegation=False

)
