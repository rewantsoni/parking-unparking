FROM python:3-onbuild
#9999 - server
WORKDIR "/app"
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY . .
CMD ["python", "./maganer.py db init"]
CMD ["python", "./maganer.py db migrate"]
CMD ["python", "./maganer.py db upgrade"]
EXPOSE 9999 9092
CMD ["python", "./NotifyUser.py"]