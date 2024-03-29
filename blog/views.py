from django.shortcuts import render
from django.utils import timezone
# models の前にあるドットは カレントディレクトリ 、もしくは カレントアプリケーション のこと
# iews.pyと models.pyは、同じディレクトリに置いてあるから、ドット入れるだけで問題なし。
# そして、モデルの名前を指定してインポート（今回はPost）。
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.views import generic
from .models import Comment
from .forms import PostForm
# 知識の技
from .forms import CommentCreateForm
from django import forms


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
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.published_date = timezone.now()
      post.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = PostForm()
  return render(request, 'blog/post_edit.html', {'form': form})
  
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# 知識の技
# コメント投稿ページのビュー
class CommentCreate(generic.CreateView):
    """コメント投稿ページのビュー"""
    template_name = 'comment_form.html'
    model = Comment
    form_class = CommentCreateForm
 
#  フォームに入力された情報が正しい場合の処理
    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect('post:detail', pk=post_pk)
 
#  htmlテンプレートに渡すデータを定義
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context
      
      # 知識の技
def PostDetail(request, pk):
        """Article page"""
        detail = get_object_or_404(Post, pk=pk)
 
        context = {
          "detail": detail,
          "comments": Comment.objects.filter(target=detail.id)   #該当記事のコメントだけを渡します。
           }
        
      