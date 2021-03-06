from django.contrib import admin

# Register your models here.
 #from posts.models import Post
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","__unicode__","updated","timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated","timestamp"]
	search_fields = ["title","content"]
	class Meta:
		model=Post

admin.site.register(Post, PostModelAdmin)