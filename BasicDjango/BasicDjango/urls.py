from django.conf.urls import include, url
import HelloDjangoApp.views

# ルーティングの設定
urlpatterns = [
    url(r'^$', HelloDjangoApp.views.index, name='index'),
    url(r'^home$', HelloDjangoApp.views.index, name='home'),
    url(r'^about$', HelloDjangoApp.views.about, name='about'),
]
