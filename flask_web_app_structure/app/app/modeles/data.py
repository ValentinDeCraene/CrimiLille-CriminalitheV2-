from flask import url_for
import datetime, jsonify, json
from sqlalchemy import and_
from ..app import db

class Amendes(db.Model):
    identifiant = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    cote = db.Column(db.Text)
    date = db.Column(db.Text)
    typeTaxe = db.Column(db.Text)
    sexe = db.Column(db.Text)
    montant = db.Column(db.Text)
    parisis = db.Column(db.Integer)
    moment = db.Column(db.Text)
    typeDelit = db.Column(db.Text)
    reunion = db.Column(db.Text)
    franchesVerites = db.Column(db.Text)
    tiers = db.Column(db.Text)
    id_personne = db.Column(db.Integer, db.ForeignKey('justiciables.id_personne'), nullable=False)
    transcription = db.Column(db.Text)
    # authorships = db.relationship("Authorship", back_populates="amende")

    justiciable = db.relationship("Justiciables", back_populates="amendes")
    @staticmethod
    def add_amende(add_amende_id, add_amende_cote, add_amende_date, add_amende_typeTaxe,
                   add_amende_sexe, add_amende_montant, add_amende_parisis, add_amende_moment,
                   add_amende_typeDelit, add_amende_reunion, add_amende_franchesverites,
                   add_amende_tiers, add_amende_transcription, add_id_personne):
        erreurs = []
        if not add_amende_id:
            erreurs.append("Veuillez renseigner l'identifiant pour cette amende.")
        if not add_amende_cote:
            erreurs.append(
                "Veuillez renseigner la cote de cette amende.")
        if not add_amende_date:
            erreurs.append(
                "Veuillez renseigner la cote de cette amende.")
        if not add_amende_typeTaxe:
            erreurs.append(
                "Veuillez renseigner la cote de cette amende.")
        if not add_amende_sexe:
            erreurs.append(
                "Veuillez renseigner la cote de cette amende.")
        if not add_amende_montant:
            erreurs.append(
                "Veuillez renseigner la cote de cette amende.")
        if not add_amende_parisis:
            erreurs.append(
                "Veuillez renseigner la cote de cette amende.")
        if not add_amende_moment:
            erreurs.append(
                "Veuillez renseigner la cote de cette amende.")
        if not add_amende_typeDelit:
            erreurs.append(
                "Veuillez renseigner la cote de cette amende.")
        if not add_amende_reunion:
            erreurs.append(
                "Veuillez renseigner la cote de cette amende.")
        if not add_amende_franchesverites:
            erreurs.append(
                "Veuillez renseigner la cote de cette amende.")
        if not add_amende_tiers:
            erreurs.append(
                "Veuillez renseigner la cote de cette amende.")
        if not add_amende_transcription:
            erreurs.append(
                "Veuillez renseigner la cote de cette amende.")
        if not add_id_personne:
            erreurs.append(
                "Veuillez renseigner la cote de cette amende.")

        if len(erreurs) > 0:
            return False, erreurs
        new_amende = Amendes(identifiant=add_amende_id, cote=add_amende_cote,
                             date = add_amende_date, typeTaxe = add_amende_typeTaxe,
                             sexe = add_amende_sexe, montant = add_amende_montant,
                             parisis = add_amende_parisis, moment = add_amende_moment,
                             typeDelit = add_amende_typeTaxe, reunion = add_amende_reunion,
                             franchesVerites = add_amende_franchesverites,
                             tiers = add_amende_tiers, transcription = add_amende_transcription, id_personne = add_id_personne)
        try:
            db.session.add(new_amende)
            db.session.commit()
            return True, new_amende

        except Exception as erreur:
            return False, [str(erreur)]


    @staticmethod
    def delete_amende(identifiant):
        del_amende = Amendes.query.get(identifiant)
        try:
            db.session.delete(del_amende)
            db.session.commit()
            return True
        except Exception as erreur:
            return False, [str(erreur)]

class Justiciables(db.Model):
    id_personne = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    # authorships = db.relationship("Authorship", back_populates="justiciable")
    nom = db.Column(db.Text)
    sexe = db.Column(db.Text)
    amendes = db.relationship("Amendes", back_populates="justiciable")

    @staticmethod
    def add_justiciable(add_id_personne, add_nom, add_sexe):
        erreurs = []
        if not add_id_personne:
            erreurs.append("Veuillez renseigner l'identifiant pour cette amende.")
        if not add_nom:
            erreurs.append(
                "Veuillez renseigner la cote de cette amende.")
        if not add_sexe:
            erreurs.append(
                "Veuillez renseigner la cote de cette amende.")
        if len(erreurs) > 0:
            return False, erreurs
        new_justiciable = Justiciables(id_personne=add_id_personne, nom=add_nom, sexe=add_sexe)
        try:
            db.session.add(new_justiciable)
            db.session.commit()
            return True, new_justiciable

        except Exception as erreur:
            return False, [str(erreur)]

    @staticmethod
    def delete_justiciable(identifiant):
        del_justiciable = Justiciables.query.get(identifiant)
        try:
            db.session.delete(del_justiciable)
            db.session.commit()
            return True
        except Exception as erreur:
            return False, [str(erreur)]