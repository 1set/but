.PHONY: default

DOCKER=docker

DOCKER_IMG_NAME=but
APP_VERSION=0.0.4

COMMIT_ID=$(shell git rev-parse --short HEAD)
BUILD_DATE=$(shell date '+%Y%m%d')
DOCKER_REGISTRY=1set
DOCKER_IMG_VERSION=$(APP_VERSION)-$(COMMIT_ID)-$(BUILD_DATE)
DOCKER_IMG_FULL_NAME_PREFIX=$(DOCKER_REGISTRY)/$(DOCKER_IMG_NAME):$(DOCKER_IMG_VERSION)
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
test:
	$(DOCKER) run --rm --name "$(DOCKER_IMG_NAME)_test" -v $$PWD/list_version.sh:/test.sh $(DOCKER_IMG_NAME) /test.sh | python3 script/check_versions.py
run:
	$(DOCKER) run --rm -it --name "$(DOCKER_IMG_NAME)_app" $(DOCKER_IMG_NAME)
runprod:
	$(DOCKER) run --rm -it --name "$(DOCKER_IMG_NAME)_prod_app" $(DOCKER_IMG_FULL_NAME_LATEST)
tag:
	$(eval VERSION_TAG=$(shell $(DOCKER) run --rm --name "$(DOCKER_IMG_NAME)_test" -v $$PWD/list_version.sh:/test.sh $(DOCKER_IMG_NAME) /test.sh | python3 script/get_tagname.py))
	$(eval DOCKER_IMG_FULL_NAME=$(DOCKER_IMG_FULL_NAME_PREFIX)-$(VERSION_TAG))
	$(DOCKER) tag $(DOCKER_IMG_NAME) $(DOCKER_IMG_FULL_NAME)
	$(DOCKER) tag $(DOCKER_IMG_NAME) $(DOCKER_IMG_FULL_NAME_LATEST)
push: tag
	$(DOCKER) push $(DOCKER_IMG_FULL_NAME)
	$(DOCKER) push $(DOCKER_IMG_FULL_NAME_LATEST)
