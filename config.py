"""
Configuração centralizada do projeto.
Carrega variáveis de config.yaml para uso em todo o projeto.
"""

import yaml
from pathlib import Path
from typing import Dict, Any


class Config:
    """Gerenciador de configurações do projeto."""
    
    _instance = None
    _config: Dict[str, Any] = {}
    
    def __new__(cls):
        """Singleton pattern - garante uma única instância."""
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance
    
    def _load_config(self):
        """Carrega config.yaml do diretório raiz do projeto."""
        config_path = Path(__file__).parent / "config.yaml"
        
        if not config_path.exists():
            raise FileNotFoundError(
                f"config.yaml não encontrado em {config_path}. "
                "Certifique-se que o arquivo existe."
            )
        
        with open(config_path, "r", encoding="utf-8") as f:
            self._config = yaml.safe_load(f)
    
    def get(self, key: str, default=None) -> Any:
        """
        Acessa configuração aninhada usando notação de ponto.
        
        Exemplo:
            config.get("paths.data.raw")
            config.get("model.max_iterations", default=1000)
        """
        keys = key.split(".")
        value = self._config
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        
        return value if value is not None else default
    
    def __getitem__(self, key: str):
        """Acesso via indexação: config["paths"]["data"]["raw"]"""
        return self._config.get(key)
    
    def reload(self):
        """Recarrega config.yaml (útil em testes)."""
        self._load_config()


# Instância global
config = Config()
