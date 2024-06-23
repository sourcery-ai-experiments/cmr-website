"""
URL configuration for CMR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from home import views as home_views

urlpatterns = i18n_patterns(
    path('credits/', home_views.credits, name='credits'),
    path('news/', home_views.news, name='news'),
    path('layouts/', include('cmr_layouts.urls')),
    path('members/', include('members.urls')),
    path('accounts/', include('allauth.urls')),  # Required by `allauth`
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),
)

# Required by `django-debug-toolbar`
if not settings.TESTING:
    urlpatterns = [
        *urlpatterns,
        path('__debug__/', include('debug_toolbar.urls')),
    ]

# -- FOR DEV ONLY -- Required by `django-cms`
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# For PROD: https://docs.djangoproject.com/en/4.2/howto/static-files/
