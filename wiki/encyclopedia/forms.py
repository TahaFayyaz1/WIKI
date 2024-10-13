from django import forms



class SearchForm(forms.Form):
    search=forms.CharField(label="Search")


class NewPage (forms.Form):
    title=forms.CharField(label="Title")
    description= forms.CharField(label="Description", widget=forms.Textarea)


class EditPage (forms.Form):
    edit_discription= forms.CharField(label="Edit Description", widget=forms.Textarea)