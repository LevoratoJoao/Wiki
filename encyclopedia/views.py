from django import forms
from django.shortcuts import render

from . import util
from markdown2 import Markdown

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=50)

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
        if searched == "":
            # Empty search
            entries = list(filter(lambda x: searched in x, util.list_entries()))
            return render(request, "encyclopedia/search.html", {
            "search": "",
            "entries": None
        })
        entry = util.get_entry(searched)
        if entry == None:
            # Show all the results with that search
            entries = list(filter(lambda x: searched in x, util.list_entries()))
            return render(request, "encyclopedia/search.html", {
            "search": searched,
            "entries": entries
        })
        # Redirect the user to the entry page
        htmlData = Markdown().convert(entry)
        return render(request, "encyclopedia/entry.html", {
        "data": htmlData,
        "titlePage": searched
    })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })