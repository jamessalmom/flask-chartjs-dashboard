# flask-chartjs-dashboard

An executive dashboard where Flask does the aggregation and the page only draws the result. The browser fetches a small JSON payload and renders it with Chart.js, in a dark layout. There is no SPA framework and no build step.

## Why aggregate on the server

Revenue by month, consultant ranking and average ticket live in `kpis.py` as plain Python functions. That way they have unit tests and can be reused by a CLI report or a scheduled export, and the frontend only renders.

## Run it

```bash
pip install -r requirements.txt
flask --app app run
# open http://127.0.0.1:5000
```

## Structure

```
dashboard_app/
  kpis.py           # revenue_by_month, ranking_by_consultant, average_ticket
  views.py          # "/" renders the page, "/api/kpis" serves the JSON
  templates/
    dashboard.html  # dark layout + Chart.js
  static/css/dark.css
```

## Development

```bash
pip install pytest ruff
pytest
ruff check .
```

## License

MIT, see [LICENSE](LICENSE).
