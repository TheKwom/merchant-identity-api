# init_db.py
from app.models import merchants  # This ensures the table is registered
from app.database import engine, metadata

print("Creating tables...")
metadata.create_all(engine)
print("Done.")
