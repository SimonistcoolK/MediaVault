from flask import Flask, render_template, redirect, url_for

import Video

app = Flask(__name__)


SHORTS = Video.SHORTS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/shorts")
def index():
    return redirect(url_for("short", short_id=1))


@app.route("/short/<int:short_id>")
def short(short_id):
    shorts_by_id = {s["id"]: s for s in SHORTS}

    if short_id not in shorts_by_id:
        return redirect(url_for("short", short_id=SHORTS[0]["id"]))

    current = shorts_by_id[short_id]
    all_ids = [s["id"] for s in SHORTS]
    current_index = all_ids.index(short_id)

    prev_id = all_ids[current_index - 1] if current_index > 0 else None
    next_id = all_ids[current_index + 1] if current_index < len(all_ids) - 1 else None

    return render_template(
        "short.html",
        short=current,
        prev_id=prev_id,
        next_id=next_id,
        current_index=current_index + 1,
        total=len(SHORTS),
    )


if __name__ == "__main__":
    app.run(debug=True)
