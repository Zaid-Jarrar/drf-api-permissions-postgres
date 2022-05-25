from django.contrib import admin
from .models import Snack
# Register your models here.



class AdminSnack(admin.ModelAdmin):
    list_display = ('title', 'price', 'purchaser', 'timestamp', 'updated')
    # list_filter = ('purchaser', 'timestamp', 'updated')
    # search_fields = ('title', 'description')


admin.site.register(Snack, AdminSnack)