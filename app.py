from flask import Flask, render_template, request

from services.analysis_service import AnalysisService

app = Flask(__name__)


# =====================================
# Dashboard
# =====================================
@app.route("/")
def index():
    return render_template("index.html")


# =====================================
# Analisis Saham
# =====================================
@app.route("/analysis", methods=["GET", "POST"])
def analysis():

    result = None
    error = None

    if request.method == "POST":

        symbol = request.form.get("symbol", "").strip().upper()

        if symbol:

            try:
                result = AnalysisService.analyze(symbol)

            except Exception as e:
                error = str(e)

        else:
            error = "Silakan masukkan kode saham."

    return render_template(
        "analysis.html",
        result=result,
        error=error
    )


# =====================================
# Scanner BEI
# =====================================
@app.route("/scanner")
def scanner():
    return render_template("scanner.html")


# =====================================
# Watchlist
# =====================================
@app.route("/watchlist")
def watchlist():
    return render_template("watchlist.html")


# =====================================
# Trading Journal
# =====================================
@app.route("/journal")
def journal():
    return render_template("journal.html")


# =====================================
# AI Assistant
# =====================================
@app.route("/ai")
def ai():
    return render_template("ai.html")


# =====================================
# Jalankan Server
# =====================================
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )