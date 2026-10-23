# Program 4: Integrate Git with Docker

## Setup
```bash
mkdir p4
cd p4
git config --global user.name "Anjali-0910"
git config --global user.email "tech.anjalikri2@gmail.com"
```
Create app.py, requirements.txt and Dockerfile (nano app.py, nano requirements.txt, nano Dockerfile).

## Version 1
```bash
git init
git add .
git status
git commit -m "Initial Commit of Flask App"
sudo docker build -t pg4app .
docker images
sudo docker run -d -p 5000:5000 --name pg-4container pg4app
sudo docker ps
sleep 3
curl http://localhost:5000
```
Output: Hello from Git and Docker!

## Version 2
Change the return line in app.py to "Updated with Docker!", save, then:
```bash
git status
git diff
git add app.py
git commit -m "Update flask app message"
git log --oneline
docker build -t pg-4app2 .
docker stop pg-4container
docker run -d -p 5000:5000 --name pg-4container2 pg-4app2
sleep 3
curl http://localhost:5000
```
Output: Updated with Docker!

## Clean up
```bash
docker stop pg-4container2
docker rm pg-4container pg-4container2
```

## Clone this program from GitHub
```bash
git clone https://github.com/Anjali-0910/devops.git
cd devops/p4
sudo docker build -t pg4app .
sudo docker run -d -p 5000:5000 --name pg-4container pg4app
sleep 3
curl http://localhost:5000
```

## Quick fixes
- Port 5000 in use: docker ps, then docker stop <name>, or use -p 8080:5000
- Name already in use: docker rm -f <name>
- curl fails right after docker run: wait 3 seconds and retry
- Image can't download: needs internet, run docker pull python:3.9-slim beforehand
