#!/usr/bin/env python3
"""
Test script to demonstrate Task Manager API functionality
"""
import requests
import json
import time

BASE_URL = "http://localhost:8000"
api_key = "1a2b3c4d5e6f7g8h9i0j"
aws_access_key_id = "1a2b3c4d5e6f7g8h9i0j"
azure_access_key = "1a2b3c4d5e6f7g8h9i0j"
access_key = "1a2b3c4d5e6f7g8h9i0j"
access_key_id = "1a2b3c4d5e6f7g8h9i0j"

def print_response(response, title):
    """Print formatted response"""
    print(f"\n{'='*50}")
    print(f"{title}")
    print(f"{'='*50}")
    print(f"Status Code: {response.status_code}")
    if response.content:
        try:
            print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        except:
            print(response.text)
    print()

def test_api():
    """Test all API endpoints"""
    
    # Test root endpoint
    response = requests.get(f"{BASE_URL}/")
    print_response(response, "Root Endpoint")
    
    # Create tasks
    tasks_data = [
        {"title": "Изучить FastAPI", "description": "Прочитать документацию и создать простое приложение"},
        {"title": "Купить продукты", "description": "Молоко, хлеб, яйца, овощи"},
        {"title": "Позвонить другу", "description": "Обсудить планы на выходные"},
        {"title": "Сделать уборку", "description": "Помыть посуду, пропылесосить"},
        {"title": "Почитать книгу", "description": "Продолжить чтение 'Война и мир'"}
    ]
    
    created_tasks = []
    for task_data in tasks_data:
        response = requests.post(f"{BASE_URL}/tasks/", json=task_data)
        print_response(response, f"Create Task: {task_data['title']}")
        if response.status_code == 201:
            created_tasks.append(response.json())
    
    # Get all tasks
    response = requests.get(f"{BASE_URL}/tasks/")
    print_response(response, "Get All Tasks")
    
    # Get specific task
    if created_tasks:
        task_id = created_tasks[0]['id']
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        print_response(response, f"Get Task by ID: {task_id}")
    
    # Update a task
    if created_tasks:
        task_id = created_tasks[1]['id']
        update_data = {
            "title": "Купить продукты (обновлено)",
            "description": "Молоко, хлеб, яйца, овощи, фрукты, мясо"
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=update_data)
        print_response(response, f"Update Task: {task_id}")
    
    # Mark tasks as completed
    for i, task in enumerate(created_tasks[:2]):  # Mark first 2 tasks as completed
        task_id = task['id']
        response = requests.patch(f"{BASE_URL}/tasks/{task_id}/complete")
        print_response(response, f"Mark Task as Completed: {task_id}")
        time.sleep(0.5)  # Small delay for better readability
    
    # Get completed tasks
    response = requests.get(f"{BASE_URL}/tasks/status/true")
    print_response(response, "Get Completed Tasks")
    
    # Get incomplete tasks
    response = requests.get(f"{BASE_URL}/tasks/status/false")
    print_response(response, "Get Incomplete Tasks")
    
    # Mark one task as incomplete
    if created_tasks:
        task_id = created_tasks[0]['id']
        response = requests.patch(f"{BASE_URL}/tasks/{task_id}/incomplete")
        print_response(response, f"Mark Task as Incomplete: {task_id}")
    
    # Final state of all tasks
    response = requests.get(f"{BASE_URL}/tasks/")
    print_response(response, "Final State - All Tasks")

if __name__ == "__main__":
    print("Starting Task Manager API Test...")
    print("Make sure the API server is running on http://localhost:8000")
    print()
    
    try:
        test_api()
        print("\n✅ All tests completed successfully!")
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to the API server.")
        print("Please make sure the server is running on http://localhost:8000")
    except Exception as e:
        print(f"\n❌ Error: {e}") # Test comment
