from django.shortcuts import render
from django.http  import HttpResponse,  HttpResponseRedirect
from django import forms
from . import util
from django.urls import reverse
from difflib import get_close_matches
from django.conf import settings
import os.path


def index(request):
    if request.method== "POST":
        search_form= SearchForm(request.POST)

        if search_form.is_valid():
            search = search_form.cleaned_data["search"]
            if util.get_entry(search) is not None:
                return HttpResponseRedirect(reverse("encyclopedia:display_content", args = [search]))
            else:
                return render(request, "encyclopedia/searchresults.html", {"close_matches":get_close_matches(search, util.list_entries())})


        else:
            return render (request, "encyclopedia/index.html", {"search_form": search_form})


    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "search_form": SearchForm()
    })




def display_content (request, title):
    content=util.get_entry(title)
    if content is None:
        return render (request, "encyclopedia/error.html", {"title": title})
    else:
        return render (request, "encyclopedia/content.html", {"content":content, "title":title})
    

def create_new_page (request):
    if request.method=="POST":
        newpagedata = NewPage(request.POST)
        
        if newpagedata.is_valid():
            title = newpagedata.cleaned_data["title"]
            description = newpagedata.cleaned_data["description"]

            if util.get_entry(title) is not None:
                return render (request, "encyclopedia/errornewpage.html", {"title": title})
            else:
                newpagefile = open(os.path.join(settings.BASE_DIR, 'entries', f"{title}.md"), "w")
                newpagefile.write(description)
                newpagefile.close()
                return render(request, "encyclopedia/content.html", {"title": title, "content": description})        

    return render (request, "encyclopedia/createnewpage.html",{"newpage": NewPage()})




class SearchForm(forms.Form):
    search=forms.CharField(label="search")


class NewPage (forms.Form):
    title=forms.CharField()
    description= forms.CharField()