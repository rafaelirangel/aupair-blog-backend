from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    path('', include('post.urls')),
    path('', include('accounts.urls'))
    # path('', TemplateView.as_view(template_name='index.html')),
] # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


] 


# # This line of code appends a new URL pattern to the existing urlpatterns list in a Django web application.
# urlpatterns += [re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]


# # if settings.DEBUG:
# #     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)