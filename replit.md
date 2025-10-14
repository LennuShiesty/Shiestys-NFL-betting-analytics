# NFL Betting Analytics

## Overview
This project collects and analyzes NFL game statistics from a betting perspective. It's a Python-based data analytics tool for fetching player and team statistics, defensive stats, and offensive efficiency data.

## Project Structure
- `scripts/data_fetch.py` - Main data fetching script
- `scripts/enrich.py` - Data enrichment and player statistics aggregation
- `data/` - Raw and processed data files (gitignored)
  - `pbp_2023_2024.parquet` - Play-by-play data for 2023-2024 seasons (99,157 plays)
  - `processed/` - Aggregated weekly player statistics
- `requirements.txt` - Python dependencies

## Current State
- Python 3.11 environment configured
- All dependencies installed and configured
- Workflow configured to run the data fetching script
- NFL play-by-play data loaded and processed successfully
- Weekly player statistics generated:
  - 1,067 passer stats (passing yards, TDs, interceptions, completions, attempts)
  - 3,638 rusher stats (rushing yards, TDs)
  - 6,663 receiver stats (receiving yards, TDs, receptions)

## Recent Changes
- October 14, 2025: Initial Replit environment setup
  - Installed Python 3.11
  - Installed all required dependencies
  - Added NFL-specific data library (nfl_data_py)
  - Updated .gitignore for Python best practices
  - Configured console workflow for script execution
  - Fixed enrich.py to work with NFL play-by-play data structure
  - Successfully processed play-by-play data into weekly player statistics

## Running the Project
- Main workflow: `python scripts/data_fetch.py` (configured in workflow)
- Process play-by-play data: `python scripts/enrich.py`

## Dependencies
- pandas (1.5.3) - Data analysis and manipulation
- requests - HTTP library for API calls
- beautifulsoup4 - Web scraping
- matplotlib - Data visualization
- nfl_data_py (0.3.3) - NFL data fetching library
- pyarrow (21.0.0) - Efficient data processing
