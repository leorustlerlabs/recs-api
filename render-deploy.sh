#!/bin/bash

# Render API deployment script
# You'll need to create an API key in your Render dashboard: https://render.com/docs/api

# Set your API key and service ID
RENDER_API_KEY="your_api_key_here"
SERVICE_ID="your_service_id_here"

# Trigger a manual deploy
curl -X POST \
  "https://api.render.com/v1/services/$SERVICE_ID/deploys" \
  -H "Authorization: Bearer $RENDER_API_KEY" \
  -H "Content-Type: application/json"

echo "Deployment triggered for service $SERVICE_ID"