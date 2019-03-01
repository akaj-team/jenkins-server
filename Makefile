JENKINS_IMAGE_NAME=at/jenkins

server-start: jenkins-image-build portainer-container-start

portainer-container-start:
	@echo ":::Starting portainer"
	docker stack deploy --compose-file portainer_compose.yml portainer
	docker network create --driver overlay public_net

jenkins-image-build: 
	@echo ":::Building jenkins image"
	docker build --rm -f docker-jenkins/Dockerfile -t $(JENKINS_IMAGE_NAME) docker-jenkins