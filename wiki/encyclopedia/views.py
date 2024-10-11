from django.shortcuts import render
from django.http  import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def display_content (request, title):
    title=title.capitalize()
    content=util.get_entry(title)
    context = {"content":content, "title":title}
    if content is None:
        return render (request, "encyclopedia/error.html", {"title": title})
    else:
        return render (request, "encyclopedia/content.html", context)