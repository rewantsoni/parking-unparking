FROM python:3-onbuild
WORKDIR "/app"
COPY requirements.txt .
RUN pip install --upgrade pip
COPY . .
EXPOSE 31743 5432
RUN chmod +x manager.py
RUN chmod +x /app/docker-entrypoint.sh
CMD ["/bin/bash", "/app/docker-entrypoint.sh"]
