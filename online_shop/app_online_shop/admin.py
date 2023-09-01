from django.contrib import admin
from .models import OnlineShop

# Register your models here.

# создаем класс для отображения модели в панели администрирования
class OnlineShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_time', 'auction', 'image']
    list_filter = ['auction', 'created_time']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'user', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })

    )

    @admin.action(description='Убрать возможность торга')
    # request - запрос с сайта
    # queryset - набор объектов, к которым применится созданный метод
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    
# отображаем нашу модель в панели администрирования
admin.site.register(OnlineShop, OnlineShopAdmin)