"""
Exemplo de como usar o sistema de configuração centralizado.

Todos os scripts do projeto podem agora usar config.get() para acessar
configurações definidas em config.yaml, ao invés de hardcoding values.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from config import config

print("=" * 60)
print("SISTEMA DE CONFIGURAÇÃO CENTRALIZADO - EXEMPLOS")
print("=" * 60)

# 1. Acessar paths de dados
print("\n1. PATHS DE DADOS:")
print(f"   Raw data:       {config.get('paths.data.raw')}")
print(f"   Processed data: {config.get('paths.data.processed')}")
print(f"   ML data:        {config.get('paths.data.ml')}")

# 2. Acessar configuração NBA API
print("\n2. NBA API CONFIG:")
print(f"   Season:      {config.get('nba_api.season')}")
print(f"   League ID:   {config.get('nba_api.league_id')}")
print(f"   Season Type: {config.get('nba_api.season_type')}")

# 3. Acessar configuração do modelo
print("\n3. MODEL CONFIG:")
print(f"   Split date:       {config.get('model.split_date')}")
print(f"   Max iterations:   {config.get('model.max_iterations')}")
print(f"   Random state:     {config.get('model.random_state')}")

# 4. Acessar logging
print("\n4. LOGGING CONFIG:")
print(f"   Level:  {config.get('logging.level')}")
print(f"   Format: {config.get('logging.format')}")

# 5. Acessar feature engineering
print("\n5. FEATURE ENGINEERING CONFIG:")
print(f"   Window size:         {config.get('feature_engineering.window_size')}")
print(f"   Min games required:  {config.get('feature_engineering.min_games_required')}")

# 6. Acessar com valor padrão
print("\n6. COM VALOR PADRÃO (se chave não existe):")
print(f"   Non-existent key: {config.get('non.existent.key', default='DEFAULT_VALUE')}")

print("\n" + "=" * 60)
print("COMO USAR NOS SCRIPTS:")
print("=" * 60)
print("""
# Em qualquer script, importe config:
from config import config

# Acesse valores com notação de ponto:
output_path = config.get("paths.data.raw")
season = config.get("nba_api.season")
split_date = config.get("model.split_date")

# Com valor padrão:
value = config.get("some.key", default="default_value")

# Ou acesse via indexação:
paths = config["paths"]
raw_path = paths["data"]["raw"]
""")

print("\nTodos os scripts foram atualizados para usar este sistema!")
