FROM python:3.10.12-alpine

COPY requirement.txt worker.py ./
RUN pip install --no-cache-dir -r requirement.txt

CMD ["python", "worker.py", "redis", "rng", "hasher"]