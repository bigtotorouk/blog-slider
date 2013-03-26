# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Category,Post
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.views.generic.list_detail import object_list
from django.http import Http404
from django.shortcuts import get_list_or_404
import datetime
import logging
import someutils

# Get an instance of a logger
logger = logging.getLogger(__name__)
logger.addHandler(someutils.null_handler)

num_in_page = 5 # default num in one page, it's used in archive_year function

@login_required
def index(request):
    categorys = Category.objects.all()
    posts = Post.objects.filter().order_by('-created')
    now = datetime.datetime.now()

    #create a dict with the years and months:events
    post_dict = {}
    if posts:
        for i in range(posts[0].created.year, posts[len(posts)-1].created.year - 1, -1):
            post_dict[i] = {}
            for month in range(1,13):
                post_dict[i][month] = []
        for post in posts:
            post_dict[post.created.year][post.created.month].append(post)

    return render_to_response('blog/index.html', {
        'request':request,
        'now':now,
        'categorys':categorys,
        'posts':posts,
        'post_dict':post_dict,
        }
        )


def archive_year(request,year):
    # Pagination for the equivalent of archive_year generic view.
    # The URL is of the form http://host/2007/page/1/
    # urls.py,say, ('^blog/(?P<year>\d{4})/page/(?P<page>\d)/$',get_archive_year),
    queryset = get_list_or_404(Post, created__year=year)
    paginator = Paginator(queryset, num_in_page)   
    page = request.GET.get('page')
    try:
        post_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post_page = paginator.page(paginator.num_pages)
    return render_to_response('blog/archive_year.html', {"post_page": post_page,"request":request,},context_instance=RequestContext(request))


def post_view(request,postId):
    """docstring for blog_view"""
    post = Post.objects.get(id=postId)
    logger.error('Something went wrong!')
    return render_to_response('blog/blog_detail.html', {
        'post':post,'request':request,
        }, context_instance=RequestContext(request) 
    )
    
