from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

class RechercheForm(FlaskForm):
    cote = StringField('Cote')
    date = StringField('Date')
    sexe = SelectField('Sexe', choices=[('', 'Sélectionner...'), ('Masculin', 'Masculin'), ('Féminin', 'Féminin'), ('NR', 'Non renseigné')])
    montant = StringField('Montant')
    parisis = StringField('Soit en denier parisis')
    typeDelit = SelectField('Type de délit', choices=[('', 'Sélectionner...'), ('Brigandage/vie sur le pays', 'Brigandage/vie sur le pays'), ('Désobéissance', 'Désobéissance'), ('NR', 'Non renseigné'), ('abus d\'appel en justice', 'abus d\'appel en justice'), ('assaut d\'une maison', 'assaut d\'une maison'), ('atteinte biens d\'autrui', 'atteinte aux biens d\'autrui'), ('autre', 'autre'), ('défaut de comparution', 'défaut de comparution'), ('faute entretien héritage', 'faute entretien héritage'), ('injures', 'injures'), ('jeux de hasard', 'jeux de hasard'), ('port armes nues', 'port d\'armes nues'), ('rapt', 'rapt'), ('solidarité envers bannis', 'solidarité envers bannis'), ('tapage nocturne', 'tapage nocturne'), ('transgression édit/main de justice', 'transgression édit/main de justice'), ('usure', 'usure'), ('viol', 'viol'), ('violence physique', 'violence physique'), ('vol', 'vol'), ('violence physique', 'violence physique')])
    moment = SelectField('Moment', choices=[('', 'Sélectionner...'), ('Jour', 'Jour'), ('Nuit', 'Nuit'), ('NR', 'Non renseigné')])
    reunion = SelectField('Délit en réunion ?', choices=[('', 'Sélectionner...'), ('Non', 'Non'), ('Oui', 'Oui'), ('NR', 'Non renseigné')])
    franchesVerites = SelectField('Franche vérité', choices=[('', 'Sélectionner...'), ('Non', 'Non'), ('Oui', 'Oui'), ('NR', 'Non renseigné')])
    tiers = SelectField('Payée par un tiers ?', choices=[('', 'Sélectionner...'), ('Non', 'Non'), ('Oui', 'Oui'), ('NR', 'Non renseigné')])
    transcription = StringField('Transcription')
    id_personne = StringField('Justiciable ID')
