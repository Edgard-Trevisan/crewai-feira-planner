# Aplicativo de Planejamento Estratégico para Feiras

Este projeto utiliza o framework CrewAI para criar uma equipe de agentes de IA que trabalham juntos para desenvolver um plano estratégico de participação em feiras comerciais.

## Estrutura do Projeto

```
feira_app/
├── .env                    # Variáveis de ambiente e chaves de API
├── requirements.txt        # Dependências do projeto
├── src/
│   ├── feira_app/
│   │   ├── __init__.py
│   │   ├── config/
│   │   │   ├── agents.yaml # Configuração dos agentes
│   │   │   └── tasks.yaml  # Configuração das tarefas
│   │   ├── crew.py         # Definição da equipe de agentes
│   │   └── main.py         # Ponto de entrada da aplicação
│   └── __init__.py
└── output/                 # Diretório onde os planos estratégicos serão salvos
```

## Requisitos

- Python 3.10+
- Chave de API OpenAI
- Chave de API Serper.dev (para pesquisa na web)

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
   ```
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```
     source venv/bin/activate
     ```
4. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
5. Configure as variáveis de ambiente no arquivo `.env`:
   ```
   OPENAI_API_KEY=sua_chave_api_openai
   SERPER_API_KEY=sua_chave_api_serper
   ```

## Uso

1. Ative o ambiente virtual
2. Execute o aplicativo:
   ```
   python -m src.feira_app.main
   ```

## Personalização

Você pode personalizar o tipo de feira e a região de interesse editando os parâmetros no arquivo `main.py`:

```python
inputs = {
    'tipo_feira': 'tecnologia',  # Altere para o tipo de feira desejado
    'regiao': 'Brasil'           # Altere para a região desejada
}
```

## Como Funciona

O aplicativo utiliza três agentes especializados:

1. **Pesquisador de Feiras**: Coleta informações sobre as principais feiras do setor
2. **Analista de Mercado**: Analisa tendências e oportunidades no mercado
3. **Planejador Estratégico**: Desenvolve um plano detalhado para participação nas feiras

Os agentes trabalham sequencialmente, com cada um utilizando os resultados do anterior para criar um plano estratégico completo.
