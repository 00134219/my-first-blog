from django.shortcuts import render
from django.utils import timezone
# models の前にあるドットは カレントディレクトリ 、もしくは カレントアプリケーション のこと
# iews.pyと models.pyは、同じディレクトリに置いてあるから、ドット入れるだけで問題なし。
# そして、モデルの名前を指定してインポート（今回はPost）。
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

# Create your views here.

def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  # blog/post_list.html テンプレートを（色々なものを合わせて）組み立てる render という関数を呼び出して,
  # 得た値を return しています。
  # 最後のパラメータに注目すると {}と書かれているが、この中に指定した情報を、テンプレートが表示してくれる。
  # {} の中に引数を記述する時は、名前と値をセットにしなくてはなりません。
  # 注意して欲しいのは、シングルクォートです。 :（コロン） で区切られた、前の方の posts は、 
  # シングルクォート で囲まれて、'posts' になっていますよね。こちらが名前で、後ろの方の posts は値、クエリセットのこと.
  # クエリセットとは、モデルの中のオブジェクトのリストのこと。
  return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
  
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

