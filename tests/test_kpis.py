from dashboard_app.kpis import (
    SaleRecord,
    average_ticket,
    ranking_by_consultant,
    revenue_by_month,
)

SALES = [
    SaleRecord("2026-01", "Ana", 100),
    SaleRecord("2026-01", "Bruno", 50),
    SaleRecord("2026-02", "Ana", 200),
]


def test_revenue_by_month_aggregates_and_sorts():
    result = revenue_by_month(SALES)
    assert result == {"2026-01": 150, "2026-02": 200}
    assert list(result.keys()) == ["2026-01", "2026-02"]


def test_ranking_orders_descending():
    result = ranking_by_consultant(SALES)
    assert result[0]["consultant"] == "Ana"
    assert result[0]["total"] == 300


def test_average_ticket_handles_empty_list():
    assert average_ticket([]) == 0.0


def test_average_ticket_computes_mean():
    assert average_ticket(SALES) == round((100 + 50 + 200) / 3, 2)
