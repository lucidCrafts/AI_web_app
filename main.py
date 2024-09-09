from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun

from crewai_tools import tool
search_tool = DuckDuckGoSearchRun()

llm_lmstudio = ChatOpenAI(
    openai_api_base="http://localhost:1234/v1",
    openai_api_key="lm-studio",                 
    model_name="local-model"
)


# Create a researcher agent
researcher = Agent(
  role='Senior Researcher',
  goal='Discover groundbreaking technologies',
  backstory='A curious mind fascinated by cutting-edge innovation and the potential to change the world, you know everything about tech.',
  verbose=True,
  #tools=[search],
  allow_delegation=False,
  llm=llm_lmstudio 
)

insight_researcher = Agent(
  role='Insight Researcher',
  goal='Discover Key Insights',
  backstory='You are able to find key insights from the data you are given.',
  verbose=True,
  allow_delegation=False,
  llm=llm_lmstudio 
)

writer = Agent(
  role='Tech Content Strategist',
  goal='Craft compelling content on tech advancements',
  backstory="""You are a content strategist known for 
  making complex tech topics interesting and easy to understand.""",
  verbose=True,
  allow_delegation=False,
  llm=llm_lmstudio 
)

formater = Agent(
  role='Markdown Formater',
  goal='Format the text in markdown',
  backstory='You are able to convert the text into markdown format',
  verbose=True,
  allow_delegation=False,
  llm=llm_lmstudio 
)

# Tasks
research_task = Task(
  description='Identify the next big trend in AI by searching the internet',
  agent=researcher,
  expected_output='A bullet list summary of the top 5 most important AI news articles found during the search.'
)

insights_task = Task(
  description='Identify a few key insights from the data in points format. Dont use any tool.',
  agent=insight_researcher,
  expected_output='A bullet list summary of the top 5 insights gleaned from analyzing the AI news articles.'
)

writer_task = Task(
  description='Write a short blog post with subheadings. Dont use any tool.',
  agent=writer,
  expected_output='A concise blog post structured with subheadings, summarizing the identified AI trends and insights.'
)

format_task = Task(
  description='Convert the text into markdown format. Dont use any tool.',
  agent=formater,
  expected_output='The blog post content converted into markdown format, ready for publishing.'
)
# Instantiate your crew
tech_crew = Crew(
  agents=[researcher, insight_researcher, writer, formater],
  tasks=[research_task, insights_task, writer_task, format_task],
  process=Process.sequential  # Tasks will be executed one after the other
)

# Begin the task execution
result = tech_crew.kickoff()
print(result)