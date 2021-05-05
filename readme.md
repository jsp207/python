
# 로컬

## 도커빌드

    docker build --tag jay-python:dev .

## 도커 실행

    실행 : docker-compose up -d

    중지 : docker-compose down


localhost:9999 실행이 잘되면 아래 원격명령을 통해, 빌드한후 Push한다.

# 원격

## 도커 로긴

도커로긴은 한번만하면 유지됨

docker login -u psmon -p XXXXXXXXX

docker logout

## 도커 재빌드및/푸시

docker build --tag psmon/jay-python:dev .

docker push psmon/jay-python:dev


## 업데이트

푸시가 완료되면  http://docker.webnori.com/
랜처에서 jay-python - web을 업그레이드한다. tag가 dev로 고정이기때문에 이때
Always pull image before create를 선택해서 업그레이드한다.


이 저장소는 다음 url에 연결되어 있다.

http://amadeus.webnori.com/










