from django.shortcuts import render
from django.http  import HttpResponse,  HttpResponseRedirect
from . import util
from django.urls import reverse
from difflib import get_close_matches
from django.conf import settings
import os.path
from . import forms



def index(request):
    if request.method== "POST":
        search_form= forms.SearchForm(request.POST)

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
        "search_form": forms.SearchForm()
    })




def display_content (request, title):
    content=util.get_entry(title)
    if content is None:
        return render (request, "encyclopedia/error.html", {"title": title})
    else:
        return render (request, "encyclopedia/content.html", {"content":content, "title":title})
    

def create_new_page (request):
    if request.method=="POST":
        newpagedata = forms.NewPage(request.POST)
        
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

    return render (request, "encyclopedia/createnewpage.html",{"newpage_form": forms.NewPage()})


def edit_page(request, title):
    initial_data = {'edit_discription':util.get_entry(title)}
    if request.method=="POST":
        edit_page_data = forms.EditPage(request.POST)

        if edit_page_data.is_valid():
            edit_discription=edit_page_data.cleaned_data["edit_discription"]
            editpagefile = open(os.path.join(settings.BASE_DIR, 'entries', f"{title}.md"), "w")
            editpagefile.write(edit_discription)
            editpagefile.close()
            return render(request, "encyclopedia/content.html", {"title": title, "content":edit_discription})

        else:
            HttpResponse ("Error")


    return render(request, "encyclopedia/editpage.html", {"editpage_form": forms.EditPage(initial=initial_data)})
