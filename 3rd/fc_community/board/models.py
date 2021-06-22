from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128,
                                verbose_name='제목')
    contents = models.TextField(max_length=128, # textfield 길이제한없는 걸로 사용
                                verbose_name='내용')
    writer = models.ForeignKey('fcuser.Fcuser', # id로 연결하는 키
                                on_delete=models.CASCADE, verbose_name='작성자')
    registered_dttm = models.DateTimeField(auto_now_add=True, #dttm은 데이트타임의 약자
                                           verbose_name='등록시간')

    def __str__(self): #Fcuser의 이름을 이름으로 나오게 함
        return self.title

    class Meta: #테이블명 직접 지정
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글' # Fcuser 클래스를 '패스트캠퍼스'로 지정한다.
        verbose_name_plural = '패스트캠퍼스 게시글' # 기본적으로 복수형으로 나타난다. 's'가 붙어서 나오는걸 없애기
