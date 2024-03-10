from django.db import models

from accounts.models import CustomUser

# # Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=100,null=True,blank=True)
    cat_image = models.ImageField(upload_to='category_pics/', null=True, blank=True)
    cat_description = models.TextField()
    is_listed = models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return self.cat_name

class Issues(models.Model):
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='reported_issues'
    )
    expert = models.ForeignKey(
        CustomUser, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='assigned_issues'
    )
    message = models.TextField()