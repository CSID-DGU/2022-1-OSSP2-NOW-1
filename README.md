# 2022-1-OSSP2-NOW-1

## 시간표 테트리스, 시간표팡

### 팀원
 - 금소현 (팀장)
 - 김서희
 - 이민수
 - 이희준

### 프로젝트 소개
'망한 시간표 대회'에서 영감을 받아 각자 자신의 시간표로 테트리스 게임을 즐겨보고자 <시간표팡> 게임을 만들었습니다.
강의 하나하나가 조각이 되어 테트리스 게임을 즐길 수 있습니다.
<시간표팡>은 개인모드와 경쟁모드로 총 2가지의 모드를 지원합니다.

### 설치방법 및 실행가이드
 - <시간표팡>을 실행하기 위해서는 Selenium과 Webdriver를 설치해야 합니다.
 - 소스코드를 다운받고, cmd에서 다음 명령어를 실행하여 필수요소를 설치하고 게임을 실행할 수 있습니다.
```bash
pip install -r ./requirements.txt 
python Pang.py
```

### 개인모드
에브리타임의 시간표 정보를 바탕으로 개인의 시간표를 불러와서 게임을 즐길 수 있습니다.  
사용자의 에브리타임 아이디를 입력하면 자동으로 시간표를 테트리스 조각으로 변경해 줍니다.  
※ 현재 에브리타임은 로그인 시 captcha 입력을 요구합니다. 로그인 창이 등장하면 captcha를 실행한 후 콘솔 창에 아무 메시지나 입력하여 계속 진행하세요!

### 경쟁모드
모두 공통된 강의 정보를 바탕으로 게임을 진행하여 공정한 경쟁을 치를 수 있습니다.  
이 모드에서는 랭킹 서비스도 구현되어있습니다.  
~~현재는 동국대학교 컴퓨터공학과의 강의 정보를 기준으로 플레이할 수 있습니다.~~  
-> 현재 서버는 동작하지 않으므로 경쟁모드를 즐길 수 없습니다.

### 조작방법
![image](https://user-images.githubusercontent.com/45023828/174065938-bcaad803-d063-4a46-925d-177418e7cfa7.png)

### 주의점
현재 webdriver-manager을 통해 최신 웹 드라이버를 자동으로 설치하지 않습니다. 자신의 크롬 버전에 맞는 웹 드라이버를 직접 다운로드 받은 후 루트 폴더에 저장하세요.

### 서버
서버에 대해 궁금하시다면 [링크](https://github.com/CSID-DGU/2022-1-OSSP2-NOW-1/tree/server/servers)를 참고하세요.
