from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]


admin.site.register(Article, ArticleAdmin)
