from django.contrib import admin
from myApp.models import *
# Register your models here.

class customUserAdmin(admin.ModelAdmin):
    
    list_display = ['id','username','email', 'user_type']
    search_fields =['id','username','email', 'user_type']
    
    fieldsets = [
            (
                "User Dashboard",
                {
                    "fields": ["username", "email", "password","user_type","first_name","last_name","profile_pic",],
                },
            ),
            
        ]
admin.site.register(customUser,customUserAdmin)
admin.site.site_header="Preskool | Manoj Gain"
admin.site.site_title="Preskool | Manoj Gain"
admin.site.index_title = 'Manoj Gain' 