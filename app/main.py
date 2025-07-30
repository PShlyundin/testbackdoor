from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uvicorn

from app import crud, models, schemas
from app.database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="A simple task management API with SQLite database",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Welcome to Task Manager API"}

@app.post("/tasks/", response_model=schemas.Task, status_code=status.HTTP_201_CREATED)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """Create a new task"""
    return crud.create_task(db=db, task=task)

@app.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all tasks with pagination"""
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks

@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """Get a specific task by ID"""
    task = crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    """Update a task by ID"""
    updated_task = crud.update_task(db, task_id=task_id, task=task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """Delete a task by ID"""
    success = crud.delete_task(db, task_id=task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")

@app.patch("/tasks/{task_id}/complete", response_model=schemas.Task)
def complete_task(task_id: int, db: Session = Depends(get_db)):
    """Mark a task as completed"""
    task_update = schemas.TaskUpdate(status=True)
    updated_task = crud.update_task(db, task_id=task_id, task=task_update)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.patch("/tasks/{task_id}/incomplete", response_model=schemas.Task)
def incomplete_task(task_id: int, db: Session = Depends(get_db)):
    """Mark a task as not completed"""
    task_update = schemas.TaskUpdate(status=False)
    updated_task = crud.update_task(db, task_id=task_id, task=task_update)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.get("/tasks/status/{status}", response_model=List[schemas.Task])
def read_tasks_by_status(status: bool, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get tasks by status (true for completed, false for not completed)"""
    tasks = crud.get_tasks_by_status(db, status=status, skip=skip, limit=limit)
    return tasks

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 