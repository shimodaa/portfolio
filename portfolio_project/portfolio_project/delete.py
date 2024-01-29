import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
from django import setup
setup()

from clothes.models import Item

Item.objects.all().delete()