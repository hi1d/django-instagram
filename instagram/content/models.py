from typing import ContextManager
from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.


class Feed(models.Model):
    content = models.TextField()  # 글 내용
    image = models.TextField()  # 피드이미지
    profile_image = models.TextField()  # 프로필 이미지
    user_id = models.TextField()  # 글쓴이
    like_count = models.IntegerField()  # 좋아요 수
