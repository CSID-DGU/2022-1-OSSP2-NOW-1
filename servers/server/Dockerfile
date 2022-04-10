FROM node:alpine

ARG ROOT=/home/node/app
ARG TARGET_FOLDER=dist
# 컴파일된 파일이 저장되는 폴더. 미리 만들고 권한을 준다

USER node 
# 유저 설정
RUN mkdir ${ROOT}
# 폴더 생성
RUN chown -R node:node ${ROOT}
# 폴더 주인 권한 node 유저에게
WORKDIR ${ROOT}
RUN mkdir ${TARGET_FOLDER}
RUN chown -R node:node ./${TARGET_FOLDER}
COPY ./package.json .

RUN npm install

COPY . .
RUN chown -R node:node ./dist
EXPOSE 3000
CMD ["npm", "run", "dev"]