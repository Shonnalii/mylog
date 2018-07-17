from django.urls import path
from . import views,core_views

app_name='blogs'
urlpatterns=[
	path('',views.blogindex,name='home'),
	path('signup/', core_views.signup, name='signup'),
	path('blogno/<int:blog_id>/<int:tag_id>',views.blogedit,name='edit'),
	path('blogno/<int:blog_id>/',views.blogdelete,name='delete'),
	path('tag/<int:blog_id>/post/<int:tag_id>',views.blogpost,name='post'),
	path('<int:blog_id>/save/<int:tag_id>',views.blogsave,name='save'),
	path('tag/<int:tag_id>/',views.tagpost,name='tagpost'),
	path('writepost/<int:tag_id>',views.writepost,name='writepost'),
	#path(r'^site_media/(?P.*)$', 'django.views.static.serve', {'document_root': '/home/shopclues/myfirstproject/mysite/newproject/mysite/blogs/templates/blogs/media'}),
#	path('<int:question_id>/vote/', views.vote, name='vote'),
]
