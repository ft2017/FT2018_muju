from django.contrib import admin

# Register your models here.
from .models import Muju,Muju_date111

# class Muju_date111Inline(admin.StackedInline):
#     model = Muju_date111
#     extra = 1

class MujuAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['muju_wo','muju_date','muju_empe','muju_source_code','muju_source_code_name','muju_plan_date','muju_seq','muju_Reason']}),
        # ('Date information', {'fields': ['muju_date']}),
    ]
    list_display = ('muju_wo', 'muju_date')
      
    # inlines = [Muju_date111Inline]
admin.site.register(Muju, MujuAdmin)

class Muju_date111Admin(admin.ModelAdmin):
	list_display = ('Muju','muju_date1', 'muju_date2',)
admin.site.register(Muju_date111,Muju_date111Admin)

# admin.site.register(Muju_date111)