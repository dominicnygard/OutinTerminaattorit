from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.references_repository import get_citations, save_references
from config import app, test_env
from util import reference_fields


@app.route("/")
def index():
    citations = get_citations()
    return render_template("index.html", citations=citations) 

@app.route("/references/type")
def choose_reference_type():
    return render_template("reference_choice.html")

@app.route("/references/new", methods=["GET", "POST"])
def new_reference():
    type = request.args.get('reference_type') or request.form.get('reference_type')

    return render_template("new_reference.html", fields = reference_fields[type], type = type)

@app.route("/references/create", methods=["POST"])
def create_reference():
    references = dict(request.form)
    type = references.pop('reference_type')
    references = {k: (None if v == '' else v) for k, v in references.items()}
    save_references(references, type)
    return redirect("/")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
