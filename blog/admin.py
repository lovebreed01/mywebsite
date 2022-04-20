from django.contrib import admin
from blog.models import (
	Post,
	Category,
	Comment,
	Music,
	Artist,
	Video,
	MusicCategory
	)
# Register your models here.
from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# creating admin class
class PostAdmin(SummernoteModelAdmin):
	# displaying posts with title slug and created time
	list_display = ('title', 'slug', 'body', 'author', 'created')
	list_filter = ("created",)
	search_fields = ['title', 'content']
	
	prepopulated_fields = {'slug': ('title', )}
	summernote_fields = ('body',)

# registering admin class
class MusicAdmin(SummernoteModelAdmin):
	list_filter = ("artist", "posted_on")
	search_fields = ["artist" , "name"]
	summernote_fields = ("content",)

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Music, MusicAdmin)
admin.site.register(Artist)
admin.site.register(Video)
admin.site.register(MusicCategory)

