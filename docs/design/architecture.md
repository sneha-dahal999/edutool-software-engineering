# Architecture Design

Edutool.com uses a client-server structure with layered responsibilities.

1. Browser/client layer — presents pages, forms, catalogue cards and search.
2. Flask application layer — receives requests and coordinates application logic.
3. Service layer — separates authentication, catalogue, search, OCR and recommendation responsibilities.
4. Data layer — MongoDB stores application data.

The architecture supports separation of concerns and makes the main responsibilities visible. The exact implementation can be refined during development without changing the agreed project scope.
