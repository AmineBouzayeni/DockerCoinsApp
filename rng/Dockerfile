FROM python:3.10.12-alpine

COPY rng/requirement.txt ./
RUN pip install --no-cache-dir -r requirement.txt

COPY rng/rng.py ./

CMD ["python", "rng.py"]