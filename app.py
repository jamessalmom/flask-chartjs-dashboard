"""Dev entrypoint: `flask --app app run` or `python app.py`."""

from dashboard_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
