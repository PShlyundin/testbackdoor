#!/usr/bin/env python3
"""
Monorepo main application
Combines all microservices into a single FastAPI application
"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import applications
from apps.task_manager.main import app as task_manager_app
# from apps.user_management.main import app as user_management_app
# from apps.notification_service.main import app as notification_app

# Create main application
app = FastAPI(
    title="Task Manager Monorepo",
    description="Monorepo containing multiple microservices",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include sub-applications
app.mount("/tasks", task_manager_app)
# app.mount("/users", user_management_app)
# app.mount("/notifications", notification_app)

@app.get("/")
def read_root():
    """Root endpoint"""
    return {
        "message": "Task Manager Monorepo API",
        "services": {
            "tasks": "/tasks",
            "docs": "/docs",
            "redoc": "/redoc"
        }
    }

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "services": ["task-manager"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True) 