from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader
from .models import *

def blogindex(request):
	blog_list=Blog.objects.order_by('-timestamp')
	tag_list=Tag.objects.order_by('id')
	#output=','.join([q.question_text for q in latest_question_list])
	#template=loader.get_template('blogs/mytemplates.html')
	template=loader.get_template('blogs/fronttemplate.html')
	context={
		'blog_list':blog_list,
		'tag_list':tag_list,
	}
	return HttpResponse(template.render(context,request))
def blogsave(request,blog_id,tag_id):
	try:
	    blog=Blog.objects.get(pk=blog_id)
	except Blog.DoesNotExist:
		blog=Blog()
	blog.body=request.POST['body']
	if(request.POST['title']):
		blog.title=request.POST['title']
	else:
		blog.title='MyBlog'
	blog.tag_id=tag_id
	blog.save()
	print(blog.id)
	tag_list=Tag.objects.order_by('id')
	return render(request,'blogs/mypost.html',{'blog':blog,'tag_list':tag_list,'tag_id':tag_id})

def blogpost(request,blog_id,tag_id):
	blog=get_object_or_404(Blog,pk=blog_id)
	return render(request,'blogs/mypost.html',{'blog':blog,'tag_id':tag_id})
def blogedit(request,blog_id,tag_id):
	blog=get_object_or_404(Blog,pk=blog_id)
	tag_list=Tag.objects.order_by('id')
	return render(request,'blogs/edit.html',{'blog':blog,'tag_list':tag_list,'tag_id':tag_id})
def blogdelete(request,blog_id):
	#remove blog
	blog_list=Blog.objects.order_by('-timestamp')
	tag_list=Tag.objects.order_by('id')
	Blog.objects.filter(id=blog_id).delete()
	tag_list=Tag.objects.order_by('id')
	return render(request,'blogs/fronttemplate.html',{'blog_list':blog_list,
	'tag_list':tag_list})

def tagpost(request,tag_id):
	print ("=============================================================================================")
	blog_list=Blog.objects.filter(tag_id=tag_id)
	tag_list=Tag.objects.order_by('id')
#	print (blog_list)
	#print (tag_list)
	return render(request,'blogs/mytagposts.html',{'blog_list':blog_list,'tag_list':tag_list,'tag_id':tag_id})

def writepost(request,tag_id):
	blog=Blog()
	#blog.body=request.POST['body']
	#blog.title=request.POST['title']
	blog.tag=tag_id
	blog.save()
	tag_list=Tag.objects.order_by('id')
	return render(request,'blogs/edit.html',{'tag_list':tag_list,'tag_id':tag_id})

# Create your views here.
