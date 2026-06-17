# Caneleira — Cattle Management Platform

A production-style, full-stack application for managing cattle, herds, and pastures on a livestock operation. Built to demonstrate a clean, scalable architecture end to end — typed Python API, typed React SPA, and the infrastructure to run both.

> **Why this repo exists:** it's a reference implementation of the patterns I use in production work — feature-sliced modules, a strict router → service → repository layering on the backend, fully type-safe data fetching on the frontend, and a one-command Docker setup. The domain (cattle/herd/pasture) is intentionally simple so the *engineering* stays in focus.

**Stack:** FastAPI · SQLAlchemy 2.0 (async) · Alembic · Pydantic · PostgreSQL · React 19 · TypeScript · TanStack Router & Query · Tailwind · shadcn/ui · Docker Compose · `uv`

---

## Architecture at a glance

```
┌──────────────────────────────┐         ┌──────────────────────────────┐
│  Frontend (React + TS)       │  HTTP   │  Backend (FastAPI)           │
│                              │ ──────► │                              │
│  routes/        (TanStack)   │  JSON   │  router    ← HTTP / validation│
│  features/<f>/  components    │         │  service   ← business logic   │
│    hooks/  (TanStack Query)  │ ◄────── │  repository← data access      │
│    api/    (typed client)    │         │  model/schema (ORM + Pydantic)│
└──────────────────────────────┘         └───────────────┬──────────────┘
                                                          │ SQLAlchemy
                                                  ┌───────▼────────┐
                                                  │  PostgreSQL    │
                                                  │  (Alembic mig.)│
                                                  └────────────────┘
```

Both sides share the same **feature-sliced** philosophy: each domain (`cattle`, `herd`, `pastures`) is a self-contained module owning its API, logic, and types. Adding a feature means adding a folder, not touching a monolith.

### Backend — layered per feature

Every feature follows the same strict separation, which keeps business logic testable and the database swappable:

| Layer | File | Responsibility |
|-------|------|----------------|
| **Router** | `router.py` | HTTP endpoints, request/response validation. No business logic. |
| **Service** | `service.py` | Business rules and orchestration. Framework-agnostic. |
| **Repository** | `repository.py` | All database access. Abstracts SQLAlchemy behind a clean interface. |
| **Model / Schema** | `model.py` / `schema.py` | SQLAlchemy ORM tables + Pydantic request/response contracts. |

### Frontend — typed all the way to the API

- **TanStack Router** for fully type-safe, file-based routing.
- **TanStack Query** for server-state caching, abstracted into per-feature hooks (`useListCattle`, `useAddCattle`, …) so components never touch fetch logic directly.
- **shadcn/ui + Tailwind** for accessible, composable UI primitives.

## Running it

Requires Docker, [`uv`](https://docs.astral.sh/uv/), and Node/Yarn.

**1. Start PostgreSQL** (Docker Compose provisions the database):

```bash
git clone https://github.com/gbilton/caneleira.git
cd caneleira
cp .env.example .env        # set POSTGRES_DB / POSTGRES_USER / POSTGRES_PASSWORD
docker compose up -d        # Postgres on :5432
```

**2. Run the backend:**

```bash
cd backend
cp .env.example .env        # set DATABASE_URL to match the compose values
uv sync
uv run alembic upgrade head # apply migrations
uv run fastapi dev app/main.py
```

API + interactive Swagger docs: http://localhost:8000/docs

**3. Run the frontend:**

```bash
cd frontend
yarn
yarn dev                    # http://localhost:5173
```

## Tests

The backend ships unit and integration tests per layer (service, repository, routes) with `pytest`:

```bash
cd backend
uv sync
uv run pytest
```

## Project layout

```
backend/
  app/
    core/        # config, logging, security
    db/          # session, base model, migrations
    features/    # cattle · herd · pastures  (router/service/repository/model/schema)
  tests/         # pytest, organized to mirror features/
frontend/
  src/
    routes/      # TanStack Router (file-based)
    features/    # per-feature components, hooks, api client, types
    components/  # shared shadcn/ui primitives
docker-compose.yml
```

See [`BLUEPRINT.md`](./BLUEPRINT.md) for the full architectural reference.

---

Built by [Guilherme Bilton](https://github.com/gbilton) — Full-Stack Engineer (Python · React · AWS). Open to remote roles.
