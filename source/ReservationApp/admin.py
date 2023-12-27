from django.contrib import admin
from .models import*
from django.contrib.admin import DateFieldListFilter
# Register your models here.

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    date_hierarchy = 'created_at'
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    list_display = ['name']
