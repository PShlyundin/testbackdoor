#!/usr/bin/env python3
"""
Management script for Task Manager Monorepo
"""
import os
import sys
import subprocess
import argparse
from pathlib import Path

def run_command(command, cwd=None):
    """Run shell command"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, check=True, capture_output=True, text=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return False

def setup_environment():
    """Setup development environment"""
    print("Setting up development environment...")
    
    # Create virtual environment
    if not Path("venv").exists():
        run_command("python -m venv venv")
    
    # Install dependencies
    run_command("pip install -r requirements.txt")
    
    # Create data directory
    Path("data").mkdir(exist_ok=True)
    
    print("Environment setup complete!")

def start_services():
    """Start all services"""
    print("Starting services...")
    
    # Start with Docker Compose
    if run_command("docker-compose up -d"):
        print("Services started successfully!")
        print("API available at: http://localhost:8000")
        print("Docs available at: http://localhost:8000/docs")
    else:
        print("Failed to start services")

def stop_services():
    """Stop all services"""
    print("Stopping services...")
    run_command("docker-compose down")
    print("Services stopped")

def run_tests():
    """Run tests"""
    print("Running tests...")
    run_command("python -m pytest tests/")

def build_docker():
    """Build Docker image"""
    print("Building Docker image...")
    run_command("docker build -f docker/Dockerfile -t task-manager-monorepo .")

def main():
    parser = argparse.ArgumentParser(description="Task Manager Monorepo Management")
    parser.add_argument("command", choices=["setup", "start", "stop", "test", "build"], 
                       help="Command to execute")
    
    args = parser.parse_args()
    
    if args.command == "setup":
        setup_environment()
    elif args.command == "start":
        start_services()
    elif args.command == "stop":
        stop_services()
    elif args.command == "test":
        run_tests()
    elif args.command == "build":
        build_docker()

if __name__ == "__main__":
    main() 