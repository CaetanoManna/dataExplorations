# 📋 IMPLEMENTAÇÃO: Config Centralizado

## ✅ O que foi feito

### 1. **config.yaml** - Arquivo de configuração centralizado
Contém todas as configurações do projeto:
- Paths de dados (raw, processed, ml)
- Configuração NBA API (season, league_id, season_type)
- Configuração do modelo (split_date, max_iterations, random_state)
- Configuração de logging
- Configuração de feature engineering

### 2. **config.py** - Gerenciador de configurações
Sistema Singleton que:
- Carrega `config.yaml` na inicialização
- Fornece método `.get()` com notação de ponto
- Suporta valores padrão
- Fácil reutilização em todos os scripts

### 3. Scripts atualizados
Todos os scripts foram modernizados para usar `config.get()`:

#### ✅ `src/extract/capture_games.py`
- Import do config
- Logging estruturado
- Configuração NBA API via config

#### ✅ `src/transform/increment_data.py`
- Paths centralizados
- Logging estruturado
- Removido hardcoding de paths

#### ✅ `src/ml/train_baseline.py`
- Correção de imports (agora funciona!)
- Config do modelo centralizada
- Logging com métricas formatadas

#### ✅ `src/ml/build_features.py`
- Config import adicionado
- Logging preparado

#### ✅ `src/quality/data_quality.py`
- Config import adicionado
- Logging estruturado

### 4. **requirements.txt** atualizado
Adicionado: `PyYAML>=6.0` para parsear YAML

### 5. **.gitignore** melhorado
Evita commitar:
- ✓ venv-proj/ (ambiente virtual inteiro)
- ✓ __pycache__/ e *.pyc
- ✓ Dados brutos
- ✓ Modelos treinados
- ✓ IDE configs (.vscode, .idea)

### 6. **config_example.py** - Exemplos de uso
Demonstra como usar o sistema:
```bash
python config_example.py
```

---

## 🎯 Vantagens

| Aspecto | Antes | Depois |
|---------|-------|--------|
| **Paths hardcoded** | ❌ Espalhado em 5 arquivos | ✅ Centralizado em 1 arquivo |
| **Mudar configuração** | ❌ Editar múltiplos scripts | ✅ Apenas editar config.yaml |
| **Ambientes diferentes** | ❌ Impossível | ✅ Criar config.prod.yaml, config.dev.yaml |
| **Versionamento** | ❌ Código muda | ✅ Config separada de código |
| **CI/CD** | ❌ Frágil | ✅ Injetar variáveis facilmente |
| **Logging** | ❌ Sem estrutura | ✅ Estruturado com logger |

---

## 📝 Exemplo de uso

**Antes:**
```python
OUTPUT_PATH = Path("data/games_2024_raw.csv")  # hardcoded
SEASON = "2023-24"  # hardcoded
print("Fetching games...")  # sem logging
```

**Depois:**
```python
from config import config
import logging

logger = logging.getLogger(__name__)

OUTPUT_PATH = Path(config.get("paths.data.raw"))  # de config.yaml
season = config.get("nba_api.season")  # de config.yaml
logger.info("Fetching games...")  # logging estruturado
```

---

## 🧪 Como testar

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Testar sistema de config
python config_example.py

# 3. Rodar scripts com nova config
python src/extract/capture_games.py
python src/transform/increment_data.py
python src/ml/train_baseline.py
```

---

## 🚀 Próximos passos

1. **Ambientes diferentes**
   - Criar `config.dev.yaml` e `config.prod.yaml`
   - Adicionar flag `--env` nos scripts

2. **Testes**
   - Criar pytest para testar config loading
   - Validar schema de config

3. **Secrets**
   - Adicionar suporte a variáveis de ambiente
   - Para credenciais, usar `.env` instead of config.yaml

4. **Logging**
   - Configurar logging.basicConfig() usando config
   - Adicionar logs em todos os scripts

---

## 📂 Estrutura após mudanças

```
dataExplorations/
├── config.yaml              # ← Config centralizada
├── config.py                # ← Gerenciador de config
├── config_example.py        # ← Exemplos de uso
├── .gitignore              # ← Atualizado
├── requirements.txt         # ← PyYAML adicionado
├── README.md
├── AVALIACACAO_CRITICA.md
└── src/
    ├── extract/
    │   └── capture_games.py (✅ atualizado)
    ├── transform/
    │   └── increment_data.py (✅ atualizado)
    ├── quality/
    │   └── data_quality.py (✅ atualizado)
    └── ml/
        ├── build_features.py (✅ atualizado)
        ├── train_baseline.py (✅ atualizado com fix de imports)
        └── metrics.py
```

---

## ✨ Status

🟢 **COMPLETO** - Sistema de config funcional e todos os scripts atualizados!

Teste com: `python config_example.py`
