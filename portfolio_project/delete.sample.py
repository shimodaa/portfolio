import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
from django import setup
setup()

from clothes.models import Outer,Inner, Coordinate,Favorite


# Coordinate.objects.id.32.delete()   

# Favorite.objects.all().delete()  

# Favorite.objects.filter(id=11).delete()
# Coordinate.objects.all().delete()   
Outer.objects.filter(id=25).delete()