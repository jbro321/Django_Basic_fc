from django.contrib import admin
from .models import Board

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',) # 이름과 패스워드로 카테고리 나오게한다.

admin.site.register(Board, BoardAdmin)