FROM python:3.10-slim-buster as builder
EXPOSE 80
EXPOSE 443
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt .
COPY manage.py .
COPY /djangoInit ./djangoInit
COPY /adminFES ./adminFES
COPY /accounts ./accounts
COPY /templates ./templates
COPY /content ./content
RUN pip install --upgrade pip && pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt
FROM python:3.10-slim-buster
WORKDIR /app
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
COPY --from=builder /app/manage.py .
COPY --from=builder /app/djangoInit ./djangoInit
COPY --from=builder /app/adminFES ./adminFES
COPY --from=builder /app/accounts ./accounts
COPY --from=builder /app/templates ./templates
COPY --from=builder /app/content ./content
RUN pip install --no-cache /wheels/* && python manage.py collectstatic --noinput