# NFL Betting Analytics

## Overview
This project collects and analyzes NFL game statistics from a betting perspective. It's a Python-based data analytics tool for fetching player and team statistics, defensive stats, and offensive efficiency data.

## Project Structure
- `scripts/data_fetch.py` - Main data fetching script
- `requirements.txt` - Python dependencies

## Current State
- Python 3.11 environment configured
- All dependencies installed and configured
- Workflow configured to run the data fetching script
- Ready to run NFL data analytics operations

## Recent Changes
- October 14, 2025: Initial Replit environment setup
  - Installed Python 3.11
  - Installed all required dependencies
  - Added NFL-specific data library (nfl_data_py)
  - Updated .gitignore for Python best practices
  - Configured console workflow for script execution

## Running the Project
The main script can be executed via the configured workflow, which runs `python scripts/data_fetch.py`.

## Dependencies
- pandas (1.5.3) - Data analysis and manipulation
- requests - HTTP library for API calls
- beautifulsoup4 - Web scraping
- matplotlib - Data visualization
- nfl_data_py (0.3.3) - NFL data fetching library
- pyarrow (21.0.0) - Efficient data processing
