# from import は他のファイルから何かを少しずつ追加する行。
# 色々なファイルから必要な部分をコピペする代わりにこの関数を使う。
# 違いは、モジュール（.pyのファイル）の全体を利用するのがimport、モジュールの一部（変数や関数）を利用するのがfrom。
# 使うなら、「import単体」、または「from モジュール import モジュールの属性」の2パターンでいいのかな？
# 多分from単体だと、どこのモジュールのものか分からないから使えないと思う。
# 「from モジュール import モジュールの属性」で行けば、モジュールの属性が使えるってことかな？
from django.conf import settings
from django.db import models
from django.utils import timezone

# class Post(models.Model): – この行が今回のモデルを定義する。（これがオブジェクト）
# classはオブジェクトを定義することを示すキーワード。
# Postはモデルの名前であり、他の名前を付けることはできる（ただし、特殊文字と空白は避ける）モデルの文字は先頭大文字。
# そもそも、DjangoはMTV（モデル・テンプレート・ビュー）という設計手法が使われている。
# モデル；データベースとの連携を行う。該当ファイルはmodels.pyである。
# テンプレート；フロントエンド（HTML）を扱う。該当ファイルはtemplatesフォルダ内のhtmlファイル。
# ビュー；バックエンドを扱う。該当ファイルはviews.pyである。
# つまり、モデルとはWebアプリケーションとデータベースを連携させる仕組みのことで、データベースに格納されているデータにアクセスできる。ちなみに、クラスである。
# MTVのやり取りは以下のようになる。
# １；ユーザーがバックエンド側（views.py）にリクエスト
# ２；views.pyにきたデータをmodels.pyにリクエスト
# ３；受け取ったデータに対して返答をview.pyに受け渡す（返答を返す）。
# ４；受け渡されたデータをTemplateにHTML表示を要求する。
# ５；ブラウザに表示する。
# models.Modelはポスト（いわゆる、郵便ポストみたいなイメージ）がDjango Modelだという意味で、Djangoが、これはデータベースに保存すべきものだと分かるようにしている。
class Post(models.Model):
  # 以下プロパティの定義。
  # 「フィールド名 = models.フィールドの型(フィールドオプション)」の形で定義する。
  # フィールドとは、モデル定義で必ず１つ以上必要になる項目。
  # データベースでいうと、テーブル（Excelみたいな表、HTMLでいうtableタグ）のカラム（表の列）にある、Excelでいうセルみたいなデータの格納場所。ちなみに、表の行は「レコード」という。
  # フィールドはモデルクラスの属性として定義される。
  # データベースでいうテーブルはモデルにあたります。このモデルを通してデータベースの操作（追加、削除、更新など）を行う。
  # つまりDjangoでは、モデルを使うことでSQL文（CREATEやINSERT）を使わないでデータベース操作を可能にする。（？？？）
  # models.ForeignKey は他のモデルへのリンク
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  # models.CharField は 文字数が制限されたテキストを定義するフィールド
  title = models.CharField(max_length=200)
  # models.TextField は制限無しの長いテキスト用
  text = models.TextField()
  # models.DateTimeField は日付と時間のフィールド
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)
  
  def publish(self):
    self.published_date = timezone.now()
    self.save()
    
  def __str__(self):
    return self.title