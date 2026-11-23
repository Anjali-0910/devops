# Program 2: Docker multi-stage build (Node.js)

```bash
cd p2
docker build -t program-2 .
docker images
docker run -d -p 3000:3000 program-2
docker ps
curl http://localhost:3000
docker stop <container_id>
```
Expected output: `Hello from Docker multi-stage build!`

(`npm install` is only needed if you want to run the app locally; package-lock.json is already included.)
