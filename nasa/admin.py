from django.contrib import admin

from nasa.models import Nasa

# Register your models here.


@admin.register(Nasa)
class GenericAdmin(admin.ModelAdmin):

    list_display = ('title', 'due_data', 'kilometers',
                    'meters', 'miles', 'feet')
    list_filter = ('title', 'due_data')
    search_fields = ('title',)
