FROM python:3-onbuild
WORKDIR "/app"
COPY requirements.txt .
RUN pip install --upgrade pip
COPY . .
EXPOSE 30100
CMD ["python", "./app.py"]