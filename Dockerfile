FROM python:slim
ENV PYTHONDONTWRITEBYTECODE=1 
COPY app app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]