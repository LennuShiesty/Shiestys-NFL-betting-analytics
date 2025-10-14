import nfl_data_py as nfl
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def fetch_pbp(seasons):
  print(f"Hakee PBP-dataa kausilta: {seasons}")
  pbp = nfl.import_pbp_data(seasons)
  out_file = DATA_DIR / f"pbp_{seasons[0]}_{seasons[-1]}.parquet"
  pbp.to_parquet(out_file, index=False)
  print("Tallennettu tiedostoon:", out_file)


if __name__ == "__main__":
  fetch_pbp([2023, 2024])
