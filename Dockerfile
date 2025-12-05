FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml poetry.lock* ./
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --only main --no-root
COPY . .
ENV PORT=8080
ENV PYTHONPATH=/app/src
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "src.app:app"]