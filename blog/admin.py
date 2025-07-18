from django.http import HttpResponse  
import csv  
from django.contrib import admin
from .models import *


# Custom Post admin class
class PostAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ("Post Information", {"fields": ["author", "category", "tag","title"]}),
        ("Content Section", {"fields": ["text", "image", "thumbnail_image"]}),
        ("Date Details", {"fields": ["created_date", "published_date"], "classes": ["collapse"]}),
         
    ]
    list_display = ["title", "author", "category", "published_date"]
    list_filter = ["author", "category", "published_date"]
    search_fields = ["title"]
    # prepopulated_fields = {"slug": ("title",)}
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected as CSV"

# Register only the Post model with custom admin
admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
