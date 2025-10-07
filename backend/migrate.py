#!/usr/bin/env python3
"""
Database migration script for AI Memory Palace
"""

import os
from flask import Flask
from flask_migrate import Migrate, init, migrate, upgrade
from app import create_app
from app.models import db

def run_migrations():
    """Initialize and run database migrations."""
    app = create_app()
    
    with app.app_context():
        # Initialize migration repository if it doesn't exist
        if not os.path.exists('migrations'):
            print("Initializing migration repository...")
            init()
        
        # Create migration if models have changed
        print("Creating migration...")
        migrate(message='Auto migration')
        
        # Apply migrations
        print("Applying migrations...")
        upgrade()
        
        print("Migrations completed successfully!")

if __name__ == '__main__':
    run_migrations()