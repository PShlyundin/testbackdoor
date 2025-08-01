# Import from shared-fastapi-core
from shared_fastapi_core.database import Base, engine, get_db, SessionLocal

# Re-export for backward compatibility
__all__ = ["Base", "engine", "get_db", "SessionLocal"] 