FROM python:3.9
COPY CTS.py /app/CTS.py
RUN pip install flask requests urllib3
WORKDIR /app
CMD ["python", "CTS.py"]
