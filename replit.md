# NFL Betting Analytics

## Overview
This project collects and analyzes NFL game statistics from a betting perspective. It's a Python-based data analytics tool for fetching player and team statistics, defensive stats, and offensive efficiency data.

## Project Structure
- `app.py` - Streamlit dashboard for visualizing NFL player stats
- `scripts/data_fetch.py` - Main data fetching script
- `scripts/enrich.py` - Data enrichment and player statistics aggregation
- `data/` - Raw and processed data files (gitignored)
  - `pbp_2023_2024.parquet` - Play-by-play data for 2023-2024 seasons (99,157 plays)
  - `processed/` - Aggregated weekly player statistics by season and week
- `requirements.txt` - Python dependencies

## Current State
- Python 3.11 environment configured
- All dependencies installed including Streamlit
- **Streamlit Dashboard running on port 5000**
- NFL play-by-play data loaded and processed successfully
- Weekly player statistics generated (by season and week):
  - 1,425 passer stats (passing yards, TDs, interceptions, completions, attempts)
  - 4,746 rusher stats (rushing yards, TDs)
  - 9,064 receiver stats (receiving yards, TDs, receptions)

## Recent Changes
- October 16, 2025: Added Streamlit dashboard
  - Created app.py with interactive NFL stats dashboard
  - Installed Streamlit
  - Updated enrich.py to include season column in aggregations
  - Re-processed data with season grouping
  - Configured Streamlit workflow on port 5000
  
- October 14, 2025: Initial Replit environment setup
  - Installed Python 3.11
  - Installed all required dependencies
  - Added NFL-specific data library (nfl_data_py)
  - Updated .gitignore for Python best practices
  - Fixed enrich.py to work with NFL play-by-play data structure
  - Successfully processed play-by-play data into weekly player statistics

## Running the Project
- **Main app**: Streamlit dashboard runs automatically (configured workflow on port 5000)
- **Data processing**: `python scripts/enrich.py` - regenerates processed statistics
- **Data fetching**: `python scripts/data_fetch.py` - fetches raw data

## Dashboard Features
- Interactive selection of player type (passers, rushers, receivers)
- Filter by season (2023, 2024) and week
- Top 10 players visualization with bar charts
- Detailed statistics table

## Dependencies
- streamlit (1.50.0) - Web dashboard framework
- pandas (1.5.3) - Data analysis and manipulation
- requests - HTTP library for API calls
- beautifulsoup4 - Web scraping
- matplotlib - Data visualization
- nfl_data_py (0.3.3) - NFL data fetching library
- pyarrow (21.0.0) - Efficient data processing
