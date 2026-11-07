# CA-M-356@18
FROM node:22.20.0-bookworm-slim AS codex
ARG CODEX_VERSION=0.156.1
RUN npm install --global @openai/codex@${CODEX_VERSION}

FROM node:22.20.0-bookworm-slim AS workbench_frontend
WORKDIR /frontend
COPY LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_FRONTEND/package.json \
     LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_FRONTEND/package-lock.json ./
RUN npm ci
COPY LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_FRONTEND ./
RUN npm run build

FROM python:3.14.7-slim@sha256:51dafde81dbdb6ebde285137a295cf18a47ca95234fe388a343719cb97305b3d
ARG RUNTIME_UID=1000
ARG RUNTIME_GID=1000
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates \
    && git config --system --add safe.directory /project \
    && rm -rf /var/lib/apt/lists/* \
    && (getent group ${RUNTIME_GID} || groupadd -g ${RUNTIME_GID} caprmedio) \
    && useradd -u ${RUNTIME_UID} -g ${RUNTIME_GID} -m -d /home/caprmedio caprmedio
RUN python -m pip install --no-cache-dir uv==0.12.18
COPY --from=codex /usr/local/bin/node /usr/local/bin/node
COPY --from=codex /usr/local/lib/node_modules /usr/local/lib/node_modules
RUN ln -s /usr/local/lib/node_modules/@openai/codex/bin/codex.js /usr/local/bin/codex
WORKDIR /workspace
COPY pyproject.toml uv.lock ./
ENV UV_PROJECT_ENVIRONMENT=/opt/venv UV_CACHE_DIR=/tmp/uv-cache
RUN --mount=type=cache,id=caprmedio-uv,target=/tmp/uv-cache uv sync --locked --no-dev --group rmed-workflow-mcp --group workflow-orchestrator \
    --group validate-atoms --group validate-atoms-dev --group workbench
RUN /opt/venv/bin/python -c "import duckdb; c=duckdb.connect(':memory:',config={'extension_directory':'/home/caprmedio/.duckdb/extensions'}); c.execute('INSTALL duckpgq FROM community'); c.close()" \
    && chown -R ${RUNTIME_UID}:${RUNTIME_GID} /home/caprmedio/.duckdb
COPY version.toml ./
COPY LAYER_2_FRAMEWORK_ENGINE ./LAYER_2_FRAMEWORK_ENGINE
COPY --from=workbench_frontend /frontend/dist \
     ./LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_FRONTEND/dist
RUN mkdir -p /home/caprmedio/.codex /workspace/.caprmedio_install \
    /workspace/.caprmedio_tmp /workspace/tmp /workspace/.caprmedio_caprmedio \
    && chown -R ${RUNTIME_UID}:${RUNTIME_GID} /home/caprmedio
ENV PATH=/opt/venv/bin:/usr/local/bin:/usr/bin:/bin PYTHONDONTWRITEBYTECODE=1
USER caprmedio
ENTRYPOINT ["/opt/venv/bin/python", "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker/entrypoint.py"]
