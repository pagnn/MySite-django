from django.shortcuts import render,get_object_or_404

from .models import BlogArticles
# Create your views here.

def blog_title(request):
	articles=BlogArticles.objects.all()
	return render(request,'blog/title.html',{'object_list':articles})
def blog_content(request,article_id):
	article=get_object_or_404(BlogArticles,id=article_id)
	return render(request,'blog/content.html',{'object':article})