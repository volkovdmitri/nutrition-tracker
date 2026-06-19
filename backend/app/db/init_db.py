from app.db.base import Base
from app.db.database import engine

import app.db.food 

Base.metadata.create_all(bind=engine)
