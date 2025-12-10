from flask import redirect, render_template, request, jsonify, Response
from db_helper import reset_db
from repositories.references_repository import get_citations, save_references, \
                                        search_references, get_references_by_id, filter_references
from config import app, test_env
from util import reference_fields, to_bibtex
import input_validation


@app.route("/")
def index():
    message = None
    citations = get_citations()
    query = request.args.get("query")
    year = request.args.get("year")
    author = request.args.get("author")
    types = request.args.getlist("type_filter")
    if query or year or author:
        citations = search_references(query=query, year=year, author=author)
        if len(citations) == 0:
            message = "No results matched the search query"
    if types:
        citations = filter_references(citations, types)

    return render_template(
        "index.html",
        citations=citations,
        message=message,
        selected_types=types or [],
        query=query or "",
        year=year or "",
        author=author or "",
    )

@app.route("/references/type")
def choose_reference_type():
    return render_template("reference_choice.html")

@app.route("/references/new", methods=["GET", "POST"])
def new_reference():
    ref_type = request.args.get('reference_type') or request.form.get('reference_type')

    return render_template("new_reference.html",
                           fields = reference_fields[ref_type],
                           type = ref_type)

@app.route("/references/create", methods=["POST"])
def create_reference():
    references = dict(request.form)
    ref_type = references.pop('reference_type')
    references = {k: (None if v == '' else v) for k, v in references.items()}

    for key in references:
        if references[key] is None:
            continue
        if key in input_validation.VALIDATION_METHODS:
            error = input_validation.VALIDATION_METHODS[key](references[key])
            if error:
                return render_template("new_reference.html",
                    fields = reference_fields[ref_type],
                    type = ref_type, error_message=error)

    save_references(references, ref_type)
    return redirect("/")

@app.route("/bibtex/download")
def download_all_bibtex():
    all_references = get_citations()
    all_citations = [get_references_by_id(ref["id"]) for ref in all_references]

    bibtex_entries = [to_bibtex(ref) for ref in all_citations]
    bibtex_text = "\n\n".join(bibtex_entries)

    return Response(
        bibtex_text,
        mimetype="application/x-bibtex",
        headers={"Content-Disposition": "attachment; filename=references.bib"}
    )

@app.route("/references/<int:ref_id>")
def reference_view(ref_id):
    citation = get_references_by_id(ref_id)
    bibtex_format = to_bibtex(citation)
    return render_template("reference.html", citation=citation, bibtex_format=bibtex_format)

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
