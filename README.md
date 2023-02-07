<img src = "https://user-images.githubusercontent.com/110344274/208290139-2695913f-c216-4dee-835a-d063aa09fe9b.png" width="500" height="160">

# Not Deafferent - 이세계 개발자 
### 작품 개요
- 본 개발 작품은 청각장애인과 비장애인이 함께 이용하는 서비스를 제공한다. 각각 한 대의 Raspberry Pi와 기기에 연결된 웹캠을 통하여 소통할 수 있다.
- Raspberry Pi에 연결된 웹캠을 통해 청각장애인의 수어를 촬영하고, 영상 데이터를 webRTC 서버를 통해 실시간으로 연산 컴퓨터로 전송한다.
- 연산 컴퓨터에서는 학습된 모델을 통하여 청각장애인의 수어를 추론하고, 문장으로 만들어 firebase에 전송한다.
- firebase에 저장된 문장 정보를 WebOS의 Web App에서 받아와 출력한다. 
### 파일 구성도

### 개발 환경
1. Webapp 
- 언어: JavaScript
- 라이브러리: React 
- 프레임워크: Enact 
- Tool: VSCode 
- Database: firebase/firestore 

2. Deep learning Model
- 언어 : Python
- 사융 툴 : Anaconda
- 라이브러리 : OpenCV, numpy, is, mediapipe, sklearn, tensorflow 

3. 서버
- 언어 : JavaScript
- 개발 환경 : Nodejs
- 라이브러리 : PeerJs, socket.io
- 프레임워크 : Express.js
- Tool : VSCode>
- 배포 : Heroku 

### 팀 명단
|이름|이메일|역할|
|----|----|----|
|이규열|dlrbduf1346@naver.com|총괄|
|박성우|psw209@chungbuk.ac.kr|webRTC 서버 구축|
|김태현|xogus5070318@gmail.com|Web App 개발|
|심민경|alals123426@gmail.com|수어 인식 연구|
|이동헌|ldh97654@icloud.com|수어 인식 연구|
