# 포트폴리오 요구사항
아래의 내용은 포트폴리오 요구사항에 대해 작성한 내용입니다. 포트폴리오 요구사항 기한은 `2024.08.23`까지 제출해야 하며, 제출방법은 별도의 채널에서 공유할 예정입니다.

## 요구사항
portfolio 브랜치의 `models/users/models.py` 파일에는 필요 이상의 유저 데이터를 수집하도록 DB 모델링이 돼 있습니다.
해당 모델을 통해 고객의 정보를 수집하고, 조회할 수 있도록 돼 있는데 아래의 요구사항을 만족할 수 있도록 models.py 혹은 serializers.py, viewsets.py 등을 수정하도록 합니다.

1. 전당포 서비스를 목적으로 고객의 정보를 수집하며, 필수적인 정보는 다음과 같으며 이외의 정보는 선택사항 
   1. 이름, 성별, CI정보, 생년월일, 이메일 
2. 고객 정보 생성/조회 API 개발 
   1. 고객 정보 생성 API에서 받을 필수 정보는 1.i에 쓰여진 필드와 같음
   2. 고객 정보 조회 API에서 조회할 수 있는 정보는 다음과 같음 
      1. id, name, email, is_active
3. 위의 필수 정보를 제외하고 선택사항 중 불필요한 모델에 대해 어떻게 처리할지 다음 항목 중에서 선택
   1. models.py 에서 삭제 -> migration 코드 필요
   2. viewsets.py 에서 조치 
   3. serializers.py 에서 조치 
   4. 이외의 다른 방법으로 조치

## 결과제출
전당포 서비스를 위한 API 개발을 완료하여 코드를 제출하며, 코드 제출 과정에서 리포트 파일을 함께 제출해야 합니다.

1. API를 개발한 코드는 반드시 동작여부를 확인하여야 함
2. 리포트 제출 시 다음과 같은 내용이 포함되어야 함
   * 서비스 개발 관점에서 API를 개발할 때 개인정보/고유식별정보 등을 어떻게 수집/처리할지 고민한 내용
   * 불필요한 정보를 어떻게 처리하였는지 설명(처리 내용 요약)
   * 불필요한 정보를 처리하는 방법을 선택한 이유에 대해 서술(자세히)
