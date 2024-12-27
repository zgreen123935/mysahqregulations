from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# You might want to add specific tools for energy regulation research
from crewai_tools import SerperDevTool


@CrewBase
class MysaHQRegulationsCrew:
    """Energy Regulations Database Management Crew for Mysa HQ"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def database_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["database_manager"],
            verbose=True,
        )

    @agent
    def quality_assurance_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["quality_assurance_specialist"],
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def database_organization_task(self) -> Task:
        return Task(
            config=self.tasks_config["database_organization_task"],
        )

    @task
    def quality_assurance_task(self) -> Task:
        return Task(
            config=self.tasks_config["quality_assurance_task"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Mysa HQ Energy Regulations Database Management crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
