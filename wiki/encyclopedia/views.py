from django.shortcuts import render
from django.http  import HttpResponse,  HttpResponseRedirect
from django import forms
from . import util
from django.urls import reverse


def index(request):
    if request.method== "POST":
        search_form= SearchForm(request.POST)

        if search_form.is_valid():
            search = search_form.cleaned_data["search"]
            return HttpResponseRedirect(reverse("encyclopedia:display_content", args = [search]))
        
        else:
            return HttpResponse ("Invalid")


    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "search_form": SearchForm()
    })




def display_content (request, title):
    title=title.capitalize()
    content=util.get_entry(title)
    context = {"content":content, "title":title}
    if content is None:
        return render (request, "encyclopedia/error.html", {"title": title})
    else:
        return render (request, "encyclopedia/content.html", context)
    


class SearchForm(forms.Form):
    search=forms.CharField(label="search")