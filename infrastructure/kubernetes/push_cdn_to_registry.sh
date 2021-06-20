#!/bin/bash

aws ecr-public get-login-password --region $REGION | docker login --username AWS --password-stdin public.ecr.aws

DOCKER_REGISTRY=public.ecr.aws/$YOUR_REGISTRY_ALIAS
TAG=v1

docker tag cdn-ops-db $DOCKER_REGISTRY/cdn-ops-db:$TAG
docker push $DOCKER_REGISTRY/cdn-ops-db:$TAG
docker tag cdn-enroller $DOCKER_REGISTRY/cdn-enroller:$TAG
docker push $DOCKER_REGISTRY/cdn-enroller:$TAG
docker tag enroll-helper $DOCKER_REGISTRY/cdn-enroll-helper:$TAG
docker push $DOCKER_REGISTRY/cdn-enroll-helper:$TAG
docker tag cdn-static $DOCKER_REGISTRY/cdn-static:$TAG
docker push $DOCKER_REGISTRY/cdn-static:$TAG
docker tag cdn-ops $DOCKER_REGISTRY/cdn-ops:$TAG
docker push $DOCKER_REGISTRY/cdn-ops:$TAG
docker tag cdn-smtp $DOCKER_REGISTRY/cdn-smtp:$TAG
docker push $DOCKER_REGISTRY/cdn-smtp:$TAG
docker tag cdn-stats $DOCKER_REGISTRY/cdn-stats:$TAG
docker push $DOCKER_REGISTRY/cdn-stats:$TAG
docker tag cdn-router $DOCKER_REGISTRY/cdn-router:$TAG
docker push $DOCKER_REGISTRY/cdn-router:$TAG
docker tag cdn-monitor $DOCKER_REGISTRY/cdn-monitor:$TAG
docker push $DOCKER_REGISTRY/cdn-monitor:$TAG
docker tag cdn-exp-server $DOCKER_REGISTRY/app-server:$TAG
docker push $DOCKER_REGISTRY/app-server:$TAG
docker tag cdn-vault $DOCKER_REGISTRY/cdn-vault:$TAG
docker push $DOCKER_REGISTRY/cdn-vault:$TAG
docker tag cdn-stats-db $DOCKER_REGISTRY/cdn-stats-db:$TAG
docker push $DOCKER_REGISTRY/cdn-stats-db:$TAG
docker tag cdn-edge $DOCKER_REGISTRY/cdn-edge:$TAG
docker push $DOCKER_REGISTRY/cdn-edge:$TAG
docker tag cdn-mid $DOCKER_REGISTRY/cdn-mid:$TAG
docker push $DOCKER_REGISTRY/cdn-mid:$TAG

