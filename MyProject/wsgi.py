import os

from django.core.wsgi import get_wsgi_application

# Development Config
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings.development')
# Production Config
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings.production')

application = get_wsgi_application()
