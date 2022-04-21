from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
schema_view = get_schema_view(
    openapi.Info(
        title="Items API",
        default_version='v1',
        description="Описание проекта",
        terms_of_services="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="alexandrsgrusina@gmail.com"),
        license=openapi.License(name='')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('articles/', views.ArticleList.as_view()),
    path('articles/<int:pk>/', views.ArticleDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]

urlpatterns = format_suffix_patterns(urlpatterns)