from django.contrib import admin

from menu_app.models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'level', 'name', 'url', 'parent', 'full_url', 'parent_url')
    readonly_fields = ('parent_url', 'full_url')

    def save_model(self, request, obj, form, change):
        if obj.parent:
            obj.parent_url = obj.parent.url
            proc_obj = obj
            full_url = obj.url

            for _ in range(obj.level - 1):
                proc_obj = proc_obj.parent
                full_url = '/'.join([proc_obj.url, full_url])

            obj.full_url = full_url
        else:
            obj.full_url = obj.url
            obj.parent_url = ''
        super().save_model(request, obj, form, change)
