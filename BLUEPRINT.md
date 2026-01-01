# Caneleira Project Blueprint

This document serves as a technical blueprint for the Caneleira project, providing a detailed overview of its architecture, patterns, and principles. It is intended to guide developers and AI assistants in understanding and contributing to the codebase.

The project is a modern full-stack application composed of a Python backend and a React frontend, both organized using a cohesive feature-sliced architecture.

## Backend

The backend is a robust API built with Python, leveraging modern tooling and a clean, layered architecture to ensure scalability and maintainability.

### Technology Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) for building high-performance, asynchronous APIs with automatic OpenAPI documentation.
- **Language**: Python 3.12+.
- **Database ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) for interacting with the PostgreSQL database.
- **Database Migrations**: [Alembic](https://alembic.sqlalchemy.org/) for managing database schema changes.
- **Configuration**: [Pydantic Settings](https://docs.pydantic.dev/latest/usage/settings/) for type-safe environment variable management.
- **Dependency Management**: `uv` for fast package installation and resolution.

### Architectural Patterns

The backend follows a **feature-sliced, layered architecture**. This design promotes separation of concerns, modularity, and testability.

- **Feature-Sliced Design**: The core business logic is organized into "features" (e.g., `cattle`, `herd`). Each feature is a self-contained module that encapsulates all related logic, from API endpoints to database interactions.
- **Layered Architecture**: Within each feature, logic is separated into distinct layers:
    1.  **Router (API Layer)**: Defines API endpoints using FastAPI's `APIRouter`. It handles HTTP request/response validation and delegates business logic to the Service layer.
    2.  **Service (Business Logic Layer)**: Contains the core business logic and orchestrates operations. It acts as an intermediary between the API layer and the data access layer.
    3.  **Repository (Data Access Layer)**: Manages all communication with the database. It abstracts away the specifics of SQLAlchemy, providing a clean interface for data manipulation (CRUD operations).

### Folder Structure

```
backend/
├── alembic.ini         # Alembic configuration
├── app/
│   ├── main.py         # Main FastAPI application entrypoint
│   ├── core/           # Application-wide configuration, logging, and security
│   ├── db/             # Database session management, base models, and migrations
│   └── features/       # Business logic organized by feature
│       └── cattle/
│           ├── router.py     # API endpoints for the cattle feature
│           ├── service.py    # Business logic for cattle
│           ├── repository.py # Data access for cattle
│           ├── model.py      # SQLAlchemy ORM model for the 'cattle' table
│           ├── schema.py     # Pydantic schemas for request/response validation
│           └── dependencies.py # Feature-specific dependency injection
└── tests/              # Unit and integration tests
```

## Frontend

The frontend is a dynamic and type-safe single-page application (SPA) built with React and TypeScript, mirroring the backend's feature-sliced philosophy.

### Technology Stack

- **Framework**: [React](https://react.dev/) for building the user interface.
- **Language**: [TypeScript](https://www.typescriptlang.org/) for static typing and improved developer experience.
- **Build Tool**: [Vite](https://vitejs.dev/) for fast development and optimized builds.
- **Package Manager**: [Yarn](https://yarnpkg.com/).

### Key Libraries & Patterns

- **Routing**: [TanStack Router](https://tanstack.com/router) for fully type-safe, file-based routing. Routes are defined in the `src/routes` directory.
- **Server State Management**: [TanStack Query (React Query)](https://tanstack.com/query) for fetching, caching, and synchronizing server state. This simplifies data fetching and eliminates the need for a global client-side state manager for server data.
- **Styling**: [Tailwind CSS](https://tailwindcss.com/) for a utility-first CSS workflow.
- **UI Components**: [shadcn/ui](https://ui.shadcn.com/) for a collection of beautifully designed, accessible, and unstyled base components. These are located in `src/components/ui` and are composed to build feature-specific components.

### Architectural Patterns

The frontend architecture is also **feature-sliced**, creating a clear and organized structure that aligns perfectly with the backend API.

- **Feature-Sliced Design**: UI and client-side logic are grouped by feature (e.g., `cattle`). Each feature directory contains everything needed for that feature to function, including pages, components, API hooks, and type definitions.
- **Component-Based Architecture**: The UI is built from reusable React components. A clear distinction is made between generic, reusable UI primitives (`src/components/ui`) and more complex, feature-specific components (`src/features/{feature-name}/components`).
- **Custom Hooks for Data Fetching**: TanStack Query logic is abstracted into custom hooks within each feature (e.g., `useListCattle`, `useAddCattle`). This encapsulates data-fetching logic and makes it easily reusable across different components.

### Folder Structure

```
frontend/
├── src/
│   ├── app/              # Core application setup (Providers, etc.)
│   ├── components/
│   │   └── ui/           # Base UI components from shadcn/ui
│   ├── features/         # Client-side logic and components organized by feature
│   │   └── cattle/
│   │       ├── components/   # React components specific to the cattle feature
│   │       ├── hooks/        # Custom hooks using TanStack Query (e.g., useListCattle)
│   │       ├── api/          # API client functions for the cattle endpoint
│   │       ├── pages/        # Feature-specific pages (if not using file-based routing pages)
│   │       └── types.ts      # TypeScript types for the cattle feature
│   ├── lib/              # Shared utilities (e.g., cn for Tailwind class merging)
│   └── routes/           # File-based routing definitions for TanStack Router
└── package.json          # Project dependencies and scripts
```
