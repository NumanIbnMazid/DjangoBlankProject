import os

from django.core.asgi import get_asgi_application

# Development Config
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings.development')
# Production Config
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings.production')

application = get_asgi_application()
