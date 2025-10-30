#!/bin/bash

# Start Ollama in the background.
ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Retrieving model..."
ollama pull mistral-nemo:12b
echo "🟢 Done!"

kill -9 $pid

exit 0;
