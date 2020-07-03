import secrets

from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.conf import settings as conf_settings

from .models import *


def indexView(request):

    if request.method == 'GET':

        template = loader.get_template('shortener/index.html')
        return HttpResponse(template.render(None, request))

    elif request.method == 'POST':
        
        url_token = secrets.token_urlsafe(8)
        url_collation = UrlСollation(token=url_token, base_url=request.POST['link'])
        url_collation.save()

        return redirect('statView', url_token=url_token)


def statView(request, url_token):

    if request.method == 'GET':

        url_collations = UrlСollation.objects.filter(token=url_token)
        
        if not len(url_collations):
           raise Http404('Ссылки не существует')

        url_collation = url_collations[0]

        template = loader.get_template('shortener/view_link.html')
        context = {
            'original_link': url_collation.base_url,
            'short_link': '{!s}{!s}'.format(conf_settings.DOMAIN_NAME, url_collation.token),
        }
        return HttpResponse(template.render(context, request))


def redirectView(request, url_token):

    if request.method == 'GET':

        url_collations = UrlСollation.objects.filter(token=url_token)
        
        if not len(url_collations):
           raise Http404('Ссылки не существует')

        url_collation = url_collations[0]

        return redirect(url_collation.base_url)
