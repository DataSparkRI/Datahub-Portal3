from django.contrib import admin
from portal.models import FlatPageAddon
from django.contrib.flatpages.admin import FlatPage
from django.contrib.flatpages.forms import FlatpageForm
from django.utils.translation import gettext_lazy as _

class FlatPageAddonInline(admin.StackedInline):
    model = FlatPageAddon

#####@admin.register(FlatPage)
class FlatPageAdmin(admin.ModelAdmin):
    model = FlatPage
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': ('registration_required', 'template_name'),
        }),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'registration_required')
    search_fields = ('url', 'title')
    inlines = [FlatPageAddonInline]

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
#admin.site.register(FlatPage, FlatPageAdmin)
