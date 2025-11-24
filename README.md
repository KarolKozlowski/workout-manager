# Workout Manager

A Django REST API application for managing workout programs and exercises.

## Tech Stack

- **Framework**: Django 5.2.8 with Django REST Framework 3.15.0
- **Server**: Gunicorn 23.0.0
- **Database**: SQLite (default Django setup)
- **Python**: 3.12
- **Container**: Alpine-based Docker image
- **Dev Tools**: pytest, black, ruff, isort, pre-commit

## Architecture

The project consists of three Django apps:

1. **wmsite** - Main project configuration with split settings (base/dev/prod)
2. **wmapi** - REST API backend with ViewSets for CRUD operations
3. **wmapp** - Web frontend views with HTML templates

## Data Models

### Core Workout Models (wmapi)

- **Workout** - Main entity with name, description, duration, start/end datetime
- **WorkoutDay** - Days of week (0-6) linked to workout parts
- **WorkoutPart** - Workout sections (warmup, strength, stretching, cardio)
- **ExerciseInstance** - Specific exercise occurrences in workout parts
- **Set** - Individual sets with reps, weight, rest time

### Exercise Library Models

- **Exercise** - Exercise library with instructions, videos, images
- **BodyPart** - Lookup table for exercise body parts
- **Muscle** - Lookup table for target and secondary muscles
- **Equipment** - Lookup table for exercise equipment

## API Endpoints

REST API available at `/api/v1/` with the following endpoints:

- `/api/v1/workouts/` - Workout CRUD operations
- `/api/v1/workout-parts/` - Workout part management
- `/api/v1/workout-days/` - Workout day configuration
- `/api/v1/exercise-instances/` - Exercise instance tracking
- `/api/v1/exercises/` - Exercise library
- `/api/v1/body-parts/` - Body part lookup
- `/api/v1/muscles/` - Muscle lookup
- `/api/v1/equipments/` - Equipment lookup

All endpoints currently use `AllowAny` permissions.

## Frontend Views

- **Index** - Home page
- **Workout List** - Browse all workouts
- **Workout Detail** - View workout structure with days, parts, exercises, and sets
- **Exercise Detail** - View exercise information with instructions and related data

Views use Django templates with prefetch optimizations for efficient database queries.

## Development

### Setup

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run migrations
python manage.py migrate

# Run development server
python manage.py runserver
```

### Testing

```bash
pytest
```

### Code Quality

The project uses pre-commit hooks with:
- black (code formatting)
- ruff (linting)
- isort (import sorting)

```bash
pre-commit install
pre-commit run --all-files
```

## Docker

Build and run with Docker:

```bash
docker build -t workout-manager .
docker run -p 80:80 workout-manager
```

Or use the provided build script:

```bash
./build-n-serve.sh
```

## Project Structure

```
workout-manager/
├── wmsite/          # Django project settings
│   ├── settings/    # Split settings (base/dev/prod)
│   └── urls.py      # Main URL configuration
├── wmapi/           # REST API app
│   ├── models.py    # Data models
│   ├── serializers.py
│   ├── api.py       # ViewSets
│   └── urls.py
├── wmapp/           # Web frontend app
│   ├── views.py     # Template views
│   ├── templates/   # HTML templates
│   └── urls.py
├── templates/       # Shared templates
├── static/          # Static files
├── db/              # Database directory
└── manage.py        # Django management script
```

## License

[Add license information]
