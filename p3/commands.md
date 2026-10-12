# Program 3: Dockerized Flask application

```bash
cd p3
docker build -t program-3 .
docker images
docker run -d -p 5000:5000 --name flask-app program-3
docker ps
curl http://localhost:5000
curl http://localhost:5000/about
docker logs flask-app
docker stop flask-app
docker rm flask-app
```
Expected output: `Hello from a Dockerized Flask application!`
