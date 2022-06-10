# server

## 사용 방법
- 개발 중 :  
```docker compose -f docker-compose.dev.yml up --build```

- 개발 중 도커 허브에 푸시 :  
```./docker-push.sh```  
blaxsior은 현재 서버 개발자의 계정이므로, 자신의 docker hub 계정으로 이름을 변경해 사용하세요.  
- 서버용(EC2 등) :   
```docker compose up```  
서버용 코드에서는 docker-push 파일을 이용하여 자신의 docker hub 계정에 대해 푸시한 이미지를 기반으로 컨테이너를 생성합니다.  
개발 환경에서 도커 허브에 이미지를 푸시하고 서버 환경에 docker-compose.yml 파일을 이동시킨 후 (내부 이름 수정 필수), 명령을 수행하세요.

## 설명
 현재 브랜치는 시간표 테트리스에 대한 서버 관련 코드를 담고 있습니다.  
 서버는 docker 기반으로 동작하며, 외부에서 전달되는 요청은 nginx 서버의 리버시 프록시를 통해 express 서버로 전달되도록 구현되어 있습니다.  
 현재 서버에서는 데이터를 삽입하기 위한 API을 제공하지 않으므로, 새로 생성한 서버 상에 데이터를 삽입하고 싶은 경우 다음 과정을 수행합니다.  
 1. ```docker compose up``` : 서버를 실행합니다.
 2. ```docker exec -it [express서버_id] sh``` : 쉘 환경을 실행합니다.
 3. ```npm run insert1```: insert1 ~ insert4를 실행하여 json 형태의 데이터를 삽입합니다.  

npm run insert1 ~ insert4 을 통해 삽입되는 데이터는 동국대학교 2021년 2학기 및 2022학년 1학기 컴퓨터공학과 시간표 정보를 25개 강의 정도로 4분할 한 것입니다. 정보 자체를 변화하고 싶으시다면 server/data 폴더의 json 내용 및 insert_index.ts 내용을 바꿔보세요.

## API 포맷

1. 성공 : 요청한 포맷에 대한 json
2. 실패 : { message : string|string[] }  

- ```/api/tetro``` : 특정 테트로미노를 요청하거나, 테트로미노에 대한 점수 반환
    - ```/get-tetro/:tid``` : 특정 테트로미노 풀을 요청
    - ```/get-scores/:tid``` : 특정 테트로미노 풀에 대한 유저 정보 요청
    - ```/set-score/:tid``` : 특정 테트로미노 풀에 대한 유저 점수 등록
- ```/api/info``` : 대학 / 테트로미노 풀 정보 반환 ( 대학이나 테트로미노 풀 선택할 때 사용 )
    - ```/univs``` : 저장된 대학 목록 반환
    - ```/:tid/tetro-pools``` : 해당 대학에 대해 사용 가능한 테트로미노 풀 반환