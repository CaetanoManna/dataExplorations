#!/usr/bin/env python
"""
Main orchestration script that runs all data pipeline steps in sequence.
Executes: extract → transform → quality check → ml
"""

import sys
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

def run_pipeline():
    """Execute the complete data pipeline in order."""
    
    logger.info("=" * 60)
    logger.info("INICIANDO PIPELINE DE PROCESSAMENTO DE DADOS")
    logger.info("=" * 60)
    
    try:
        # Step 1: Extract data from NBA API
        logger.info("\n[STEP 1/5] Executando extração de dados (capture_games.py)...")
        from src.extract.capture_games import fetch_games_2024, capture_players
        fetch_games_2024()
        capture_players()
        logger.info("✓ Extração concluída com sucesso")
        
    except Exception as e:
        logger.error(f"✗ Erro na extração: {e}", exc_info=True)
        return False
    
    try:
        # Step 2: Transform and clean data
        logger.info("\n[STEP 2/5] Executando transformação de dados (increment_data.py)...")
        from src.transform.increment_data import clean_games, data_to_ml, clean_player_stats
        clean_games()
        data_to_ml()
        clean_player_stats()
        logger.info("✓ Transformação concluída com sucesso")
        
    except Exception as e:
        logger.error(f"✗ Erro na transformação: {e}", exc_info=True)
        return False
    
    try:
        # Step 3: Validate data quality
        logger.info("\n[STEP 3/5] Executando validação de qualidade (data_quality.py)...")
        from src.quality.data_quality import valid_schema_ml, valid_data_ml
        import pandas as pd
        from config import config
        
        df_ml = pd.read_csv(config.get("paths.data.ml"), parse_dates=["game_date"])
        
        schema = valid_schema_ml()
        schema.validate(df_ml)
        valid_data_ml(df_ml)
        logger.info("✓ Validação de qualidade concluída com sucesso")
        
    except Exception as e:
        logger.error(f"✗ Erro na validação: {e}", exc_info=True)
        return False
    
    try:
        # Step 4: Build ML features
        logger.info("\n[STEP 4/5] Construindo features ML (build_features.py)...")
        from src.ml.build_features import build_features
        import pandas as pd
        from config import config
        
        df_ml = pd.read_csv(config.get("paths.data.ml"), parse_dates=["game_date"])
        X, y, full_df = build_features(df_ml)
        logger.info(f"✓ Features construídas - Shape: {X.shape}")
        
    except Exception as e:
        logger.error(f"✗ Erro ao construir features: {e}", exc_info=True)
        return False
    
    try:
        # Step 5: Train baseline model
        logger.info("\n[STEP 5/5] Treinando modelo baseline (train_baseline.py)...")
        from src.ml.train_baseline import main
        main()
        logger.info("✓ Treinamento do modelo concluído com sucesso")
        
    except Exception as e:
        logger.error(f"✗ Erro no treinamento: {e}", exc_info=True)
        return False
    
    logger.info("\n" + "=" * 60)
    logger.info("✓ PIPELINE COMPLETO EXECUTADO COM SUCESSO!")
    logger.info("=" * 60)
    return True


if __name__ == "__main__":
    success = run_pipeline()
    sys.exit(0 if success else 1)
