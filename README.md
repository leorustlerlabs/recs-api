# RECS API

A simple API server for serving product recommendation results from the RECS system. The API serves results for different YouTube channels/influencers.

## Live API

The API is deployed and available at:
https://recs-2ac9vmvl8-leorustlerlabs-projects.vercel.app/

### Example Endpoints:
- List available channels: [/](https://recs-2ac9vmvl8-leorustlerlabs-projects.vercel.app/)
- MKBHD recommendations: [/api/recommendations/mkbhd](https://recs-2ac9vmvl8-leorustlerlabs-projects.vercel.app/api/recommendations/mkbhd)
- Test data: [/api/recommendations/test](https://recs-2ac9vmvl8-leorustlerlabs-projects.vercel.app/api/recommendations/test)

## Local Development Setup

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

## Running the Server Locally

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
3. Commit and push the changes to GitHub to trigger a new deployment

## Deployment

This project is deployed on Vercel. Any changes pushed to the main branch will automatically trigger a new deployment.

### Manual Deployment

To manually deploy the project:

1. Install Vercel CLI:
   ```
   npm install -g vercel
   ```

2. Log in to Vercel:
   ```
   vercel login
   ```

3. Deploy the project:
   ```
   vercel --prod
   ```

   Or use the provided script:
   ```
   ./deploy-to-vercel.sh
   ```

## Project Structure

- `app.py` - Main Flask application
- `test_results.json` - Default test results data
- `mkbhd_ytdlp_1video_with_quotes.json` - Results for MKBHD channel
- `requirements.txt` - Python dependencies
- `vercel.json` - Vercel deployment configuration
- `deploy-to-vercel.sh` - Script for deploying to Vercel