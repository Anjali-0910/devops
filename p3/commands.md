# Program 3: Dockerized Python Flask Application

```bash
cd p3
# Build the Docker image
docker build -t my-flask-app .

# Run the container
docker run -p 5000:5000 my-flask-app
```
Open http://localhost:5000 in the browser.
Expected output: `Hello from a Dockerized Flask App!`
