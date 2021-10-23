from django.db import models
from django.core.validators import MaxLengthValidator

class Category(models.Model):
    lang_type = models.CharField(max_length=50)

    def __str__(self):
        return self.lang_type
        
    class Meta:
            db_table = 'categories'


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    web_site = models.URLField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blogs'


class Contact(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[MaxLengthValidator(100, '100文字以内で入力してください')])
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'contacts'