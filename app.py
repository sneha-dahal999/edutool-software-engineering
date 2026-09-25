from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "edutool-demo-key"

DEMO_USER = {"username": "sneha", "password": "password123"}

BOOKS = [
    {"title": "Python Basics", "author": "A. Sharma", "topic": "Programming"},
    {"title": "Software Engineering Fundamentals", "author": "R. Kumar", "topic": "Software Engineering"},
    {"title": "Introduction to Cyber Security", "author": "M. Singh", "topic": "Cyber Security"},
    {"title": "Database Management Essentials", "author": "J. Patel", "topic": "Database"},
]


@app.route("/", methods=["GET"])
def home():
    if "username" in session:
        return redirect(url_for("catalogue"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if username == DEMO_USER["username"] and password == DEMO_USER["password"]:
            session["username"] = username
            return redirect(url_for("catalogue"))

        error = "Invalid username or password."

    return render_template("login.html", error=error)


@app.route("/catalogue", methods=["GET"])
def catalogue():
    if "username" not in session:
        return redirect(url_for("login"))

    query = request.args.get("q", "").strip().lower()
    results = BOOKS

    if query:
        results = [
            book for book in BOOKS
            if query in book["title"].lower()
            or query in book["author"].lower()
            or query in book["topic"].lower()
        ]

    return render_template(
        "catalogue.html",
        books=results,
        query=query,
        username=session["username"],
    )


@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
