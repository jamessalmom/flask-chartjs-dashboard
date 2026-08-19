from dashboard_app import create_app


def test_index_renders():
    app = create_app()
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Executive Dashboard" in resp.data


def test_kpis_endpoint_returns_expected_shape():
    app = create_app()
    client = app.test_client()
    resp = client.get("/api/kpis")
    assert resp.status_code == 200
    body = resp.get_json()
    assert "revenue_by_month" in body
    assert "ranking" in body
    assert "average_ticket" in body
