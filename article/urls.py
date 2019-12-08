from django.urls import path
from .import views
app_name='article'
urlpatterns = [
    # path函数将url映射到视图
    path('category/',views.category_list,name='category_list'),
    path('category/<name>/',views.sort_by_category,name='sort_by_category'),
    path('', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    # 写文章
    path('article-create/', views.article_create, name='article_create'),
    # 删除文章
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    # 更新文章
    path('article-update/<int:id>/', views.article_update, name='article_update'),
]