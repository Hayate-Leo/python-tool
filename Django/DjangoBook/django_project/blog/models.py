from django.db import models

class Blog(models.Model):
    LANG_TYPES = (
        ('py', 'Python'),
        ('js', 'Javascript'),
        ('css', 'CSS'),
        ('html', 'HTML'),
    )
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    lang_type = models.CharField(max_length=50, choices=LANG_TYPES, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blogs'

class Contact(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'contacts'