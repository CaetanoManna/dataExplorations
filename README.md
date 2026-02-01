
```markdown
# 🏀 dataExplorations - NBA Games ML Pipeline

Um projeto para extrair, transformar e modelar dados da NBA (2019-24) com um pipeline completo,
integração Docker.

**Principais mudanças recentes**
- Orquestração do pipeline via `main.py` (executa toda a sequência automaticamente).
- Dockerfile + `docker-compose.yaml` para build e execução em container.
- `config.yaml` centralizado para parâmetros e paths.

## 🏗️ Estrutura do Projeto (atualizada)

```
dataExplorations/
├── data/                          # Dados brutos e processados
├── src/
│   ├── extract/                  # Extração de dados (capture_games.py)
│   ├── transform/                # Limpeza e transformações (increment_data.py)
│   ├── quality/                  # Validação (data_quality.py)
│   └── ml/                       # ML, features,treino
│       ├── build_features.py
│       ├── train_baseline.py
├── notebooks/                     # Notebooks interativos
├── main.py                        # Orquestrador do pipeline
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
└── README.md
```

## 🚀 Quick Start (atualizado)

### Requisitos
- Python 3.10+ (recomendado 3.12)
- Docker (opcional, recomendado para produção)

### Instalação local

```powershell
# Entre na pasta do projeto
cd dataExplorations

# Crie e ative venv (Windows)
python -m venv venv-proj
venv-proj\Scripts\activate

# Instale dependências
pip install -r requirements.txt
```

### Executar pipeline completo (local)

```powershell
# Orquestrador executa: extract -> transform -> quality -> features -> train -> forecast
python main.py
```



### Executar com Docker (recomendado)

```powershell
# Build + up
docker-compose up --build

# Ver logs
docker-compose logs -f data-pipeline

# Parar
docker-compose down
```

## 📚 Principais componentes e onde olhar

- **Orquestração:** `main.py` — executa todas as etapas em sequência e trata erros.
- **Extração:** `src/extract/capture_games.py` — captura dados da NBA API.
- **Transformação:** `src/transform/increment_data.py` — limpa e gera `players_2024_processed.csv` e `games_to_ml.csv`.
- **Validação:** `src/quality/data_quality.py` — schemas e checks com `pandera` / `great_expectations`.
- **Features:** `src/ml/build_features.py` — engenharia de features para ML.
- **Treino baseline:** `src/ml/train_baseline.py` — modelo de baseline (LogisticRegression).


## 🐳 Docker

- O `Dockerfile` instala dependências e executa `main.py` por padrão.
- `docker-compose.yaml` monta `./data` e `./notebooks` como volumes para persistência.

## ⚙️ Configuração

- Parâmetros centrais em `config.yaml` (paths, modelo, forecast horizon, métodos habilitados).
- Para gravação incremental em CSV use `mode='a'`(ver função de escrita em `src/transform/increment_data.py`).

## 🧪 Testes e exemplos

- `examples.py` contém exemplos práticos para rodar forecasts em um jogador, múltiplas métricas e batch.
- `notebooks/player_forecast_5years.ipynb` tem tutorial interativo.

## ✅ Observações finais


- Caso você tenha revertido arquivos localmente, garanta que `main.py` esteja presente e atualizado antes de rodar.

## 🔧 Comandos úteis

```powershell
# Rodar pipeline
python main.py


# Docker
docker-compose up --build
```

## 👤 Autor

Caetano Manna | Feb 2026

---

MIT
```
