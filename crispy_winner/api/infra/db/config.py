from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

eng = create_engine('postgresql+psycopg2://test:password@postgres/postgres', echo=True)

Base = declarative_base()
Base.metadata.bind = eng

Session = sessionmaker(bind=eng)
