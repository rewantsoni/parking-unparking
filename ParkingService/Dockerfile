FROM python:3-onbuild
#5000 - check user
#8888 -  server
#i dont think i need to expose 5432
#8082 - client for parking_copy
WORKDIR "/app"
COPY requirements.txt .
RUN pip install --upgrade pip && \
COPY . .
EXPOSE 8082 8888 5000 9092 5432
CMD ["python", "./app.py"]