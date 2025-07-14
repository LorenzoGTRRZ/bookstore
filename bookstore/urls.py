# bookstore/urls.py
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

# Importe as novas views
from bookstore import views as bookstore_views # Importe sua views.py

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")), # Certifique-se de que está comentado ou removido para produção
    path("admin/", admin.site.urls),
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
    path("api-token-auth/", obtain_auth_token, name="api-token-auth"),

    # NOVAS ROTAS PARA O EXERCÍCIO DE DEPLOY AUTOMÁTICO:
   path("update_server/", bookstore_views.update, name="update_server"),  # Para o webhook
    path("hello/", bookstore_views.hello_world, name="hello_world"), # Para a página de sucesso
]