import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="NFL Data Dashboard", layout="wide")

DATA_DIR = Path(__file__).resolve().parent / "data" / "processed"

st.title("🏈 NFL Player Stats Dashboard")
st.write("Data perustuu NFL play-by-play 2023–2024 tilastoihin.")

data_type = st.sidebar.selectbox(
    "Valitse datatyyppi",
    ["Heittäjät (passers)", "Juoksijat (rushers)", "Kiinniottajat (receivers)"]
)

if data_type.startswith("Heittäjät"):
    df = pd.read_parquet(DATA_DIR / "passer_stats_weekly.parquet")
elif data_type.startswith("Juoksijat"):
    df = pd.read_parquet(DATA_DIR / "rusher_stats_weekly.parquet")
else:
    df = pd.read_parquet(DATA_DIR / "receiver_stats_weekly.parquet")

seasons = sorted(df["season"].unique())
season = st.sidebar.selectbox("Valitse kausi", seasons)
weeks = sorted(df[df["season"] == season]["week"].unique())
week = st.sidebar.selectbox("Valitse viikko", weeks)

df_week = df[(df["season"] == season) & (df["week"] == week)]

st.subheader(f"{data_type} – Kausi {season}, Viikko {week}")

if data_type.startswith("Heittäjät"):
    top = df_week.sort_values("passing_yards", ascending=False).head(10)
    st.bar_chart(top.set_index("player_name")["passing_yards"])
elif data_type.startswith("Juoksijat"):
    top = df_week.sort_values("rushing_yards", ascending=False).head(10)
    st.bar_chart(top.set_index("player_name")["rushing_yards"])
else:
    top = df_week.sort_values("receiving_yards", ascending=False).head(10)
    st.bar_chart(top.set_index("player_name")["receiving_yards"])

st.dataframe(top)
