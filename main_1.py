from agents import blog_post_content_writer
from tasks import blog_post_content_writer_tasks

from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun

from crewai_tools import tool
search_tool = DuckDuckGoSearchRun()


agents = blog_post_content_writer()

researcher =agents.researcher()
insight_researcher =agents.insight_researcher()
writer =agents.writer()
formater =agents.formater()


tasks = blog_post_content_writer_tasks()

research_task = tasks.research_task()
insights_task = tasks.insights_task()
writer_task = tasks.writer_task()
format_task = tasks.format_task()