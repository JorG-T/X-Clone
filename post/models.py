from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class PostModel(models.Model):
    name = models.CharField('name', max_length=50, blank= False, null= False, db_index= True)
    body  = models.CharField('body', max_length=500, blank= False, null= False, db_index= True)
    image = CloudinaryField('image', blank = True, null = True, db_index = True)
    count = models.IntegerField('count', blank = True, default = 0)
    created_at = models.DateTimeField('created datetime', blank = True, auto_now_add = True) 
    updated_at = models.DateTimeField('updated datetime', blank = True, auto_now = True)

    