from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun


class blog_post_content_writer_tasks():
    def research_task(self):
    
        return Task(
        description='Identify the next big trend in AI by searching the internet.',
        expected_output='A bullet list summary of the top 5 most important AI news articles found during the search.',
        agent='researcher',
         )
    
    def insights_task(self):
        
        return Task(
        description='Identify a few key insights from the data in points format. Dont use any tool.',
        expected_output='A bullet list summary of the top 5 insights gleaned from analyzing the AI news articles.',
        agent='insight_researcher',
        )

    def writer_task(self):
        
        return Task(
        description='Write a short blog post with subheadings. Dont use any tool.',
        expected_output='A concise blog post structured with subheadings, summarizing the identified AI trends and insights.',
        agent='writer',
        )
    
    def format_task(self):
    
        
        return Task(
        description='Convert the text into markdown format. Dont use any tool.',
        expected_output='The blog post content converted into markdown format, ready for publishing.',
        agent='formater',
        
        )       
    
        
        
        
        
        