# 🏀 dataExplorations - NBA Games ML Pipeline

Um projeto de **Data Engineering** que constrói um pipeline completo de extração, transformação e aprendizado de máquina para prever resultados de jogos da NBA.

## 📋 Objetivo

Explorar dados de jogos da NBA (temporada 2023-24) e construir modelos preditivos para:
- Analisar padrões de desempenho das equipes
- Prever vencedores baseado em histórico de pontuação e taxa de vitória
- Validar estratégias de modelagem temporal

## 🏗️ Estrutura do Projeto

```
dataExplorations/
├── data/                          # Dados brutos e processados
│   ├── games_2024_raw.csv        # Dados extraídos da API (bruto)
│   ├── games_2024_processed.csv  # Dados limpos e filtrados
│   └── games_to_ml.csv           # Dataset preparado para ML
├── src/
│   ├── extract/                  # Extração de dados
│   │   └── capture_games.py      # API da NBA
│   ├── transform/                # Transformações e limpeza
│   │   └── increment_data.py     # Pipeline de processamento
│   ├── quality/                  # Validação de dados
│   │   └── data_quality.py       # Assertions de qualidade
│   └── ml/                       # Machine Learning
│       ├── build_features.py     # Feature engineering
│       ├── train_baseline.py     # Treinamento do modelo
│       └── metrics.py            # Avaliação
├── notebooks/                     # Análises exploratórias (Jupyter)
├── requirements.txt               # Dependências Python
└── README.md                      # Este arquivo
```

## 🚀 Quick Start

### Requisitos
- Python 3.10+
- pip

### 1. Instalação

```bash
# Clonar/navegar para o projeto
cd dataExplorations

# Criar ambiente virtual
python -m venv venv-proj

# Ativar ambiente
# Windows:
venv-proj\Scripts\activate
# Linux/Mac:
source venv-proj/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Executar Pipeline Completo

```bash
# 1️⃣ Extrair dados da NBA API
python src/extract/capture_games.py

# 2️⃣ Transformar e limpar dados
python src/transform/increment_data.py

# 3️⃣ Treinar modelo
python src/ml/train_baseline.py
```

## 📊 Pipeline de Dados

```
NBA API
   ↓
[capture_games.py] → games_2024_raw.csv
   ↓
[increment_data.py] → games_2024_processed.csv
                   → games_to_ml.csv
   ↓
[build_features.py] → Features engineering
   ↓
[train_baseline.py] → Modelo Logistic Regression
   ↓
Predições + Métricas (Accuracy, ROC AUC)
```

## 🔧 Tecnologias

| Componente | Tecnologia |
|-----------|-----------|
| Extração | `nba_api` |
| Processamento | `pandas`, `numpy` |
| ML | `scikit-learn` |
| Visualização | `matplotlib`, `seaborn` |

## 📈 Features Atuais

- `pts_avg_diff`: Diferença média de pontos marcados (home vs visitor)
- `winrate_diff`: Diferença de taxa de vitória

## 🎯 Resultados Esperados

Após executar o pipeline:
- **Accuracy**: ~55-65% (baseline)
- **ROC AUC**: ~0.55-0.65

## 🔮 Próximas Melhorias

- [ ] Expandir features (últimas 5 games, lesões, descanso)
- [ ] Adicionar validação cruzada
- [ ] Hyperparameter tuning
- [ ] Persistência de modelos
- [ ] Dashboard com resultados
- [ ] Notebooks exploratórios completos

## ⚙️ Configuração

Atualmente os paths estão hardcoded. Para customizar:
- Edite os `PATH` em cada script
- *Futuro*: Criar `config.yaml` centralizado

## 📝 Notas

- Validação temporal: dados anteriores a 2024-02-01 para treino, posteriores para teste
- Sem data leakage: features usam apenas histórico anterior à data do jogo
- Assertions de qualidade em `data_quality.py`

## 👤 Autor

Caetano Manna | Jan 2026

## 📄 Licença

MIT
