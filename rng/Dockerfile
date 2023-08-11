FROM python:3.10.12-alpine

COPY requirement.txt rng.py ./
RUN pip install --no-cache-dir -r requirement.txt

CMD ["python", "rng.py"]