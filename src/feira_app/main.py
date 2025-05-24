#!/usr/bin/env python
"""
Aplicativo principal para planejamento estratégico de participação em feiras.
"""
import os
import sys
from dotenv import load_dotenv
from src.feira_app.crew import FeiraAppCrew

def run():
    """
    Executa a crew de planejamento de feiras.
    """
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    
    # Verifica se a API key do OpenAI está configurada
    if not os.getenv("OPENAI_API_KEY"):
        print("Erro: OPENAI_API_KEY não encontrada no arquivo .env")
        print("Por favor, adicione sua chave de API no arquivo .env")
        sys.exit(1)
    
    # Verifica se a API key do Serper está configurada
    if not os.getenv("SERPER_API_KEY"):
        print("Aviso: SERPER_API_KEY não encontrada no arquivo .env")
        print("A funcionalidade de pesquisa na web pode não funcionar corretamente")
    
    # Configuração dos inputs para a crew
    inputs = {
        'tipo_feira': 'avicultura',  # Tipo de feira a ser analisada
        'regiao': 'Brasil'           # Região de interesse
    }
    
    # Cria diretório de saída se não existir
    os.makedirs('output', exist_ok=True)
    
    # Executa a crew com os inputs definidos
    result = FeiraAppCrew().crew().kickoff(inputs=inputs)
    
    # Exibe o resultado final
    print("\nProcesso concluído com sucesso!")
    print(f"O plano estratégico foi salvo em: output/plano_estrategico_{inputs['tipo_feira']}.md")
    
    return result

if __name__ == "__main__":
    run()
