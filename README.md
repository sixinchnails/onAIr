![Final 2IZON (1)](https://github.com/hyunnn12/onAIr/assets/119777617/5f716c20-2bf6-4df3-826e-1d76256b2119)


</br>

# 🎉 OnAIr

#### 별이 빛나는 밤에, 꿈꾸는 라디오, 푸른 밤, 두시의 데이트
##### 📻라디오를 들어보신적 있으신가요? 

###### 요즘에야 음악 들을 때 알고리즘을 통해 이노래 저노래를 자연스레 추천해주지만

###### 불과 십여년 전만 해도 라디오를 통해 음악을 추천받을 때가 꽤나 많았답니다.

##### 내 사연을 듣고 AI라디오가 추천해주는 음악을 많은 사람들과 공유해보세요!


###### OnAIr는 빅데이터 분산 처리 기반의 'AI 라디오' 프로젝트로 사용자가 '사연'과 '희망테마'를 입력하면 그에 맞는 대본과 음악 추천 결과를 생성하여 스트리밍 하는 서비스입니다.
</br>




# ⌛ 프로젝트 기간 : 2023. 08. 21 ~ 2023. 10. 06.




# 👥 팀 구성

<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/hyunnn12"><img src="https://avatars.githubusercontent.com/u/119777617?v=4" width="100px;" height="120px;" alt=""/><br /><sub><b>강현<br>Front-end<br/></b></sub></a></td>
    <td align="center"><a href="https://github.com/qkrrlgus114"><img src="https://avatars.githubusercontent.com/u/121294224?v=4" width="100px;" height="120px;" alt=""/><br /><sub><b>박기현<br> Back-end<br/></b></sub></a></td>
    <td align="center"><a href="https://github.com/yeonchaking"><img src="https://avatars.githubusercontent.com/u/99801068?v=4" width="100px;" height="120px;" alt=""/><br /><sub><b>연제경<br>PM/Full-Stack<br/></b></sub></a></td>
    <td align="center"><a href="https://github.com/Eungae-D"><img src="https://avatars.githubusercontent.com/u/135101171?v=4" width="100px;" height="120px;" alt=""/><br /><sub><b>최규호<br> Front-end<br/></b></sub></a></td>
    <td align="center"><a href="https://github.com/pum005"><img src="https://avatars.githubusercontent.com/u/108645121?v=4" width="100px;" height="120px;" alt=""/><br /><sub><b>최시환<br> Back-end<br/></b></sub></a></td>
    <td align="center"><a href="https://github.com/sixinchnails"><img src="https://avatars.githubusercontent.com/u/36617233?v=4" width="100px;" height="120px;" alt=""/><br /><sub><b>최재용<br> Data-Engineer<br/></b></sub></a></td>
</table>

</br>


</br>


# 📌 주요 기능


## 1. 온캐스트 생성 및 재생
- 사용자가 제목, 사연을 입력 후 음악의 테마와 DJ를 설정.
- 음악 추천 알고리즘을 통해 사연에 맞는 음악 3가지 추천 및 TTS 생성.
- AI DJ가 사연을 읽고 그에 따른 추천된 음악을 재생.

## 2. 음악 플레이 리스트
- 원하는 음악을 내 보관함의 저장 후 나만의 플레이 리스트 생성.

## 3. 음악 플레이어
- 플레이 리스트를 재생하면 음악 플레이어 실행.
- 페이지가 바뀌어도 음악 플레이어는 끊김없이 재생.(사용성 강화)

## 4. 라이브 서버
- 공유된 온캐스트를 특정 시간에 라이브 서버에서 재생.(하루 10개 제한)
- 사용자들은 온캐스트를 들으며 소통.
- 마음에 드는 음악은 내 보관함에 추가 가능.


# 🔗 주요 기술

## 1. AWS EC2 5대의 서버로 Spark 클러스터 구축
- NameNode 1대, Backup NameNode 1대, DataNode 3대
- YARN과 ZOOKEEPER는 구동 중인 NameNode 상 운영
- 800만 개의 노래 데이터를 HDFS에 적재하여 분산 병렬 처리
- 클러스터 실행, 종료, 재실행 스크립트 작성
</br>
![IMAGE_DESCRIPTION](./frontend/src/assets/demo1.png)

## 2. PCA와 K-평균 군집화를 활용한 음악 추천 기능
- 차원 축소법(PCA)으로 노래 데이터의 특성들의 다중공선성 제거 및 모델 성능 개선
- PySpark와 분산 병렬 처리를 이용한 800만 개의 노래 데이터를 K-평균 군집화
- 실루엣(Silhouette) 계수 기반으로 최적의 K 값 활용
- 사용자 입력 데이터가 속한 클러스터 내 중심점에 가까운 노래 목록 일부 추출
</br>
![IMAGE_DESCRIPTION](./frontend/src/assets/demo2.png)
![IMAGE_DESCRIPTION](./frontend/src/assets/demo3.png)

## 3. 사용자 사연 분석을 위해 BERT 기반의 트랜스포머 모델을 활용한 텍스트 감성 분석
- 추천 알고리즘에 필요한 Valence와 Energy를 얻기 위한 감성 분석 수행
- HuggingFace BERT 토크나이저 및 트랜스포머 모델(XLM-RoBERTa-large) 활용

## 4. 랜덤 포레스트로 음악 특성 값에 대한 특성 중요도를 도출하고 이를 코사인 유사도에 가중치로 적용하여 추천 결과 생성
- 앙상블 모델인 랜덤 포레스트(**sklearn.ensemble.RandomForestClassifier)**를 기반으로 각 노래 특성 별 중요도를 측정
- 전체 특성 중 일부를 제거하여 모델의 성능이 얼마나 변화하는가 기준으로 중요도 계산
- 특성 중요도는 클러스터마다 개별 측정
</br>
![IMAGE_DESCRIPTION](./frontend/src/assets/demo4.png)

## 5. 데이터 수집기 구현 및 HDFS, YARN, ZOOKEEPER 서버 환경 구축
- Spotify API를 이용하여 키워드(ex. KPOP, ROCK etc.) 별 플레이리스트에 등록된 노래들과 특성 값들을 수집하여 HDFS에 적재
- YARN, ZOOKEEPER를 NameNode 서버 상에서 구동 및 관리

## 6. Flask, Hive와 Zeppelin을 활용한 추천 결과 집계 및 시각화
- Flask REST API 서버를 구축하여 사용자에게 추천 결과 제공
- Hive와 Zeppelin를 연동하여 MapReduce 기반 집계 및 시각화 수행
- Hive 메타스토어 DB로 Derby DB 사용

## 7. kafka를 통한, 실시간 라이브 서버간 비동기 메시지 통신 구현
- 라이브에 참여한 사용자에게 실시간 라이브 정보를 제공하는 서버와 라이브 스케줄을 관리하는 서버 사이에 실시간성을 높이기 위해 효율적인 데이터 전달 기술이 필요했습니다.
- kafka 와 zookeeper를 활용해 클러스터를 구축하여, 비동기 메시지 통신을 구현하고 안정적인 라이브 기능을 제공할수 있었습니다.

## 8. 불필요한 데이터 전송을 막기 위한 Websocket 도입
- 실시간 채팅과 실시간 라이브 방송을 진행을 위해, 사용자들이 서로 데이터를 주고 받아야만 했습니다.
- HTTP Polling 방식 대신, WebSocket 방식을 도입해 불필요한 데이터 전송을 줄여, 서버 부하를 막고, 네트워크 대역폭을 줄일수 있었습니다.

# 🔨 개발 및 협업 환경


### Backend
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)&nbsp;<img src="https://img.shields.io/badge/Spring-green?style=flat-square&logo=spring&logoColor=white"/>
&nbsp;<img src="https://img.shields.io/badge/SpringBoot-green?style=flat-square&logo=springboot&logoColor=white"/>
&nbsp;<img src="https://img.shields.io/badge/MySql-4479A1?style=flat-square&logo=mysql&logoColor=white"/>
&nbsp;<img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white"/>
&nbsp;

### Frontend
<img src="https://img.shields.io/badge/React-skyblue?style=flat-square&logo=react&logoColor=white"/>
&nbsp;<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/>
&nbsp;<img src="https://img.shields.io/badge/HTML-red?style=flat-square&logo=html5&logoColor=white"/>
&nbsp;<img src="https://img.shields.io/badge/CSS-blue?style=flat-square&logo=css3&logoColor=white"/>
&nbsp;<img src="https://img.shields.io/badge/Node.js-green?style=flat-square&logo=nodedotjs&logoColor=white"/>

### Data
<img src="https://img.shields.io/badge/Python-blue?style=flat-square&logo=python&logoColor=white"/>
&nbsp;<img src="https://img.shields.io/badge/Kafka-black?style=flat-square&logo=apachekafka&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Spark-black?style=flat-square&logo=apachespark&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Hadoop-blue?style=flat-square&logo=apachehadoop&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Hive-yellow?style=flat-square&logo=apachehive&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Flask-black?style=flat-square&logo=flask&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Spotify-green?style=flat-square&logo=spotify&logoColor=white"/>



# 🖼 서비스 화면
### 온캐스트 생성을 위한 제목, 테마, 사연, DJ 선택
![Frame 112](https://github.com/hyunnn12/onAIr/assets/119777617/76b4d6ae-4b9c-4033-b138-5f60385fccce)


### 생성된 온캐스트의 라디오 컴포넌트
![개인 라디오 DJ페이지](https://github.com/hyunnn12/onAIr/assets/119777617/c9c8010a-6c8c-427d-88e6-a3d37a013aa7)


### 생성된 온캐스트의 음악 컴포넌트
![라디오 음악 페이지](https://github.com/hyunnn12/onAIr/assets/119777617/581807ab-c7fd-471f-af36-87229a5fd6fd)


### 저장된 온캐스트들 이 페이지에서 다시 재생 및 라이브로 공유 가능
![마이페이지 - 라디오](https://github.com/hyunnn12/onAIr/assets/119777617/53f09c63-6cdb-40e6-9ab7-71f81ef1feed)


### 음악 스트리밍까지 가능하여 원하는 플레이리스트들을 만들어 언제나 들을 수 있다.
![마이페이지-음악 보관함](https://github.com/hyunnn12/onAIr/assets/119777617/f4548a86-8856-4db7-b954-ea0e0bbb79b5)


### 음악 플레이어-플레이리스트들을 재생하는 페이지
![플레이어페이지](https://github.com/hyunnn12/onAIr/assets/119777617/babc6b9e-6e63-4efd-a350-f0057f8bc031)

### 라이브 페이지-공유된 온캐스트로 다 함께 실시간으로 감상 가능한 라디오
![라이브 라디오 DJ페이지](https://github.com/hyunnn12/onAIr/assets/119777617/e52ef205-e999-42df-86d6-c261f26a1e93)


### 라이브 페이지-공유된 온캐스트의 음악들을 실시간으로 다함께 감상 가능
![라이브 라디오 목록 페이지](https://github.com/hyunnn12/onAIr/assets/119777617/c7e975cc-76d5-4b90-8b2b-6c95e31c6f1a)


### 라이브 페이지-실시간으로 라이브 페이지에 있는 유저들끼리 소통 가능
![라이브 라디오 대화 페이지](https://github.com/hyunnn12/onAIr/assets/119777617/07687ac6-eaa0-4e4d-8509-2161b4dae186)


# 💬 시스템 아키텍처
![system_architecture](https://github.com/hyunnn12/CodingTestPractice/assets/119777617/d549215c-c5ca-40f0-beb5-c876e8655ad8)

# 💬 데이터 모델링(ERD)
![erd사진](https://github.com/hyunnn12/CodingTestPractice/assets/119777617/7f4b2ab3-cdef-4285-99c7-fa6534561007)

# 💬 화면 설계서(목업)
![피그마](https://github.com/hyunnn12/CodingTestPractice/assets/119777617/9d27af23-5b1e-4c47-ab88-a77debd5ee02)

# 💬 인터페이스 설계서(API명세서)
![명세서1](https://github.com/qkrrlgus114/qkrrlgus114/assets/121294224/99197d4b-3872-4554-bf65-4695b30e9352)
![명세서2](https://github.com/qkrrlgus114/qkrrlgus114/assets/121294224/4b6deddf-9f39-4577-a8c7-5bb362aa22f2)


