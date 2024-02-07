![IMAGE_DESCRIPTION](./frontend/src/assets/zizon.png)

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
- YARN과 ZOOKEEPER로 리소스 관리 및 HA 제공
- 쉘 스크립트로 클러스터 시작, 재시작, 중단
</br>
![IMAGE_DESCRIPTION](./frontend/src/assets/demo1.png)

## 2. Random Forest 및 K-평균 군집화 기반 음악 추천 기능
- 800만 개의 노래 데이터를 PySpark와 Cluster로 K-평균 군집화
- Silhouette 계수 기반 최적의 K 값 선정
- Random Forest로 노래 특성 별 중요도를 도출하고 코사인 유사도의 가중치로 적용
- 사용자 입력 데이터가 속한 클러스터 내 중심점에 가까운 노래 목록 일부 추출
</br>
![IMAGE_DESCRIPTION](./frontend/src/assets/demo2.png)
![IMAGE_DESCRIPTION](./frontend/src/assets/demo3.png)

## 3. 사용자 사연 분석을 위해 BERT 기반의 트랜스포머 모델을 활용한 텍스트 감성 분석
- 추천 알고리즘에 필요한 Valence와 Energy를 얻기 위한 감성 분석
- HuggingFace BERT Tokenizer 및 XLM-RoBERTa-large 모델 활용
</br>
![IMAGE_DESCRIPTION](./frontend/src/assets/demo4.png)

## 5. Spotify API로 키워드 별 playlist에 등록된 노래 데이터 수집

## 6. Flask, Hive와 Zeppelin을 활용한 추천 결과 집계 및 시각화
- Flask REST API 서버로 사용자에게 추천 결과 제공
- Hive와 Zeppelin으로 MapReduce 기반 집계 및 시각화 수행

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
![IMAGE_DESCRIPTION](./frontend/src/assets/Frame 112.png)

### 생성된 온캐스트의 라디오 컴포넌트
![IMAGE_DESCRIPTION](./frontend/src/assets/radio.png)

### 생성된 온캐스트의 음악 컴포넌트
![IMAGE_DESCRIPTION](./frontend/src/assets/music.png)

### 저장된 온캐스트들 이 페이지에서 다시 재생 및 라이브로 공유 가능
![IMAGE_DESCRIPTION](./frontend/src/assets/mypageRadio.png)

### 음악 스트리밍까지 가능하여 원하는 플레이리스트들을 만들어 언제나 들을 수 있다.
![IMAGE_DESCRIPTION](./frontend/src/assets/mypageMusic.png)

### 음악 플레이어-플레이리스트들을 재생하는 페이지
![IMAGE_DESCRIPTION](./frontend/src/assets/플레이어페이지.png)


### 라이브 페이지-공유된 온캐스트로 다 함께 실시간으로 감상 가능한 라디오
![IMAGE_DESCRIPTION](./frontend/src/assets/liveRadio.png)

### 라이브 페이지-공유된 온캐스트의 음악들을 실시간으로 다함께 감상 가능
![IMAGE_DESCRIPTION](./frontend/src/assets/liveList.png)

### 라이브 페이지-실시간으로 라이브 페이지에 있는 유저들끼리 소통 가능
![IMAGE_DESCRIPTION](./frontend/src/assets/liveChat.png)

# 💬 시스템 아키텍처
![system_architecture](https://github.com/hyunnn12/CodingTestPractice/assets/119777617/d549215c-c5ca-40f0-beb5-c876e8655ad8)

# 💬 데이터 모델링(ERD)
![erd사진](https://github.com/hyunnn12/CodingTestPractice/assets/119777617/7f4b2ab3-cdef-4285-99c7-fa6534561007)

# 💬 화면 설계서(목업)
![피그마](https://github.com/hyunnn12/CodingTestPractice/assets/119777617/9d27af23-5b1e-4c47-ab88-a77debd5ee02)

# 💬 인터페이스 설계서(API명세서)
![명세서1](https://github.com/qkrrlgus114/qkrrlgus114/assets/121294224/99197d4b-3872-4554-bf65-4695b30e9352)
![명세서2](https://github.com/qkrrlgus114/qkrrlgus114/assets/121294224/4b6deddf-9f39-4577-a8c7-5bb362aa22f2)


