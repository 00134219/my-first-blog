from django.contrib import admin
# models.pyをimport
from .models import Post

# モデルをadminページ（管理画面）上で見えるようにするため、以下のコマンドが必要。
admin.site.register(Post)


# Register your models here.
