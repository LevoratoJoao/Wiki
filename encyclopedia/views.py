from django import forms
from django.shortcuts import render

from . import util
from markdown2 import Markdown

class NewPageText(forms.Form):
    title = forms.CharField(label="Tittle")
    text = forms.CharField(widget=forms.Textarea, label="Text")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, pk):
    entryContent = util.get_entry(pk)
    if entryContent == None:
        return render(request, "encyclopedia/error.html", {
            "pagePath": request.build_absolute_uri()
        })
    htmlContent = Markdown().convert(entryContent)
    return render(request, "encyclopedia/entry.html", {
        "data": htmlContent,
        "titlePage": pk
    })

def search(request):
    if request.method == "GET":
        searched = request.GET.get('q')
        entry = util.get_entry(searched)
        if searched != "":
            if entry != None:
                # Redirect the user to the entry page
                htmlData = Markdown().convert(entry)
                return render(request, "encyclopedia/entry.html", {
                    "data": htmlData,
                    "titlePage": searched
                })
            else:
                # Show all the results with that search
                entries = list(filter(lambda x: searched in x, util.list_entries()))
                return render(request, "encyclopedia/search.html", {
                    "search": searched,
                    "entries": entries
                })
        else:
            # Empty search
            return render(request, "encyclopedia/search.html", {
                "search": searched,
                "entries": None
            })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def create(request):
    if request.method == "POST":
        form = NewPageText(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            text = form.cleaned_data.get('text')
            searchEqual = list(filter(lambda x: title in x, util.list_entries()))
            if searchEqual == []:
                util.save_entry(title, text)
                return entry(request, title)
            else:
                return render(request, "encyclopedia/create.html", {
                "title": "Error",
                "form": form
            })
        else:
            return render(request, "encyclopedia/create.html", {
                "title": "Create New Page",
                "form": form
            })
    return render(request, "encyclopedia/create.html", {
        "title": "Create New Page",
        "form": NewPageText
    })

def random(request):
    return render(request, "encyclopedia/random.html", {
        "entries": util.list_entries()
    })