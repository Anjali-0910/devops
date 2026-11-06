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
sudo docker build -t p4 .
docker images
sudo docker run -d -p 5000:5000 --name p4-container p4
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
docker build -t p4-v2 .
docker stop p4-container
docker run -d -p 5000:5000 --name p4-container2 p4-v2
sleep 3
curl http://localhost:5000
```
Output: Updated with Docker!

## Clean up
```bash
docker stop p4-container2
docker rm p4-container p4-container2
```

## Clone this program from GitHub
```bash
git clone https://github.com/Anjali-0910/devops.git
cd devops/p4
sudo docker build -t p4 .
sudo docker run -d -p 5000:5000 --name p4-container p4
sleep 3
curl http://localhost:5000
```

## Quick fixes
- Port 5000 in use: docker ps, then docker stop <name>, or use -p 8080:5000
- Name already in use: docker rm -f <name>
- curl fails right after docker run: wait 3 seconds and retry
- Image can't download: needs internet, run docker pull python:3.9-slim beforehand
