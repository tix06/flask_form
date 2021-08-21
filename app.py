# app.py

# imports
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, UniqueConstraint, ForeignKey, DateTime
from sqlalchemy.exc import IntegrityError, InterfaceError
from sqlalchemy.orm import mapper, sessionmaker

from flask import Flask

from datetime import datetime
from flask import render_template, request, redirect, url_for


app = Flask(__name__) # Crée un instance de la classe Flask, c'est notre app


##########################
# connexion à la bdd sqlite avec sqlalchemy
##########################


# chaîne de connexion à une base de données PostgreSQL
engine = create_engine("postgresql+psycopg2://erictixidor@localhost:5432/form_db")


# metadata
metadata = MetaData()


prof_table = Table("profs",metadata,
    Column('pr_id', Integer, primary_key=True),
    Column('pr_name', String(50), unique=True, nullable=False),
    Column('pr_identifiant',String(50), nullable=True, default=None))

class Prof(object):
    def __init__(self,pr_name,pr_identifiant):
        self.pr_name = pr_name
        self.pr_identifiant = pr_identifiant

    def __repr__(self):
        return "<Prof(pr_name='%s', pr_identifiant='%s')>" % (self.pr_name, self.pr_identifiant)




# le mapping
mapper(Prof, prof_table)




# la session factory
Session = sessionmaker()
Session.configure(bind=engine)

session = None


# une session

session = Session()


# suppression de la table
session.execute("drop table if exists prof")

# recréation de la table à partir du mapping
metadata.create_all(engine)

# insertion
session.add(Prof("Charles Ingals", "Charles@Ingals"))
session.commit()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
