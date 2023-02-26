# Week 1 — App Containerization

- build dockerfile
- I have used docker before. I got more information about docker this time. Best part i liked is the diff between RUN and CMD

Challenges:
Unable to push to dockerhub directly. had to add tag manually to match with dockerhub to be able to push


### HOMEWORK DONE:
deployed the backend image to dockerhub https://hub.docker.com/r/mdsadiq/experiments/tags  [dockerhub-image](./assets/week-1-local.PNG)

Ran a docker instance locally [run docker locally](./assets/week-1.PNG)

converted backend flask to multi stage pipeline [multi stage pipeline](./assets/week-1-multi-stage.JPG)

install and run docker conatiner in ec2 [docker running in ec2, aws shell](./assets/week-1-ec2-docker.JPG)

implemented healthcheck on frontend 

Read best practices and implemented them, for ex. multi stage, layers for installing library, using non root user etc
