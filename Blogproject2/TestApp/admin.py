from django.contrib import admin
from TestApp.models import Post,Comment,Feedback
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=["title","slug","author","status","created","publish","updated","body"]
    list_filter=("status","created","author")
    search_fields=("title","body")
    prepopulated_fields={"slug":("title",)}
    raw_id_fields=("author",)
    ordering=["status","publish"]


class CommentAdmin(admin.ModelAdmin):
    list_display=["name","email","post","created","body","active"]
    search_fields=("email","name","body")
    list_filter=("active","created")


class FeedbackAdmin(admin.ModelAdmin):
    list_display=["name","phone","email","feedback"]

admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
