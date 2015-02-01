from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
		# Examples:
		# url(r'^blog/', include('blog.urls')),
		
		url(r'^$', 'Amper.views.home', name='home'),

		url(r'^admin/', include(admin.site.urls)),

		url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
		url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
		url(r'^products/', include('product.urls')),
		url(r'^shopping-cart/', include('shopping_cart.urls')),

		# generator

)

if settings.DEBUG :
  urlpatterns += patterns('',
  (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)