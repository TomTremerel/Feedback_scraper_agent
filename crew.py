
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv

load_dotenv()
@CrewBase
class CompanyFeedbackCrew:
    """Crew pour collecter et analyser les retours sur l'entreprise"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def web_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['web_scraper'],
            verbose=True,
            memory = True, 
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        )

    @agent
    def feedback_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['feedback_analyst'],
            verbose=True,
            memory = True,
        )

    @task
    def scrape_task(self) -> Task:
        return Task(
            config=self.tasks_config['scrape_task']
        )

    @task
    def analyze_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_task'],
            output_file= "feedback_output/report"
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
