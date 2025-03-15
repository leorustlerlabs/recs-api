#!/bin/bash

# Vercel deployment script
# Run this script locally to deploy to Vercel

echo "Deploying to Vercel..."

# Step 1: Make sure Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
  echo "Vercel CLI not found. Installing..."
  npm install -g vercel
fi

# Step 2: Make sure you're logged in
echo "Step 2: Ensuring you're logged in to Vercel..."
vercel whoami || vercel login

# Step 3: Deploy the application
echo "Step 3: Deploying the application..."
vercel --prod

echo "Deployment completed! Your API should now be available at the URL shown above."