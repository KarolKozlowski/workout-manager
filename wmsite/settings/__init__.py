import importlib
import os

# Choose settings variant via DJANGO_SETTINGS_ENV (dev|prod). Default: dev
env = os.environ.get("DJANGO_SETTINGS_ENV", "dev").lower()
module_name = f"wmsite.settings.{env}"

try:
    _module = importlib.import_module(module_name)
except Exception as exc:  # pragma: no cover - environment/config error
    raise ImportError(
        f"Could not import settings module '{module_name}': {exc}"
    ) from exc

# Copy only UPPERCASE attributes (Django settings convention) into this package
for _name in dir(_module):
    if _name.isupper():
        globals()[_name] = getattr(_module, _name)

__all__ = [n for n in globals().keys() if n.isupper()]
