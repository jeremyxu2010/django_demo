import os

import django

from django_demo import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings.__name__)
django.setup()