import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
RAW_FILE = DATA_DIR / "pbp_2023_2024.parquet"
PROCESSED_DIR = DATA_DIR / "processed"
PROCESSED_DIR.mkdir(exist_ok=True)

# Lue raakadata
pbp = pd.read_parquet(RAW_FILE)

print(f"Ladattu {len(pbp)} riviä dataa")
print(f"Sarakkeet: {pbp.columns.tolist()[:20]}...")

# Aggregoi pelaajatilastot: passers
passer_stats = pbp[pbp['passer_player_id'].notna()].groupby(
    ['passer_player_id', 'passer_player_name', 'season', 'week']
).agg({
    'passing_yards': 'sum',
    'pass_touchdown': 'sum',
    'interception': 'sum',
    'complete_pass': 'sum',
    'pass_attempt': 'sum'
}).reset_index()
passer_stats.columns = ['player_id', 'player_name', 'season', 'week', 'passing_yards', 'passing_td', 'interceptions', 'completions', 'attempts']

# Aggregoi pelaajatilastot: rushers
rusher_stats = pbp[pbp['rusher_player_id'].notna()].groupby(
    ['rusher_player_id', 'rusher_player_name', 'season', 'week']
).agg({
    'rushing_yards': 'sum',
    'rush_touchdown': 'sum'
}).reset_index()
rusher_stats.columns = ['player_id', 'player_name', 'season', 'week', 'rushing_yards', 'rushing_td']

# Aggregoi pelaajatilastot: receivers
receiver_stats = pbp[pbp['receiver_player_id'].notna()].groupby(
    ['receiver_player_id', 'receiver_player_name', 'season', 'week']
).agg({
    'receiving_yards': 'sum',
    'pass_touchdown': 'sum',
    'complete_pass': 'sum'
}).reset_index()
receiver_stats.columns = ['player_id', 'player_name', 'season', 'week', 'receiving_yards', 'receiving_td', 'receptions']

# Tallennetaan aggregoidut tilastot
passer_stats.to_parquet(PROCESSED_DIR / "passer_stats_weekly.parquet", index=False)
rusher_stats.to_parquet(PROCESSED_DIR / "rusher_stats_weekly.parquet", index=False)
receiver_stats.to_parquet(PROCESSED_DIR / "receiver_stats_weekly.parquet", index=False)

print(f"\nTallennettu pelaajatilastot:")
print(f"  Passers: {len(passer_stats)} viikkotilastoa")
print(f"  Rushers: {len(rusher_stats)} viikkotilastoa")
print(f"  Receivers: {len(receiver_stats)} viikkotilastoa")
print(f"\nTiedostot tallennettu: {PROCESSED_DIR}")
