## Purpose

Knead is a learning project and real application.

The application code is written by the project owner. For now, agents should only provide review, feedback, architectural guidance, explanations, and targeted assistance rather than implementing features unless explicitly asked.

This may be subject to change.

## Architecture

Knead follows Domain-Driven-Design using Architecture Patterns with Python (Cosmic Python) as a key  architectural reference.

Key Rules:

### Keep the domain model as pure Python

Do not make the domain other infrastructure like FastAPI, Pydantic, SQLAlchemy, persistence, etc ...

### Organise code by bounded context

#### Example

This may change.

For example we have two distinct domain elements
Recipes provide the exact ingredients and methods to follow.

Bakes is like a journal and log of baking attempts.

```
src/
└── knead/
    ├── recipes/
    │   └── domain/
    │       └── model.py
    │
    └── bakes/
        └── domain/
            └── model.py
```

### Business rules belong in the appropriate domain

### Services

Application services orchestrate use cases.

### Adapters

FastAPI routes, persistence, and the eventual UI are adapters around the application/domain.

### Evolving Architecture

Introduce repositories, service layers, units of work, events, and other patterns only when the application requires them.

## Documentation

Treat documentation as part of the codebase.

- Each concept should have one canonical source of truth.
- Prefer references to existing documentation over duplicating guidance.
- Keep this file concise; detailed guidance belongs in `docs/`.
- When code changes make documentation inaccurate, update the relevant documentation in the same change.
- When adding documentation, link it from the appropriate parent or index document.
- Do not rewrite accepted Architecture Decision Records to reflect later decisions; create a new ADR when a decision is superseded.

### Documentation map

Read the relevant documentation before making changes in that area:

As the codebase evolves this map should remain updated.

#### <path>

<description>

#### `docs/architecture.md`

Current architecture, bounded contexts, dependency direction and application structure.

#### `docs/domain-model.md`

Domain terminology and current modelling decisions and definitions.

#### `docs/testing.md`

Testing strategy and conventions.

#### `docs/decisions.md`

Architecture decision records for significant architectural choices.
