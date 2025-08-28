from django.contrib import admin


from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "category", "subcategory", "created_at", "document")
	list_filter = ("category", "subcategory")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ("post", "author", "created_at")
