from django.contrib import admin

# Register your models here.

# here to display the models


from django.contrib import admin

from . import models


class NotesAdmin(admin.ModelAdmin):
    list_display = ('title','text')


admin.site.register(models.Notes, NotesAdmin)
