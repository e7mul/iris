.PHONY: docker-build docker-shell

SHELL= /bin/sh

PROJECT_NAME=worldmodel_d
USER_NAME=wmasarczyk
UID=$(shell id -u)
PASSWD=test
PORT=53017
IMAGE_NAME=$(USER_NAME)_$(PROJECT_NAME)
CONTAINER_NAME=$(IMAGE_NAME)_default


docker-build:
	docker build \
		--build-arg USER_NAME=$(USER_NAME) \
                --build-arg PASSWD=$(PASSWD) \
		--build-arg UID=$(UID) \
		-t $(IMAGE_NAME) .


docker-shell:
	docker run --gpus all --rm -ti \
		-v $(PWD)/..:/home/$(USER_NAME)/project/ \
		-v /data/wmasarcz/$(PROJECT_NAME):/home/$(USER_NAME)/project/results/ \
		-v /data/SHARE/datasets/:/home/$(USER_NAME)/project/data/ \
		--shm-size=64gb \
		-d \
		-p $(PORT):22 \
		--name=$(CONTAINER_NAME) \
		$(IMAGE_NAME)

docker-build_minimal:
	docker build \
		-f minimal_Dockerfile \
                -t $(IMAGE_NAME)_execution .


docker-shell_execution:
        docker run --gpus all --rm -ti \
                -v $(PWD):/home/$(USER_NAME)/project/ \
                --name=$(IMAGE_NAME)_execution \
                $(IMAGE_NAME)_execution
