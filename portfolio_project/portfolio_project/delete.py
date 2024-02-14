import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
from django import setup
setup()

from clothes.models import Item

instance_to_delete = Item.objects.get(pk=1) 

instance_to_delete.delete()


# Item.objects.all().delete()