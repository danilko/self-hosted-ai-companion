# offline-ollama-docker-compose
Sample Docker Compose for Offline Ollama Usage

Overall Explanation
--

Sample Example to use docker-compose to:
1. Perform download of ollama model with a container with network access into a share docker volume and auto stop
2. Run the ollama model on a container with bridge network with no external network access
3. Run the OpenWeb UI on another container with above bridge network with no external access

Start Up
--
Test in Fedora 41 with SELinux + Podman `sudo dnf install podman docker-switch` + Nvidia Toolkit Installation
```
mkdir -p ollama-data
mkdir -p open-webui-data
docker compose up
```
To exit, do Ctrl + C to terminate


Access
--
The Ollama is available at
```
http://localhost:11434/
```

The OpenWeb UI is available at
```
http://localhost:8080/
```

Verification of no network access
--
After docker compose
```
docker exec -it ollama bash -c '(echo >/dev/tcp/google.com/443) &>/dev/null && echo "open" || echo "closed"'
docker exec -it open-webui bash -c '(echo >/dev/tcp/google.com/443) &>/dev/null && echo "open" || echo "closed"'
```
