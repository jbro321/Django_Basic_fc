from django.db import models

# Create your models here.


class Fcuser(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, #dttm은 데이트타임의 약자
                                           verbose_name='등록시간')

    def __str__(self): #Fcuser의 이름을 이름으로 나오게 함
        return self.username

    class Meta: #테이블명 직접 지정
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자' # Fcuser 클래스를 '패스트캠퍼스'로 지정한다.
        verbose_name_plural = '패스트캠퍼스 사용자' # 기본적으로 복수형으로 나타난다. 's'가 붙어서 나오는걸 없애기
        
        