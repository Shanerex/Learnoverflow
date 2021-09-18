from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/courses")
def courses():
  return render_template("courses.html")

@app.route("/courseshome")
def courses_home():
  return render_template("course_home.html")

@app.route("/newsletter")
def newsletter():
  return render_template("newsletter.html")

@app.route("/player")
def player():
  return render_template("player.html")

@app.route("/privacy")
def privacy():
  return render_template("privacy.html")

@app.route("/register")
def register():
  return render_template("register.html")

app.run()
