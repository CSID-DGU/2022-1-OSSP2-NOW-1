# server

## 사용 방법
개발 중
```docker compose -f docker-compose.dev.yml up --build```

개발 중 도커 허브에 푸시
```./docker-push.sh```

서버 : 
```docker compose up```

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