from django.db import models

# # Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=100,null=True,blank=True)
    cat_image = models.ImageField(upload_to='category_pics/', null=True, blank=True)
    cat_description = models.TextField()
    is_listed = models.BooleanField(default=True)

    def __str__(self):
        return self.cat_name
    