from django.contrib import admin
from .models import internal_letter,external_letter

admin.site.register(internal_letter)
admin.site.register(external_letter)
