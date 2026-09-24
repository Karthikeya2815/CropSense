"""
app.py — CropSense: Seasonal Farm Analytics
Flask REST API & frontend routes.
Author: G Karthikeya
Run: python app.py
"""

from flask import Flask, jsonify, request, render_template, abort
from flask_cors import CORS
import analysis

app = Flask(__name__)
CORS(app)

# ── Helper ────────────────────────────────────────────────────────────────────

def ok(data):
    return jsonify({"status": "ok", "data": data})


def err(msg, code=400):
    return jsonify({"status": "error", "message": msg}), code


# ══════════════════════════════════════════════════════════════════════════════
# FRONTEND ROUTES
# ══════════════════════════════════════════════════════════════════════════════

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/explorer")
def explorer():
    return render_template("explorer.html")


@app.route("/report")
def report():
    return render_template("report.html")


# ══════════════════════════════════════════════════════════════════════════════
# REST API ROUTES  (all under /api/v1/)
# ══════════════════════════════════════════════════════════════════════════════

API = "/api/v1"


@app.route(f"{API}/summary")
def api_summary():
    """GET /api/v1/summary — Dataset overview & descriptive statistics."""
    return ok(analysis.summary_stats())


@app.route(f"{API}/yield/by-crop")
def api_yield_by_crop():
    """GET /api/v1/yield/by-crop — Average yield stats grouped by crop."""
    return ok(analysis.yield_by_crop())


@app.route(f"{API}/yield/by-season")
def api_yield_by_season():
    """GET /api/v1/yield/by-season — Average yield stats grouped by season."""
    return ok(analysis.yield_by_season())


@app.route(f"{API}/yield/by-state")
def api_yield_by_state():
    """GET /api/v1/yield/by-state — Average yield stats grouped by state."""
    return ok(analysis.yield_by_state())


@app.route(f"{API}/profitability")
def api_profitability():
    """GET /api/v1/profitability — Profitability metrics grouped by crop."""
    return ok(analysis.profitability_by_crop())


@app.route(f"{API}/irrigation")
def api_irrigation():
    """GET /api/v1/irrigation — Yield & water efficiency by irrigation method."""
    return ok(analysis.irrigation_analysis())


@app.route(f"{API}/correlation")
def api_correlation():
    """GET /api/v1/correlation — Pearson correlation matrix for key numeric features."""
    return ok(analysis.correlation_matrix())


@app.route(f"{API}/heatmap/season-crop")
def api_heatmap():
    """GET /api/v1/heatmap/season-crop — Avg yield pivot: season × crop."""
    return ok(analysis.season_crop_heatmap())


@app.route(f"{API}/farms/top-bottom")
def api_top_bottom():
    """GET /api/v1/farms/top-bottom?n=10 — Top & bottom N farms by yield."""
    try:
        n = int(request.args.get("n", 10))
        n = max(1, min(n, 50))
    except ValueError:
        return err("n must be an integer between 1 and 50")
    return ok(analysis.top_bottom_farms(n))


@app.route(f"{API}/rainfall-yield")
def api_rainfall_yield():
    """GET /api/v1/rainfall-yield — Avg yield per rainfall bucket."""
    return ok(analysis.rainfall_yield_buckets())


@app.route(f"{API}/disease-risk")
def api_disease_risk():
    """GET /api/v1/disease-risk — Disease & pest risk statistics by crop."""
    return ok(analysis.disease_risk_by_crop())


@app.route(f"{API}/water-efficiency")
def api_water_efficiency():
    """GET /api/v1/water-efficiency — Water efficiency by state."""
    return ok(analysis.water_efficiency_by_state())


@app.route(f"{API}/seed-quality")
def api_seed_quality():
    """GET /api/v1/seed-quality — Seed quality vs yield scatter sample."""
    return ok(analysis.seed_quality_vs_yield())


@app.route(f"{API}/insights")
def api_insights():
    """GET /api/v1/insights — Auto-generated key insights from the dataset."""
    return ok(analysis.key_insights())


@app.route(f"{API}/records")
def api_records():
    """GET /api/v1/records?page=1&page_size=50&crop=&season=&state= — Paginated raw records."""
    try:
        page = int(request.args.get("page", 1))
        page_size = int(request.args.get("page_size", 50))
        page_size = max(1, min(page_size, 200))
    except ValueError:
        return err("page and page_size must be integers")
    crop = request.args.get("crop") or None
    season = request.args.get("season") or None
    state = request.args.get("state") or None
    return ok(analysis.raw_records(page, page_size, crop, season, state))


@app.route(f"{API}/health")
def api_health():
    """GET /api/v1/health — Health check."""
    return ok({"message": "CropSense API is running."})


# ── Error handlers ────────────────────────────────────────────────────────────

@app.errorhandler(404)
def not_found(e):
    return err("Endpoint not found", 404)


@app.errorhandler(500)
def server_error(e):
    return err(f"Internal server error: {str(e)}", 500)


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
