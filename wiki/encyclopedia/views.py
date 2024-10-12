from django.shortcuts import render
from django.http  import HttpResponse,  HttpResponseRedirect
from django import forms
from . import util
from django.urls import reverse
from difflib import get_close_matches


def index(request):
    if request.method== "POST":
        search_form= SearchForm(request.POST)

        if search_form.is_valid():
            search = search_form.cleaned_data["search"]
            entries=util.list_entries()
            for entry in entries:
                if search.lower() == entry.lower():
                    return HttpResponseRedirect(reverse("encyclopedia:display_content", args = [search]))
                else:
                    return render(request, "encyclopedia/searchresults.html", {"close_matches":get_close_matches(search, entries)})
        
        else:
            return render (request, "encyclopedia/index.html", {"search_form": search_form})


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