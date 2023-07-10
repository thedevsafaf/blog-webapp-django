from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.utils import timezone
from django.urls import reverse
from articles.functions import generate_form_errors
import json
from django.core.paginator import Paginator
from articles.models import Article, NewsLetter
from articles.forms import NewsLetterForm


def articles(request):
    # queryset
    blog_list = Article.objects.all().order_by('posted_on')
    # recent 3 posts
    recent_post = Article.objects.order_by('-posted_on')[:3]
    form = NewsLetterForm()

    # pagination
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('pg')
    blog_list = paginator.get_page(page)

    # context
    context = {
        "blog_list": blog_list,
        "recent_post": recent_post,
        "form": form,
    }
    return render(request, 'home.html', context)


def article(request, pk):
    # queryset
    article = get_object_or_404(Article.objects.filter(pk=pk))

    # context
    context = {
        "article": article,
    }
    return render(request, 'detail.html', context)


def newsletter(request):
    if request.method == "POST":
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()

            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Email Successfully Submitted."
            }
        else:
            message = generate_form_errors(form, formset=False)

            response_data = {
                "status": "false",
                "stable": "true",
                "title": "Form validation error",
                "message": str(message)
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        return HttpResponse("Invalid Request")
