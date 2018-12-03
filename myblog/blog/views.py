from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Tag
import markdown
from comments.forms import CommentForm
from comments.models import Comment
from django.views.decorators.cache import cache_page
# Create your views here.


@cache_page(60 * 5)
def index(request):
    article_list = Article.objects.all().order_by("-created_time")
    return render(request, "blog/index.html", {
        "article_list": article_list,
    })


@cache_page(60 * 5)
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.increase_views()
    article.body = markdown.markdown(
        article.body,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
    form = CommentForm()
    comment_list = article.comment_set.all()
    context = {
        "article": article,
        "form": form,
        "comment_list": comment_list,
    }
    return render(request, "blog/detail.html", context=context)


@cache_page(60 * 5)
def archives(request, year, month):
    article_list = Article.objects.filter(
        created_time__year=year,
        created_time__month=month).order_by("-created_time")
    return render(request, "blog/index.html", {"article_list": article_list})


@cache_page(60 * 5)
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(
        category=cate).order_by("-created_time")
    return render(request, "blog/index.html", {"article_list": article_list})


@cache_page(60 * 5)
def tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    article_list = Article.objects.filter(tags=tag).order_by("-created_time")
    return render(request, "blog/index.html", {"article_list": article_list})


@cache_page(60 * 5)
def about(request):
    article_list = Article.objects.all().order_by("-created_time")
    return render(request, "blog/about.html", {
        "article_list": article_list,
    })
