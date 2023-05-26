FROM python:3.9
COPY CTS.py /app/CTS.py
RUN pip install flask requests
WORKDIR /app
CMD ["python", "CTS.py"]