from django.urls import path
from .views import index, encouragement_view, forbidden_word_view

urlpatterns = [
    path('', index, name= 'index'),
    path('encouragement/', encouragement_view, name='encouragement_view'), #  励ましの言葉
    path('forbidden_word/', forbidden_word_view, name='forbidden_word'), # 禁句ワード登録
]