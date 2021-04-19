from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())\
        .exclude(出荷日__lte=timezone.now() )\
        .order_by('c_date')
    page_obj  = paginate_queryset(request, posts, 5)
    context = {
        'posts': page_obj.object_list,
        'page_obj': page_obj,
    }
    #return render(request, 'unit/post_list.html', {'posts': posts})
    return render(request, 'unit/post_list.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'unit/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'unit/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'unit/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(Q(published_date__isnull=True) \
        | Q(published_date__gte=timezone.now())).order_by('p_no')
    page_obj  = paginate_queryset(request, posts, 5)
    context = {
        'posts': page_obj.object_list,
        'page_obj': page_obj,
    }
    return render(request, 'unit/post_draft_list.html', context)
 
def post_shipped_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())\
            .filter(出荷日__lte=timezone.now() )\
            .order_by('p_no')
    page_obj  = paginate_queryset(request, posts, 5)
    context = {
        'posts': page_obj.object_list,
        'page_obj': page_obj,
    }
    return render(request, 'unit/post_shipped_list.html', context)

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
    
def publish(self):
    self.published_date = timezone.now()
    self.save()

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def paginate_queryset(request, queryset, count):
    """Pageオブジェクトを返す。

    ページングしたい場合に利用してください。

    countは、1ページに表示する件数です。
    返却するPgaeオブジェクトは、以下のような感じで使えます。

        {% if page_obj.has_previous %}
          <a href="?page={{ page_obj.previous_page_number }}">Prev</a>
        {% endif %}

    また、page_obj.object_list で、count件数分の絞り込まれたquerysetが取得できます。

    """
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


