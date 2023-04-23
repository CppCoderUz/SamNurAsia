from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import (
    IjtimoiyTarmoqlarSerializer,
    ArticleColumnSerializer,
    ArticleSerializer,
    JournalSerializer,
    PostSerializer,
)

from pages.models import (
    Eslatma,
    Icon,
    IjtimoiyTarmoqlar,
    Manzili,
    MaqolaJoylash,
    Narxlar
) 

from articles.models import (
    Article,
    ArticleColumn,
    Post,
    Journal,
)



def eslatma_api(request):
    return JsonResponse(Eslatma.as_dict())

def icon_api(request):
    return JsonResponse(Icon.as_dict())

def manzil_api(request):
    return JsonResponse(Manzili.as_dict())

def maqola_joylash_api(request):
    return JsonResponse(MaqolaJoylash.as_dict())

def narxlar_api(request):
    return JsonResponse(Narxlar.as_dict())

class IjtimoiyTarmoqlarAPI(ListAPIView):
    queryset = IjtimoiyTarmoqlar.objects.all()
    serializer_class = IjtimoiyTarmoqlarSerializer


class PostAllAPI(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPI(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class JournalAllAPI(ListAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

class JournalDetailAPI(RetrieveAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

class ArticleColumnAllAPI(ListAPIView):
    queryset = ArticleColumn.objects.all()
    serializer_class = ArticleColumnSerializer

class ArticleColumnDetailAPI(RetrieveAPIView):
    queryset = ArticleColumn.objects.all()
    serializer_class = ArticleColumnSerializer


class ArticleALLAPI(ListAPIView):
    queryset = Article.objects.filter(is_active=True)
    serializer_class = ArticleSerializer


class ArticleDetailAPI(RetrieveAPIView):
    queryset = Article.objects.filter(is_active=True)
    serializer_class = ArticleSerializer