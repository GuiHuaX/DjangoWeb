
# article/views.py

# 导入 HttpResponse 模块
from django.http import HttpResponse
# 引入redirect重定向模块
from django.shortcuts import render, redirect

# 导入数据模型ArticlePost
from .models import ArticlePost
# 引入ArticlePostForm表单类
from .forms import ArticlePostForm
# 引入User模型
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# 引入分页模块
from django.core.paginator import Paginator
# 引入 Q 对象
from django.db.models import Q
# 引入markdown模块
import markdown
# 消息通知
from notifications.signals import notify


# 类视图
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

class ArticleListView(ListView):
    # 上下文的名称
    context_object_name = 'articles'
    # 模板位置
    template_name = 'article/list.html'
    
    def get_queryset(self):
        """
        查询集
        """
        queryset = ArticlePost.objects.filter(title='Python')
        return queryset
        
    def get_context_data(self, **kwargs):
        # 获取原有的上下文
        context = super().get_context_data(**kwargs)
        # 增加新上下文
        context['order'] = 'total_views'
        return context   
        
 
class ArticleDetailView(DetailView):
    queryset = ArticlePost.objects.all()
    context_object_name = 'article'
    template_name = 'article/detail.html'
    
    def get_object(self):
        """
        获取需要展示的对象
        """
        # 首先调用父类的方法
        obj = super(ArticleDetailView, self).get_object()
        # 浏览量 +1
        obj.total_views += 1
        obj.save(update_fields=['total_views'])
        return obj


class ArticleCreateView(CreateView):
    model = ArticlePost

    fields = '__all__'
    # 或者只填写部分字段，比如：
    # fields = ['title', 'content']

    template_name = 'article/create_by_class_view.html'



# 视图函数
def article_list(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    
    # 初始化查询集
    article_list = ArticlePost.objects.all()
    
    # 搜索查询集
    if search:
        article_list = article_list.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    else:
        search = ''
    
    # 查询集排序
    if order == 'total_views':
        article_list = article_list.order_by('-total_views')
    
    # 每页显示#篇文章
    paginator = Paginator(article_list, 3)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 articles
    articles = paginator.get_page(page)

    context = { 
        'articles': articles, 
        'order': order,
        'search': search,
        }
    
    return render(request, 'article/list.html', context)


# 文章详情
def article_detail(request, id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=id)
    
    # 浏览量 +1
    article.total_views += 1
    article.save(update_fields=['total_views'])
    
    # 将markdown语法渲染成html样式
    md = markdown.Markdown(
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        # 目录扩展
        'markdown.extensions.toc',
        ]
    )
    article.body = md.convert(article.body)

    
    # 需要传递给模板的对象
    context = { 
        'article': article,
        'toc': md.toc 
        }
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)
    

# 写文章的视图
# 检查登录
@login_required(login_url='/userprofile/login/')
def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(request.POST, request.FILES)
        
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定目前登录的用户为作者
            new_article.author = User.objects.get(id=request.user.id)
            # 将新文章保存到数据库中
            new_article.save()
            
            # 通知 
            notify.send(
                request.user,
                recipient = request.user,
                verb = '更新了文章',
                target = new_article,       
                )
            
            # 完成后返回到文章列表
            return redirect("article:article_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = { 
            'article_post_form': article_post_form
            }
        # 返回模板
        return render(request, 'article/create.html', context) 
        
        
# 删文章
@login_required(login_url='/userprofile/login/')
def article_delete(request, id):
    # 根据 id 获取需要删除的文章
    article = ArticlePost.objects.get(id=id)
    # 调用.delete()方法删除文章
    article.delete()
    # 完成删除后返回文章列表
    return redirect("article:article_list")        
        
        
# 安全删除文章
@login_required(login_url='/userprofile/login/')
def article_safe_delete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        
        # 过滤非作者的用户
        if request.user != article.author:
            return HttpResponse("抱歉，你无权修改这篇文章。")
            
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许post请求")


# 更新文章
@login_required(login_url='/userprofile/login/')
def article_update(request, id):
    # 获取需要修改的具体文章对象
    article = ArticlePost.objects.get(id=id)
    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            article.title = request.POST['title']
            article.body = request.POST['body']
            
            if request.FILES.get('avatar'):
                article.avatar = request.FILES.get('avatar')
            
            article.save()
                  
            # 完成后返回到修改后的文章中。需传入文章的 id 值
            return redirect("article:article_detail", id=id)
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")

    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = { 
            'article': article, 
            'article_post_form': article_post_form 
            }
        # 将响应返回到模板中
        return render(request, 'article/update.html', context)










        
    