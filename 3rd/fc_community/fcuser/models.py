from django.db import models

# Create your models here.


class Fcuser(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, #dttm은 데이트타임의 약자
                                           verbose_name='등록시간')

    class Meta: #테이블명 직접 지정
        db_table = 'fastcampus_fcuser'
        