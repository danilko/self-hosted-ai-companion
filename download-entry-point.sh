#!/bin/bash

# Start Ollama in the background.
ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Retrieving model..."
ollama pull gemma3n:latest
ollama pull gemma3:4b
ollama pull gemma3:12b
echo "🟢 Done!"

kill -9 $pid

exit 0;
