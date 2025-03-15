#!/bin/bash

# Railway deployment script
# Run this script locally to deploy to Railway

echo "Deploying to Railway..."

# Step 1: Make sure you're logged in
echo "Step 1: Ensuring you're logged in to Railway..."
railway whoami || railway login

# Step 2: Initialize or link to a Railway project
echo "Step 2: Initializing or linking to a Railway project..."
if [ -f .railway/project.json ]; then
  echo "Project already linked."
else
  echo "Creating a new Railway project..."
  railway init
fi

# Step 3: Deploy the application
echo "Step 3: Deploying the application..."
railway up

# Step 4: Get the deployment URL
echo "Step 4: Opening the project dashboard..."
railway open

echo "Deployment completed! Your API should now be available."
echo "To get your API URL, check the Railway dashboard or run 'railway status'"