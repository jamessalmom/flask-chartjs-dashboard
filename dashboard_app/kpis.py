"""Server-side KPI aggregation feeding the dashboard.

In a real deployment these would query the warehouse; here they operate
on an in-memory list of sales records so the module is fully testable
without a database.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class SaleRecord:
    month: str  # "2026-01"
    consultant: str
    amount: float


def revenue_by_month(sales: list[SaleRecord]) -> dict[str, float]:
    totals: dict[str, float] = defaultdict(float)
    for sale in sales:
        totals[sale.month] += sale.amount
    return dict(sorted(totals.items()))


def ranking_by_consultant(sales: list[SaleRecord]) -> list[dict[str, float]]:
    totals: dict[str, float] = defaultdict(float)
    for sale in sales:
        totals[sale.consultant] += sale.amount
    ranked = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)
    return [{"consultant": name, "total": round(total, 2)} for name, total in ranked]


def average_ticket(sales: list[SaleRecord]) -> float:
    if not sales:
        return 0.0
    return round(sum(s.amount for s in sales) / len(sales), 2)
