from . import base as _base

# Copy only UPPERCASE settings from base to avoid wildcard import pollution
for _name in dir(_base):
    if _name.isupper():
        globals()[_name] = getattr(_base, _name)

# Development settings
DEBUG = True

# If no secret key is provided in env during development, generate one.
if not globals().get("SECRET_KEY"):
    from django.core.management.utils import get_random_secret_key

    SECRET_KEY = get_random_secret_key()
