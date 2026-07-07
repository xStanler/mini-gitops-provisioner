FROM demisto/fastapi:0.125.0.10158186

ARG APP_VERSION=1.0.0
ARG COMMIT_SHA=unknown

ENV APP_VERSION=${APP_VERSION}
ENV COMMIT_SHA=${COMMIT_SHA}
ENV ENVIRONMENT=deploy
ENV HOSTNAME=alma-linux

WORKDIR /app

RUN pip install uv

COPY . .

RUN uv sync

CMD ["uv", "run", "uvicorn", "app/main:app"]
