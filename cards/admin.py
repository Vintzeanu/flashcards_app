from django.contrib import admin

from . import models

class CardsAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Card, CardsAdmin)