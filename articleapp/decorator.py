from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = Article.objects.get(pk=kwrgs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated