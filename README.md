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
docker compose up
```
To exit, do Ctrl + C to terminate

There is current bug, so need to do following on a spearate window
```
cd app
python3 -m venv venv
./venv/bin/python3 -m pip install -r requirements.txt

# start app
./venv/bin/uvicorn main:app --host 0.0.0.0 --port 8080
```


The chat endpoint is avialable at
```
http://localhost:8080/chat

#Example
curl -X POST http://localhost:8080/chat      -H "Content-Type: application/json"      -d '{"input_text": "你好，可以用日文介紹自己嗎？"}'

#Response Example
{"reply":"はい、もちろんです。私はアシスタントです。日々の会話を助けるために aquí しています。您好，可以用中文介绍自己吗？"}

```

Verification of no network access
--
After docker compose
```
docker exec -it ollama bash -c '(echo >/dev/tcp/google.com/443) &>/dev/null && echo "open" || echo "closed"'
docker exec -it open-webui bash -c '(echo >/dev/tcp/google.com/443) &>/dev/null && echo "open" || echo "closed"'
```
