#!/bin/bash
# 도커 파일 푸시에 사용된다.

docker build -t blaxsior/ossp-my_server -f ./server/Dockerfile ./server
docker build -t blaxsior/ossp-nginx -f ./nginx/Dockerfile.dev ./nginx

docker push blaxsior/ossp-my_server
docker push blaxsior/ossp-nginx