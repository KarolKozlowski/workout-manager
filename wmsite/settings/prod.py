from . import base as _base

# Copy only UPPERCASE settings from base to avoid wildcard import pollution
for _name in dir(_base):
    if _name.isupper():
        globals()[_name] = getattr(_base, _name)

# Production settings
DEBUG = False

# Require a secret key to be explicitly set in production.
if not globals().get("SECRET_KEY"):
    raise ValueError("The DJANGO_SECRET_KEY environment variable is not set.")

# Optionally tighten security defaults here for production deployments.
