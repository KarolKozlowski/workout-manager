# TODO

## In Progress
- [ ] Merge dev branch to main after tests pass
- [ ] Commit untracked files (migrations, resetdb.sh)

## CI/CD & DevOps
- [ ] Add GitHub Actions CI/CD pipeline
  - [ ] Automated tests on pull requests
  - [ ] Code quality checks (linting, formatting)
  - [ ] Build and push Docker images from main branch
- [ ] Set up automated deployments
- [ ] Add pre-commit hooks enforcement in CI

## Authentication & Security
- [ ] Add authentication/permissions (replace `AllowAny`)
- [ ] Implement token-based authentication (JWT or DRF tokens)
- [ ] Add role-based access control (admin, trainer, user)
- [ ] Add CORS configuration for frontend
- [ ] Audit API endpoints for security vulnerabilities

## Testing
- [ ] Expand test coverage for all ViewSets
- [ ] Add integration tests for complex workflows
- [ ] Add performance/load testing
- [ ] Add test fixtures/seed data for development
- [ ] Achieve >80% code coverage

## API Documentation
- [ ] Add Swagger/OpenAPI documentation (drf-spectacular)
- [ ] Document all endpoints with examples
- [ ] Add API versioning strategy
- [ ] Create API client libraries/SDKs

## Frontend & UX
- [ ] Build modern frontend (React/Vue.js)
- [ ] Improve HTML templates styling
- [ ] Add form validation and error handling
- [ ] Implement user dashboard/profile
- [ ] Add export functionality (PDF, CSV)

## Database & Data Management
- [ ] Add database backups strategy
- [ ] Implement data migrations for production
- [ ] Add database indexes for performance
- [ ] Create admin commands for data seeding
- [ ] Add soft deletes where appropriate

## Features
- [ ] User workout history and progress tracking
- [ ] Workout recommendations/templates
- [ ] Exercise video integration
- [ ] Social features (sharing, following)
- [ ] Mobile app (native or PWA)
- [ ] Notifications/reminders for workouts
- [ ] Analytics and statistics dashboard

## Code Quality
- [ ] Add comprehensive logging
- [ ] Improve error handling and validation
- [ ] Add type hints throughout codebase
- [ ] Refactor large functions/views
- [ ] Add more detailed code comments
- [ ] Create contributing guidelines

## Documentation
- [ ] Add API endpoint examples
- [ ] Create architecture documentation
- [ ] Write deployment guides
- [ ] Add development setup video/walkthrough
- [ ] Document database schema

## Performance
- [ ] Optimize database queries (add indexes)
- [ ] Implement caching (Redis)
- [ ] Add pagination to list endpoints
- [ ] Monitor query performance
- [ ] Optimize static file serving

## Monitoring & Logging
- [ ] Set up application logging
- [ ] Add error tracking (Sentry)
- [ ] Add performance monitoring
- [ ] Create health check endpoint
- [ ] Add request/response logging

## Deployment
- [ ] Set up staging environment
- [ ] Create production deployment checklist
- [ ] Add database migration strategy for production
- [ ] Configure environment-specific settings properly
- [ ] Add secrets management (environment variables, vaults)
