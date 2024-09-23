FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /code

# 의존성 파일 복사 및 설치
COPY app/requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . /code

# 포트 개방
EXPOSE 8000

# 기본 명령어
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
