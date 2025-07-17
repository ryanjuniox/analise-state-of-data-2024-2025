# Data Hackers 2025 - State of Data 2024 Analysis

## Descrição do Projeto
Análise exploratória dos dados da pesquisa "State of Data 2024" da Data Hackers.

## Estrutura do Projeto

```
├── data/
│   ├── raw/                    # Dados originais, imutáveis
│   ├── interim/                # Dados intermediários durante processamento
│   └── processed/              # Dados finais, limpos e prontos para análise
├── notebooks/
│   ├── exploratory/            # Notebooks de análise exploratória
│   └── analysis/               # Notebooks de análise final
├── src/
│   ├── data/                   # Scripts para processamento de dados
│   ├── visualization/          # Scripts para visualizações
│   └── utils/                  # Funções utilitárias
├── reports/
│   ├── figures/                # Gráficos e visualizações geradas
│   └── final_report.md         # Relatório final
├── configs/                    # Arquivos de configuração
├── tests/                      # Testes unitários
├── requirements.txt            # Dependências do projeto
└── .gitignore                 # Arquivos a serem ignorados pelo Git
```

## Como usar
1. Instalar dependências: `pip install -r requirements.txt`
2. Executar notebooks na ordem numerada
3. Visualizar relatórios na pasta `reports/`

## Dados
- **Fonte**: State of Data 2024 - Kaggle
- **Arquivo original**: `Final Dataset - State of Data 2024 - Kaggle - df_survey_2024.csv`
