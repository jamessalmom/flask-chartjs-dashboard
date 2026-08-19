"""dashboard_app

Minimal, dependency-light Flask blueprint for a dark-mode executive
dashboard: server computes/aggregates the KPIs, the template only renders
Chart.js from a small JSON payload injected server-side. No SPA build
step, no client-side data fetching layer to maintain.
"""

from flask import Flask

from .views import dashboard_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(dashboard_bp)
    return app


__all__ = ["create_app", "dashboard_bp"]
__version__ = "0.1.0"
