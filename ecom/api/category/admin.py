from atexit import register
from unicodedata import category
from django.contrib import admin
from api.category.models import category
# Register your models here.
admin.site.register(category)