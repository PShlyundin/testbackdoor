from sqlalchemy.orm import Session
from app import models, schemas
from typing import List, Optional

def get_task(db: Session, task_id: int) -> Optional[models.Task]:
    """Get task by ID"""
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 100) -> List[models.Task]:
    """Get all tasks with pagination"""
    return db.query(models.Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: schemas.TaskCreate) -> models.Task:
    """Create new task"""
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task: schemas.TaskUpdate) -> Optional[models.Task]:
    """Update task by ID"""
    db_task = get_task(db, task_id)
    if db_task:
        update_data = task.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_task, field, value)
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int) -> bool:
    """Delete task by ID"""
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False

def get_tasks_by_status(db: Session, status: bool, skip: int = 0, limit: int = 100) -> List[models.Task]:
    """Get tasks by status (completed or not completed)"""
    return db.query(models.Task).filter(models.Task.status == status).offset(skip).limit(limit).all() 