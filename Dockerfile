FROM python:3.11.7-alpine
WORKDIR /usr/src/woltapp
COPY . .
RUN pip install -r requirements.txt
# make sure that uvicorn uses the 0.0.0.0 address instead of
# the default localhost (127.0.0.1), since that doesn't work
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
