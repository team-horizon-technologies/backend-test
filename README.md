## Horizon Technologies

# 백엔드 과제

- 주어진 모델을 조회하는 api 만들기

## 요구사항

- Django Rest Framework로 작성해주세요.
- 제공되는 testboard app에 구현해주세요.
- 외부 라이브러리도 필요하다면 사용해주셔도 좋습니다.
- 폴더 구조또한 자유롭게 구성해주셔도 좋습니다.
- db는 제공해드린 sqlite로 구현해주세요.

## 주요 구현

### Post 모델 리스트 조회

- url -> GET: /posts/
- 리턴 받아야 할 데이터
  - post id
  - post title
  - post writer -> username
  - post created_at
  - post와 연결된 comment의 갯수
- 예시

```
[
    {
        "id": 1,
        "title": "테스트",
        "created_at": "2022-04-21T06:20:45.166385Z",
        "writer": "user1",
        "comments_count": 4
    },
    ...
]
```

### Post 모델 상세데이터

- url -> GET: /posts/<int: post_id>
- 리턴 받아야 할 데이터
  - post id
  - post title
  - post content
  - post created_at
  - post writer -> username
  - post -> comment -> content
  - post -> comment -> writer -> username
  - post -> comment -> created_at
- 예시

```
{
    "id": 1,
    "title": "테스트 글 1",
    "content": "테스트",
    "writer": "user1",
    "created_at": "2022-04-21T06:20:45.166385Z",
    "comments": [
        {
            "content": "테스트 글1에 적힌 댓글1",
            "writer": "user2",
            "created_at": "2022-04-21T06:24:06.013729Z"
        },
        ...
    ]
}
```

## 주의사항

- 모든 기능이 완벽하지 않아도 좋습니다. 할 수 있는 만큼만 작성해주세요.
- Post나 Comment에 데이터를 추가하셔도 좋습니다.
- SECRET_KEY는 `django-insecure-x$&atszjdy0c1@x=k!j%6!a!cmv&7hrd6dp=)79-r_xi%$stcr` 입니다

## 제출방법

- 과제 repository를 fork해주세요.
- 모든 코드의 변경과정을 잘 정리해서 commit해주세요.
  - commit 메세지도 잘 작성해주세요.
- 코드에 대해 간단한 설명을 README.md 파일에 정리해주세요.(기존에 있는 README.md 파일은 삭제해주세요)
- 시간 내에 마무리 해주시고 해당 repository 주소를 보내주세요!
