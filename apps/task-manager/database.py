# Import from shared database configuration
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from shared.database import Base, engine, get_db, SessionLocal

# Re-export for backward compatibility
__all__ = ["Base", "engine", "get_db", "SessionLocal"] 