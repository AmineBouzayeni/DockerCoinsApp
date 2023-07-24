FROM python:3.10.12-alpine

COPY worker/requirement.txt ./
RUN pip install --no-cache-dir -r requirement.txt

COPY worker/worker.py ./

CMD ["python", "worker.py", "redis", "rng", "hasher"]