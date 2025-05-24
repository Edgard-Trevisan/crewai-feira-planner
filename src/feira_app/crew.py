from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai_tools import SerperDevTool
from typing import List
import os
from dotenv import load_dotenv
from crewai.agents.agent_builder.base_agent import BaseAgent

# Carregar variáveis de ambiente
load_dotenv()

@CrewBase
class FeiraAppCrew():
    """Crew para planejamento estratégico de participação em feiras"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @before_kickoff
    def before_kickoff_function(self, inputs):
        """Função executada antes do início da execução da crew"""
        print(f"Iniciando análise para feira de {inputs.get('tipo_feira')} na região {inputs.get('regiao')}")
        return inputs

    @after_kickoff
    def after_kickoff_function(self, result):
        """Função executada após o término da execução da crew"""
        print(f"Análise concluída. Plano estratégico gerado com sucesso!")
        return result

    @agent
    def pesquisador_feira(self) -> Agent:
        """Cria o agente pesquisador de feiras"""
        # Obter a chave API do Serper
        serper_api_key = os.getenv("SERPER_API_KEY")
        
        return Agent(
            config=self.agents_config['pesquisador_feira'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def analista_mercado(self) -> Agent:
        """Cria o agente analista de mercado"""
        # Obter a chave API do Serper
        serper_api_key = os.getenv("SERPER_API_KEY")
        
        return Agent(
            config=self.agents_config['analista_mercado'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def planejador_estrategico(self) -> Agent:
        """Cria o agente planejador estratégico"""
        return Agent(
            config=self.agents_config['planejador_estrategico'],
            verbose=True
        )

    @task
    def pesquisa_feiras(self) -> Task:
        """Cria a tarefa de pesquisa de feiras"""
        return Task(
            config=self.tasks_config['pesquisa_feiras']
        )

    @task
    def analise_mercado(self) -> Task:
        """Cria a tarefa de análise de mercado"""
        return Task(
            config=self.tasks_config['analise_mercado']
        )

    @task
    def plano_estrategico(self) -> Task:
        """Cria a tarefa de planejamento estratégico"""
        return Task(
            config=self.tasks_config['plano_estrategico'],
            output_file='output/plano_estrategico_{tipo_feira}.md'
        )

    @crew
    def crew(self) -> Crew:
        """Cria a crew de planejamento de feiras"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
