#!/bin/bash

# Start Ollama in the background.
ollama run gemma3:12b
# Record Process ID.
pid=$!

wait $pid
