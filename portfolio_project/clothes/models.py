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



class Coordinate(models.Model):
    
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=10000, blank=True)
    description = models.CharField(max_length=100)
    outer = models.FileField(upload_to='picture/',default='')
    inner = models.FileField(upload_to='picture/',default='')
    pants = models.FileField(upload_to='picture/',default='')
    shoes = models.FileField(upload_to='picture/',default='')
    create_at = models.DateTimeField(default=timezone.now) 
    update_at = models.DateTimeField(default=timezone.now)
         
    class Meta:
     db_table = 'coordinate'
     
    def save(self, *args, **kwargs):
        if not self.name:  # もしnameが空ならば
            # 最後のレコードのid + 1 をnameに設定
            last_id = Coordinate.objects.all().order_by('-id').first().id if Coordinate.objects.exists() else 0
            self.name = str(last_id + 1)
        super().save(*args, **kwargs)
     
class Outer(models.Model):
    
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    outer = models.FileField(upload_to='picture/',default='')
    coordinate = models.ForeignKey(Coordinate, on_delete=models.SET_NULL, null=True, blank=True,related_name='outers')
    create_at = models.DateTimeField(default=timezone.now) 
    update_at = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'outer'
        
class Inner(models.Model):
    
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    inner = models.FileField(upload_to='picture/',default='')
    coordinate = models.ForeignKey(Coordinate, on_delete=models.SET_NULL, null=True, blank=True,related_name='inners')
    create_at = models.DateTimeField(default=timezone.now) 
    update_at = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'inner'
        
class Pants(models.Model):
    
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    pants = models.FileField(upload_to='picture/',default='')
    coordinate = models.ForeignKey(Coordinate, on_delete=models.SET_NULL, null=True, blank=True,related_name='pantss')
    create_at = models.DateTimeField(default=timezone.now) 
    update_at = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'pants'

class Shoes(models.Model):
    
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    shoes = models.FileField(upload_to='picture/',default='')
    coordinate = models.ForeignKey(Coordinate, on_delete=models.SET_NULL, null=True, blank=True,related_name='shoess')
    create_at = models.DateTimeField(default=timezone.now) 
    update_at = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'shoes'

    
class Favorite(models.Model):
    
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    outer = models.FileField(upload_to='picture/',default='')
    inner = models.FileField(upload_to='picture/',default='')
    pants = models.FileField(upload_to='picture/',default='')
    shoes = models.FileField(upload_to='picture/',default='')
    coordinate = models.ForeignKey(Coordinate, on_delete=models.SET_NULL, null=True, blank=True,related_name='favorites')
    create_at = models.DateTimeField(default=timezone.now) 
    update_at = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'favorite'
     
     
     

    
    

    

        
