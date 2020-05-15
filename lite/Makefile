.PHONY: default

DOCKER=docker

DOCKER_IMG_NAME=butlite
APP_VERSION=0.0.5

COMMIT_ID=$(shell git rev-parse --short HEAD)
BUILD_DATE=$(shell date '+%Y%m%d')
DOCKER_REGISTRY=1set
DOCKER_IMG_VERSION=$(APP_VERSION)-$(COMMIT_ID)-$(BUILD_DATE)
DOCKER_IMG_FULL_NAME_TAG=$(DOCKER_REGISTRY)/$(DOCKER_IMG_NAME):$(DOCKER_IMG_VERSION)
DOCKER_IMG_FULL_NAME_LATEST=$(DOCKER_REGISTRY)/$(DOCKER_IMG_NAME):latest

default:
	@echo "build target is required"
	@exit 2
build:
	$(DOCKER) build -t $(DOCKER_IMG_NAME) .
buildnew:
	$(DOCKER) build --pull --no-cache -t $(DOCKER_IMG_NAME) .
buildci: build
	$(DOCKER) tag $(DOCKER_IMG_NAME) $(DOCKER_IMG_FULL_NAME_LATEST)
clean:
	$(DOCKER) rmi -f $(DOCKER_IMG_NAME)
inspect:
	docker images | grep $(DOCKER_IMG_NAME)
	$(DOCKER) history $(DOCKER_IMG_NAME)
run:
	$(DOCKER) run --rm -it --name "$(DOCKER_IMG_NAME)_app" $(DOCKER_IMG_NAME)
runprod:
	$(DOCKER) run --rm -it --name "$(DOCKER_IMG_NAME)_prod_app" $(DOCKER_IMG_FULL_NAME_LATEST)
tag:
	$(DOCKER) tag $(DOCKER_IMG_NAME) $(DOCKER_IMG_FULL_NAME_TAG)
	$(DOCKER) tag $(DOCKER_IMG_NAME) $(DOCKER_IMG_FULL_NAME_LATEST)
push: tag
	$(DOCKER) push $(DOCKER_IMG_FULL_NAME_TAG)
	$(DOCKER) push $(DOCKER_IMG_FULL_NAME_LATEST)
