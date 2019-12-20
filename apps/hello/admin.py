from django.contrib import admin

from .models import Greeting


class GreetingAdmin(admin.ModelAdmin):
    date_hierarchy = 'my_time'
    list_display = ('my_time',)
    search_fields = ('my_time',)
    list_filter = ('my_time',)


admin.site.register(Greeting, GreetingAdmin)

admin.site.site_title = "后台"
admin.site.site_header = "后台"
