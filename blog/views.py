from django.shortcuts import render

# Create your views here.

def post_list(request):
  # blog/post_list.html テンプレートを（色々なものを合わせて）組み立てる render という関数を呼び出して,
  # 得た値を return しています。
  return render(request, 'blog/post_list.html', {})
