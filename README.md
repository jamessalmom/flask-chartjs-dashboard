# flask-chartjs-dashboard

A server-side-rendered executive dashboard: **Flask computes and
aggregates the KPIs**, the page just fetches a small JSON payload and
draws it with Chart.js. No SPA, no build step, no client-side data layer
— matches the "dashboard executivo em modo escuro" pattern used for a
commercial funnel/BI portal.

## Why server-side aggregation

Keeping revenue-by-month, ranking, and ticket-average calculations in
Python (`kpis.py`) instead of in the browser means the same functions are
unit-tested and reusable from a CLI report, a scheduled export, or the
dashboard — the frontend only renders.

## Run it

```bash
pip install -r requirements.txt
flask --app app run
# open http://127.0.0.1:5000
```

## Structure

```
dashboard_app/
  kpis.py           # pure functions: revenue_by_month, ranking_by_consultant, average_ticket
  views.py          # blueprint: "/" renders the page, "/api/kpis" serves JSON
  templates/
    dashboard.html  # dark-mode layout + Chart.js
  static/css/dark.css
```

## Development

```bash
pip install pytest ruff
pytest
ruff check .
```

## License

MIT — see [LICENSE](LICENSE).
