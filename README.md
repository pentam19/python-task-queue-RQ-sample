### Python Task Queue RQ Sample
RedisとWorker起動
$ docker-compose up --scale worker=4

タスク実行
$ docker-compose run --rm worker python app.py
