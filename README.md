# redis-rdb-merger
redis 의 rdb 파일을 하나로 합쳐주는 툴입니다. 찾아보니 없어서 그냥 만들었습니다.

# 요구사항
* python 2.7+
* rdb 파일들

# 사용법 
기본적인 사용법은 다음과 같습니다.
```bash
$ python merger.py [-h] [--out OUT_FILE] rdbs [rdbs ...]
```

## rdb 파일들을 가져오기
합치고자 하는 rdb 파일들을 받아옵니다.

## rdb 파일 합치기
해당 유틸리티를 이용해서 rdb 파일들을 하나로 합칩니다.

## redis 에 로드하기
redis 서버의 dump.rdb 파일을 결과 파일로 교체한 후 서버를 재기동합니다.
이때, 재기동 하고자 하는 서버의 redis.conf 에서 rdbchecksum 값을 no 로 설정해야 합니다.

rdbchecksum 을 yes 로 하고자 할 경우엔, 먼저 rdbchecksum 을 no 로 해서 로드한 후에,
bgsave 를 한 번 수행하고 rdbchecksum 을 yes 로 설정한 후 redis 를 재시작하면 됩니다.

# 제한
해당 유틸리티는 하나의 redis 서버에 하나의 db 만 있다고 가정하고 작성된 유틸리티입니다.
하나의 redis 서버에 여러 db 를 두는 환경의 rdb 파일을 하나로 합치는 것은 지원하지 않고 있습니다.

# 참고
* [RDB file format](https://github.com/sripathikrishnan/redis-rdb-tools/wiki/Redis-RDB-Dump-File-Format)
