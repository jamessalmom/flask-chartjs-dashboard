"""Dashboard blueprint: one route renders the page, one serves chart data."""

from __future__ import annotations

from flask import Blueprint, jsonify, render_template

from .kpis import SaleRecord, average_ticket, ranking_by_consultant, revenue_by_month

dashboard_bp = Blueprint("dashboard", __name__, template_folder="templates", static_folder="static")

# Demo dataset; swap for a real query in production.
_DEMO_SALES = [
    SaleRecord("2026-01", "Ana", 12000),
    SaleRecord("2026-01", "Bruno", 8000),
    SaleRecord("2026-02", "Ana", 15000),
    SaleRecord("2026-02", "Bruno", 9500),
    SaleRecord("2026-03", "Ana", 11000),
    SaleRecord("2026-03", "Bruno", 13500),
]


@dashboard_bp.get("/")
def index():
    return render_template("dashboard.html")


@dashboard_bp.get("/api/kpis")
def kpis():
    return jsonify(
        {
            "revenue_by_month": revenue_by_month(_DEMO_SALES),
            "ranking": ranking_by_consultant(_DEMO_SALES),
            "average_ticket": average_ticket(_DEMO_SALES),
        }
    )
