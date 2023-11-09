from flask import Flask, render_template, request, flash, redirect, send_file, url_for

from ..app import app, db, login

from ..modeles.data import Amendes, Justiciables

from .forms import RechercheForm

from sqlalchemy import and_, or_

from ..constantes import RESULTATS_PAR_PAGES

from flask_login import login_user, current_user, logout_user, login_required
from warnings import warn
import random, sqlalchemy

@app.route("/")
def accueil():
    return render_template("pages/index.html")

@app.route("/index/amendes/")
def index_amendes():
    page = request.args.get("page", 1)
    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1
    amendes = Amendes.query.paginate(page=page, per_page=RESULTATS_PAR_PAGES)
    return render_template("pages/index_amendes.html", amendes=amendes)

@app.route("/index/justiciables/")
def index_justiciables():
    page = request.args.get("page", 1)
    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1
    justiciables = Justiciables.query.paginate(page=page, per_page=RESULTATS_PAR_PAGES)
    return render_template("pages/index_justiciables.html", justiciables=justiciables)


@app.route("/amende/<identifiant>")
def amende(identifiant):
    amende_unique = Amendes.query.filter(Amendes.identifiant == identifiant).first()
    return render_template("pages/amende.html", amende=amende_unique)

@app.route("/add_amende", methods=["GET", "POST"])
def add_amende():
    if request.method == "POST":
        statut, informations = Amendes.add_amende(
            add_amende_id=request.form.get("add_amende_id", None),
            add_amende_cote=request.form.get("add_amende_cote", None),
            add_amende_date=request.form.get("add_amende_date", None),
            add_amende_typeTaxe=request.form.get("add_amende_typeTaxe", None),
            add_amende_sexe=request.form.get("add_amende_sexe", None),
            add_amende_montant=request.form.get("add_amende_montant", None),
            add_amende_parisis=request.form.get("add_amende_parisis", None),
            add_amende_moment=request.form.get("add_amende_moment", None),
            add_amende_typeDelit=request.form.get("add_amende_typeDelit", None),
            add_amende_reunion=request.form.get("add_amende_reunion", None),
            add_amende_franchesverites=request.form.get("add_amende_franchesverites", None),
            add_amende_tiers=request.form.get("add_amende_tiers", None),
            add_amende_transcription=request.form.get("add_amende_transcription", None),
            add_id_personne=request.form.get("add_id_personne", None)
        )

        if statut is True:
            flash("Ajout d'une nouvelle amende", "success")
            return redirect("/")
        else:
            flash("L'ajout a échoué pour les raisons suivantes : " + ", ".join(informations), "danger")
            return render_template("pages/add_amende.html")
    else:
        return render_template("pages/add_amende.html")


@app.route("/justiciable/<id_personne>")
def justiciable(id_personne):
    justiciable_unique = Justiciables.query.filter(Justiciables.id_personne == id_personne).first()
    return render_template("pages/justiciable.html", justiciable=justiciable_unique)

@app.route("/recherche")
def recherche():


    motclef = request.args.get("keyword", None)
    page = request.args.get("page", 1)
    resultats = []
    titre = "Recherche"

    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    if motclef:
        resultats = \
            Amendes.query.filter(or_(
                Amendes.transcription.like("%{}%".format(motclef)),
                Amendes.cote.like("%{}%".format(motclef)),
                Amendes.date.like("%{}%".format(motclef)),
                Amendes.montant.like("%{}%".format(motclef)),
                Amendes.typeDelit.like("%{}%".format(motclef)),
                Amendes.moment.like("%{}%".format(motclef)),
            )
        )\
            .paginate(page=page, per_page=RESULTATS_PAR_PAGES)

        titre = "Résultat pour la recherche '" + motclef + "'"
    return render_template("pages/recherche.html", resultats=resultats, titre=titre, keyword=motclef)

from flask import render_template

@app.route('/recherche_avancee', methods=['GET', 'POST'])
def recherche_avancee():
    form = RechercheForm()

    if form.validate_on_submit():
        resultats = Amendes.query

        if form.cote.data:
            resultats = resultats.filter(Amendes.cote == form.cote.data)

        if form.date.data:
            resultats = resultats.filter(Amendes.date == form.date.data)

        if form.sexe.data:
            resultats = resultats.filter(Amendes.sexe == form.sexe.data)

        if form.montant.data:
            resultats = resultats.filter(Amendes.montant == form.montant.data)

        if form.parisis.data:
            resultats = resultats.filter(Amendes.parisis == form.parisis.data)

        if form.moment.data:
            resultats = resultats.filter(Amendes.moment == form.moment.data)

        if form.typeDelit.data:
            resultats = resultats.filter(Amendes.typeDelit == form.typeDelit.data)

        if form.reunion.data:
            resultats = resultats.filter(Amendes.reunion == form.reunion.data)

        if form.franchesVerites.data:
            resultats = resultats.filter(Amendes.franchesVerites == form.franchesVerites.data)

        if form.tiers.data:
            resultats = resultats.filter(Amendes.tiers == form.tiers.data)

        if form.transcription.data:
            resultats = resultats.filter(Amendes.transcription == form.transcription.data)

        if form.id_personne.data:
            resultats = resultats.filter(Amendes.id_personne == form.id_personne.data)

        resultats = resultats.all()

        return render_template("pages/resultats_avancee.html", resultats=resultats)

    return render_template("pages/recherche_avancee.html", form=form)


@app.route('/download_sql')
def download_sql():
    f = 'app/bdd_crimilille.sql'
    return send_file(f, attachment_filename='bdd_crimilille.sql', as_attachment=True)

@app.route('/download_amendes_csv')
def download_amendes_csv():
    f = 'app/amendes.csv'
    return send_file(f, attachment_filename='amendes.csv', as_attachment=True)

@app.route('/download_justiciables_csv')
def download_justiciables_csv():
    f = 'app/justiciables.csv'
    return send_file(f, attachment_filename='justiciables.csv', as_attachment=True)