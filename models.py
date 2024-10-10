import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Use PostgreSQL if DATABASE_URL is set, otherwise fall back to SQLite for local development
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')


if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Ms(db.Model):
    selected = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(256), primary_key=True)
    retention_index = db.Column(db.String(256))
    num_peaks = db.Column(db.String(256))
    d_alkane_rt1 = db.Column(db.String(256))
    n_alkane_rt1 = db.Column(db.String(256))
    instrument = db.Column(db.String(256))
    ionization = db.Column(db.String(256))
    injection_method = db.Column(db.String(256))
    gc_column = db.Column(db.String(256))
    oven_temp = db.Column(db.String(256))
    campaign_experimental_source = db.Column(db.String(256))
    experimental_condition = db.Column(db.String(256))
    contributor = db.Column(db.String(256))
    date_of_entry = db.Column(db.String(256))
    publications = db.Column(db.String(256))
    x_coordinates = db.Column(db.String(256))
    y_coordinates = db.Column(db.String(256))

    def to_dict(self):
        return {
            "Name": self.name,
            "Retention_index": self.retention_index,
            "Num Peaks": self.num_peaks,
            "d_alkane_RTI": self.d_alkane_rt1,
            "n_alkane_RTI": self.n_alkane_rt1,
            "Instrument": self.instrument,
            "Ionization": self.ionization,
            "Injection_method": self.injection_method,
            "gc_column": self.gc_column,
            "oven_temp": self.oven_temp,
            "campaign_experimental_source": self.campaign_experimental_source,
            "experimental_conditions": self.experimental_condition,
            "contributor": self.contributor,
            "date_of_entry": self.date_of_entry,
            "publications": self.publications,
            "selected": self.selected,
            "x_coordinates": self.x_coordinates,
            "y_coordinates": self.y_coordinates
        }