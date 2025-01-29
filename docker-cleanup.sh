#!/bin/bash

# Timestamp for log preservation
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
LOG_DIR="${HOME}/docker-logs"

# Create log directory if needed
mkdir -p "$LOG_DIR"

# Find existing containers using port 5678
CONTAINERS=$(docker ps -q --filter "publish=5678")

if [ -n "$CONTAINERS" ]; then
    echo "🔴 Found existing containers:"
    docker ps --filter "publish=5678"
    
    # Save logs before removal
    for CONTAINER in $CONTAINERS; do
        echo "💾 Saving logs for $CONTAINER to ${LOG_DIR}/${CONTAINER}_${TIMESTAMP}.log"
        docker logs "$CONTAINER" > "${LOG_DIR}/${CONTAINER}_${TIMESTAMP}.log" 2>&1
    done
    
    # Cleanup
    echo "🚮 Removing containers..."
    docker rm -f $CONTAINERS
fi

# Optional: Remove dangling images
echo "🧹 Cleaning up Docker artifacts..."
docker container prune -f
docker image prune -f

# Force rebuild next time
echo "🗑️  Removing existing calibre-stubgen images..."
docker image rm -f calibre-stubgen > /dev/null 2>&1 || true