from django.contrib import admin
from fruits.models import Fruit

# Register your models here.
class FruitAdmim(admin.ModelAdmin):
    list_display = ('name', 'category', 'fresh_fruit', 'quant', 'value' )
    search_fields = ('name',)

admin.site.register(Fruit,FruitAdmim)
