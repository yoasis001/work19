from django.contrib import admin
from .models import Item, Review

admin.site.register(Item)

# @admin.register(Item)  # 아래 클래스가 Post 모델을 관리하는 클래스임
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'short_content',   # short content
#                     'tagged',                                   # tagged
#                     'updated',  # 'updated_at',
#                     ]
#     # 위에서 'author.username'으로 하면 'not a callable' 오류
#     # 위에서 'tags'로 하면 'must not be a ManyToManyField'라고 오류
#     list_display_links = ['id', 'title', ]
#     list_filter = ['created_at', 'updated_at',]
#     search_fields = ['title', 'content', ]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'item', 'message', 'updated', ]
    list_display_links = ['id', 'message', ]
