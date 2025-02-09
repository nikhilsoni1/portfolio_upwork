#!/bin/bash

# Check if .env file exists
if [ ! -f .env ]; then
  echo ".env file not found"
  exit 1
fi

# Export variables from .env
while IFS='=' read -r key value; do
  # Ignore comments and empty lines
  if [[ -z "$key" || "$key" =~ ^# ]]; then
    continue
  fi

  # Remove leading/trailing whitespace
  key=$(echo "$key" | xargs)
  value=$(echo "$value" | xargs)

  # Export the variable
  export "$key=$value"

done < .env

echo "Environment variables loaded"
