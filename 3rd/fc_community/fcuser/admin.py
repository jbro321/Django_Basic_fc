from django.contrib import admin
from .models import Fcuser

# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password') # 이름과 패스워드로 카테고리 나오게한다.

admin.site.register(Fcuser, FcuserAdmin)