from django.contrib import admin
from .models import OurRecord


# Register your models here.
@admin.register(OurRecord)
class AdminOurRecord(admin.ModelAdmin):
    list_display = ('id','item','shop','price','time')


