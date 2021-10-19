from django.contrib import admin

from .models import Blog, Contact, Category

admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Category)
