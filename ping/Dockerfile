FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN pip install flask requests
ENTRYPOINT ["python3"]
CMD ["ping.py"]
