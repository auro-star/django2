"""django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path  # favicon.ico
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView  # favicon.ico

from apps.blog.views import *

# favicon.ico
favicon_view = RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)

# 定制站点头部和标题
admin.site.site_title = '博客后台管理系统'  # 站点标题
admin.site.site_header = '博客后台管理系统'  # 站点头部

urlpatterns = [
                  re_path(r'favicon\.ico$', favicon_view),
                  re_path(r'favicon\.png$', favicon_view),
                  path('admin/', admin.site.urls),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('blog/', include('apps.blog.urls', namespace='blog')),
                  path(
                      'admin/password_reset/',
                      auth_views.PasswordResetView.as_view(),
                      name='admin_password_reset',
                  ),
                  path(
                      'admin/password_reset/done/',
                      auth_views.PasswordResetDoneView.as_view(),
                      name='password_reset_done',
                  ),
                  path(
                      'reset/<uidb64>/<token>/',
                      auth_views.PasswordResetConfirmView.as_view(),
                      name='password_reset_confirm',
                  ),
                  path(
                      'reset/done/',
                      auth_views.PasswordResetCompleteView.as_view(),
                      name='password_reset_complete',
                  ),

                  # 网站验证
                  path('root.txt', root),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
