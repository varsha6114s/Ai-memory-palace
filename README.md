# AI Memory Palace

A full-stack application for creating and managing AI-powered memory palaces to enhance learning and retention.

## Architecture

- **Frontend**: React.js application
- **Backend**: Flask API with JWT authentication
- **Database**: PostgreSQL for data persistence
- **Cache/Queue**: Redis for caching and task queuing
- **Worker**: Celery for background processing
- **Reverse Proxy**: Nginx for load balancing

## Features

- User authentication and authorization
- Memory palace creation and management
- AI-powered content suggestions
- Real-time updates
- Background task processing

## Quick Start

1. Clone the repository
2. Copy environment variables: `cp .env.example .env`
3. Start the application: `docker-compose up --build`
4. Access the app at http://localhost:3000

## API Endpoints

- `GET /health` - Health check
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /users/profile` - Get user profile
- `PUT /users/profile` - Update user profile

## Development

Each service can be developed independently using Docker containers. See individual service directories for specific setup instructions.