![Thumbnail](https://github.com/hyunnn12/onAIr/assets/119777617/b57c97bb-886b-44d6-a100-1d5058036fd0)

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

- AWS EC2 5대의 서버로 Spark 클러스터 구축
- NameNode 1대, Backup NameNode 1대, DataNode 3대
- YARN과 ZOOKEEPER는 구동 중인 NameNode 상 운영
- 800만 개의 노래 데이터를 HDFS에 적재하여 분산 병렬 처리
- 클러스터 실행, 종료, 재실행 스크립트 작성
![IMAGE_DESCRIPTION](https://file.notion.so/f/f/93f6a052-c8ca-4250-8609-aadf4d306770/53b4ea7c-3a5b-47a5-9dd2-2d712286b4d0/Untitled.png?id=bab91b59-07cd-46a1-babf-c2eb4b9dcd96&table=block&spaceId=93f6a052-c8ca-4250-8609-aadf4d306770&expirationTimestamp=1701597600000&signature=pmFZ0pEwiFZ3-0E9yQ2WeWasMvajgH6Bxy3kDdTdWf4&downloadName=Untitled.png)


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
## 추후 모여서 작성 예정

### gif1 메인화면 - 사연 테마 입력- 온캐스트 생성 완료까지

### gif2 마이페이지 - 온캐스트 재생 - 스크립트, 음악 재생까지

### gif3 마이페이지 - 음악 플레이리스트에 추가 - 플레이어로 재생 - 백그라운드 재생까지(메인화면으로)

### gif4 라이브 페이지 - 편성표 - 채팅


# 💬 시스템 아키텍처
![system_architecture](https://github.com/hyunnn12/CodingTestPractice/assets/119777617/d549215c-c5ca-40f0-beb5-c876e8655ad8)

# 💬 데이터 모델링(ERD)
![erd사진](https://github.com/hyunnn12/CodingTestPractice/assets/119777617/7f4b2ab3-cdef-4285-99c7-fa6534561007)

# 💬 화면 설계서(목업)
![피그마](https://github.com/hyunnn12/CodingTestPractice/assets/119777617/9d27af23-5b1e-4c47-ab88-a77debd5ee02)

# 💬 인터페이스 설계서(API명세서)
![명세서1](https://github.com/qkrrlgus114/qkrrlgus114/assets/121294224/99197d4b-3872-4554-bf65-4695b30e9352)
![명세서2](https://github.com/qkrrlgus114/qkrrlgus114/assets/121294224/4b6deddf-9f39-4577-a8c7-5bb362aa22f2)


