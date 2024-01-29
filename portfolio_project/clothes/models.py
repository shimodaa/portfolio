from django.db import models
from django.urls import reverse_lazy
from accounts.models import Users
from datetime import datetime
from django.db import models, transaction
from django.utils import timezone


class BaseModel(models.Model):
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        abstract = True


# class ItemManager(models.Manager): #いると思う
#     def filter_by_outer(self, outer):
#         return self.filter(outer=outer).all()

    
class Coordinate(models.Model):
    
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    outer = models.FileField(upload_to='picture/',default='')
    inner = models.FileField(upload_to='picture/',default='')
    pants = models.FileField(upload_to='picture/',default='')
    shoes = models.FileField(upload_to='picture/',default='')
    create_at = models.DateTimeField(default=timezone.now) 
    update_at = models.DateTimeField(default=timezone.now)
         
    class Meta:
     db_table = 'coordinate'
    
    
class Item(models.Model):
    
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    outer = models.FileField(upload_to='picture/',default='')
    inner = models.FileField(upload_to='picture/',default='')
    pants = models.FileField(upload_to='picture/',default='')
    shoes = models.FileField(upload_to='picture/',default='')
    coordinate = models.ForeignKey(Coordinate, on_delete=models.SET_NULL, null=True, blank=True)
    create_at = models.DateTimeField(default=timezone.now) 
    update_at = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'item'
        
    # def get_absolute_url(self):
    #     return reverse_lazy('clothes:detail_item', kwargs={'pk': self.pk})
     # objects = ItemManager()


# def add_item(self, outer):
#         existing_item = self.outer.filter(id=outer.id).first()
#         if existing_item:
#             return