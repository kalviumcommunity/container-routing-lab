# Container Routing Lab

Two small Python services:

| Service | What it does | Port inside its container |
|---|---|---|
| `api` (incident-api) | Returns incidents as JSON at `/health` and `/incidents` | 8080 |
| `dashboard` | Calls the API and shows how many incidents are open at `/` | 9000 |

**The Python logic is correct. Requests are not reaching the services.** Your job is to find where each request stops, fix it, and prove it works.

## Expected behaviour when everything is fixed

| Request (from your laptop) | Expected |
|---|---|
| `curl -i http://localhost:8080/health` | `HTTP/1.0 200 OK` and `{"status": "ok"}` |
| `curl -i http://localhost:9000/` | `HTTP/1.0 200 OK` and `Open incidents: 1` |

## Rules

- Keep the ports: API on 8080, dashboard on 9000, both inside the container and on your laptop.
- Do not change how incidents are counted or what the API returns.
- Use Docker on your own machine. No cloud, no paid tool.

## Start

```bash
docker build -t incident-api:lab ./api
sh run-api.sh
```

`run-api.sh` starts the API on its own. `compose.yaml` starts the API and the dashboard together:

```bash
docker compose up -d --build
```

## Useful commands

```bash
docker ps
docker port incident-api
docker logs incident-api
docker compose ps
docker compose logs dashboard
curl -i --max-time 3 http://localhost:8080/health
```

Windows: use PowerShell and type `curl.exe` instead of `curl`. Run `sh run-api.sh` from Git Bash, or copy the `docker run` line from the file into PowerShell.

## Clean up

```bash
docker rm -f incident-api
docker compose down
```
