"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from index import views as index_views
from user_profile import views as profile_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	url(r'^$',index_views.home,name='home'),
	url(r'^admin/', admin.site.urls),
	url(r'^signup/$',profile_views.signup, name='signupasuser'),
	# url(r'^register/$',index_views.signupasrest, name='signupasrest'),
    url(r'^restaurants/',include('rest_page.urls')),
	url(r'^login/$',auth_views.login,{'template_name':'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^user/$',profile_views.view_profile,name="view_profile"),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

