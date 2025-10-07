# Contributing to AI Memory Palace

Thank you for your interest in contributing to the AI Memory Palace project! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites
- Docker and Docker Compose
- Git
- Node.js 18+ (for local frontend development)
- Python 3.11+ (for local backend development)

### Development Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ai-memory-palace
   ```

2. **Set up environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Start development environment**
   ```bash
   docker-compose up --build
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000
   - Health Check: http://localhost:5000/health

## 🏗️ Project Structure

```
ai-memory-palace/
├── frontend/          # React.js application
├── backend/           # Flask API server
├── database/          # PostgreSQL schema and migrations
├── worker/            # Celery background tasks
├── nginx/             # Load balancer configuration
├── scripts/           # Setup and utility scripts
└── docs/              # Documentation
```

## 🔧 Development Guidelines

### Code Style

#### Python (Backend)
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for functions and classes
- Maximum line length: 88 characters (Black formatter)

#### JavaScript/React (Frontend)
- Use ESLint configuration provided
- Follow React hooks patterns
- Use functional components over class components
- Use Material-UI components consistently

#### Database
- Use descriptive table and column names
- Include proper indexes for performance
- Write migration scripts for schema changes
- Document complex queries

### Testing

#### Backend Testing
```bash
cd backend
python -m pytest tests/
```

#### Frontend Testing
```bash
cd frontend
npm test
```

### API Development

#### Adding New Endpoints
1. Create route in appropriate blueprint (`backend/app/api/`)
2. Add input validation using Marshmallow schemas
3. Include proper error handling
4. Add authentication where required
5. Update API documentation

#### Example API Endpoint
```python
@users_bp.route('/example', methods=['POST'])
@jwt_required()
def create_example():
    """Create a new example resource."""
    user_id = get_jwt_identity()
    
    # Validate input
    schema = ExampleSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    # Business logic
    try:
        result = create_example_logic(user_id, data)
        return jsonify({'example': result.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': 'Creation failed'}), 500
```

### Frontend Development

#### Adding New Components
1. Create component in `frontend/src/components/`
2. Use Material-UI components
3. Implement proper error handling
4. Add loading states
5. Use React Query for API calls

#### Example React Component
```jsx
import React from 'react';
import { useQuery } from 'react-query';
import { CircularProgress, Alert } from '@mui/material';
import { api } from '../services/api';

const ExampleComponent = () => {
  const { data, isLoading, error } = useQuery(
    'example-data',
    () => api.get('/example').then(res => res.data)
  );

  if (isLoading) return <CircularProgress />;
  if (error) return <Alert severity="error">Failed to load data</Alert>;

  return (
    <div>
      {/* Component content */}
    </div>
  );
};

export default ExampleComponent;
```

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Environment information**
   - Operating system
   - Docker version
   - Browser (for frontend issues)

2. **Steps to reproduce**
   - Clear, numbered steps
   - Expected vs actual behavior
   - Screenshots if applicable

3. **Error messages**
   - Full error messages
   - Console logs
   - Network request details

## 💡 Feature Requests

For new features:

1. **Check existing issues** to avoid duplicates
2. **Describe the use case** and problem it solves
3. **Provide implementation ideas** if you have them
4. **Consider backward compatibility**

## 🔄 Pull Request Process

1. **Fork the repository** and create a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the guidelines above

3. **Test your changes**
   ```bash
   # Run all tests
   docker-compose -f docker-compose.test.yml up --build
   ```

4. **Commit with clear messages**
   ```bash
   git commit -m "feat: add user profile management
   
   - Add profile update endpoint
   - Implement profile editing UI
   - Add validation for user data"
   ```

5. **Push and create pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

### Commit Message Format

Use conventional commits:
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

## 🏷️ Release Process

1. **Version bumping** follows semantic versioning
2. **Changelog** is updated for each release
3. **Docker images** are built and tagged
4. **Documentation** is updated as needed

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://reactjs.org/docs/)
- [Material-UI Documentation](https://mui.com/)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## 🤝 Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Maintain a positive environment

## 📞 Getting Help

- **Issues**: Use GitHub issues for bugs and features
- **Discussions**: Use GitHub discussions for questions
- **Documentation**: Check the `/docs` directory

Thank you for contributing to AI Memory Palace! 🏛️