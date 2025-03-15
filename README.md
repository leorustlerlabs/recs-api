# RECS API

A simple API server for serving product recommendation results from the RECS system. The API serves results for different YouTube channels/influencers.

## Setup

1. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Server

```
source venv/bin/activate
python app.py
```

The server runs on http://0.0.0.0:5001 by default (to avoid conflicts with macOS AirPlay Receiver), making it accessible from other devices on the network.

## API Endpoints

- `GET /` - Lists all available channels and usage examples
- `GET /api/recommendations/<channel_id>` - Returns the results for a specific YouTube channel (e.g., `/api/recommendations/mkbhd`)
- `GET /api/results` - (Legacy) Returns the test results from the default JSON file

## Adding a New Channel

To add a new channel:
1. Add the channel's results JSON file to the project directory
2. Update the `CHANNEL_MAPPING` dictionary in `app.py` to include the new channel ID and its corresponding JSON file

## Project Structure

- `app.py` - Main Flask application
- `test_results.json` - Default test results data
- `mkbhd_ytdlp_1video_with_quotes.json` - Results for MKBHD channel
- `requirements.txt` - Python dependencies