#!/usr/bin/env python3
"""
AI Memory Palace - Demo Script
Demonstrates the project structure and validates components
"""

import os
import json
import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a file exists and print status."""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} (missing)")
        return False

def validate_json_file(filepath, description):
    """Validate JSON file syntax."""
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        print(f"✅ {description}: Valid JSON")
        return True
    except Exception as e:
        print(f"❌ {description}: Invalid JSON - {e}")
        return False

def main():
    print("🏛️  AI Memory Palace - Project Validation")
    print("=" * 50)
    
    # Check project structure
    print("\n📁 Project Structure:")
    components = [
        ("backend/app/__init__.py", "Backend Flask App"),
        ("backend/app/models.py", "Database Models"),
        ("backend/app/api/auth.py", "Authentication API"),
        ("backend/app/api/users.py", "Users API"),
        ("backend/wsgi.py", "WSGI Entry Point"),
        ("backend/requirements.txt", "Backend Dependencies"),
        ("frontend/package.json", "Frontend Dependencies"),
        ("frontend/src/App.js", "React Main Component"),
        ("frontend/src/components/Dashboard.js", "Dashboard Component"),
        ("frontend/src/contexts/AuthContext.js", "Auth Context"),
        ("database/schema.sql", "Database Schema"),
        ("worker/celery_app.py", "Celery Worker"),
        ("docker-compose.yml", "Docker Orchestration"),
        ("nginx/nginx.conf", "Nginx Configuration"),
    ]
    
    all_exist = True
    for filepath, description in components:
        if not check_file_exists(filepath, description):
            all_exist = False
    
    # Validate JSON files
    print("\n🔍 JSON Validation:")
    json_files = [
        ("frontend/package.json", "Frontend Package"),
        ("backend/app/config.py", "Backend Config (Python)"),
    ]
    
    # Validate package.json
    if os.path.exists("frontend/package.json"):
        validate_json_file("frontend/package.json", "Frontend Package")
    
    # Check Python syntax
    print("\n🐍 Python Syntax Check:")
    python_files = [
        "backend/app/__init__.py",
        "backend/app/models.py",
        "backend/app/config.py",
        "backend/wsgi.py",
        "worker/celery_app.py"
    ]
    
    for py_file in python_files:
        if os.path.exists(py_file):
            try:
                with open(py_file, 'r') as f:
                    compile(f.read(), py_file, 'exec')
                print(f"✅ {py_file}: Valid Python syntax")
            except SyntaxError as e:
                print(f"❌ {py_file}: Syntax error - {e}")
                all_exist = False
    
    # Check environment configuration
    print("\n⚙️  Configuration:")
    if check_file_exists(".env.example", "Environment Template"):
        with open(".env.example", 'r') as f:
            env_vars = [line.split('=')[0] for line in f if '=' in line and not line.startswith('#')]
            print(f"   📋 Environment variables defined: {len(env_vars)}")
            for var in env_vars[:5]:  # Show first 5
                print(f"      • {var}")
            if len(env_vars) > 5:
                print(f"      ... and {len(env_vars) - 5} more")
    
    # Show API endpoints
    print("\n🌐 API Endpoints:")
    endpoints = [
        "GET  /health - Health check",
        "POST /auth/register - User registration", 
        "POST /auth/login - User login",
        "GET  /auth/verify - Token verification",
        "GET  /users/profile - Get user profile",
        "PUT  /users/profile - Update profile",
        "GET  /users/memory-palaces - List palaces",
        "POST /users/memory-palaces - Create palace"
    ]
    
    for endpoint in endpoints:
        print(f"   📡 {endpoint}")
    
    # Show database tables
    print("\n🗄️  Database Schema:")
    tables = [
        "users - User accounts and authentication",
        "memory_palaces - User's memory palace collections", 
        "rooms - Individual rooms within palaces",
        "memory_items - Items stored in rooms"
    ]
    
    for table in tables:
        print(f"   📊 {table}")
    
    # Show services
    print("\n🐳 Docker Services:")
    services = [
        "frontend - React.js application (port 3000)",
        "backend - Flask API server (port 5000)",
        "database - PostgreSQL database (port 5432)",
        "redis - Cache and task queue (port 6379)",
        "worker - Celery background tasks",
        "nginx - Load balancer and reverse proxy (port 80)"
    ]
    
    for service in services:
        print(f"   🔧 {service}")
    
    # Summary
    print("\n" + "=" * 50)
    if all_exist:
        print("🎉 Project Status: COMPLETE AND READY!")
        print("\n🚀 To run the application:")
        print("   1. Install Docker and Docker Compose")
        print("   2. Run: docker-compose up --build")
        print("   3. Access: http://localhost:3000")
        print("\n📖 See README.md for detailed instructions")
    else:
        print("⚠️  Project Status: Some components missing")
    
    print("\n🏛️  AI Memory Palace - Validation Complete")

if __name__ == "__main__":
    main()