
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

expected_output = {
        'summary': 'Summary of research findings',
        'data_points': 'Key financial metrics and insights'


class blog_post_content_writer():
    def researcher(self):
        return Agent(
        role='Tech Content Strategist',
        goal='Craft compelling content on tech advancements',
        backstory="""You are a content strategist known for 
        making complex tech topics interesting and easy to understand.""",
        verbose=True,
        allow_delegation=False,
        expected_output=expected_output,,
        llm=llm_lmstudio 
        )

    
    def insight_researcher(self):
        return Agent(
        role='Markdown Formater',
        goal='Format the text in markdown',
        backstory='You are able to convert the text into markdown format',
        verbose=True,
        allow_delegation=False,
        expected_output=expected_output,,
        llm=llm_lmstudio 
        )

        
    
    def writer(self):
        return Agent(
        role='Tech Content Strategist',
        goal='Craft compelling content on tech advancements',
        backstory="""You are a content strategist known for 
        making complex tech topics interesting and easy to understand.""",
        verbose=True,
        allow_delegation=False,
        expected_output=expected_output,,
        llm=llm_lmstudio 
        )
        
        
    def formater(self):
        return Agent(
        role='Markdown Formater',
        goal='Format the text in markdown',
        backstory='You are able to convert the text into markdown format',
        verbose=True,
        allow_delegation=False,
        expected_output=expected_output,,
        llm=llm_lmstudio 
        )
        
        
    