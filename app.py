from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.app_context().push()


app.config["SECRET_KEY"] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# Story class already provided, so we'll continue from there...

# Define the home route
@app.route('/')
def ask_questions():
    """Show home form for story prompts."""
    prompts = story.prompts
    return render_template("questions.html", prompts=prompts)

# Define the story route
@app.route("/story")
def show_story():
    """Show story result."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)


