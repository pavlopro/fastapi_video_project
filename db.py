import databases
import sqlalchemy

database = databases.Database("sqlite:///db.sqlite")
engine = sqlalchemy.create_engine("sqlite:///sqlite.db")
metadata = sqlalchemy.MetaData()

metadata.create_all(engine)

