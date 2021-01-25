from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
import random
import markdown2

from . import util


entries = util.list_entries()
title_random = random.choice(entries)

def index(request):
    entries = util.list_entries()
    title_random = random.choice(entries)
    return render(request, "encyclopedia/index.html", {
        "entries": entries, "title_random": title_random
    })

def entry(request, title):
    entries = util.list_entries()
    title_random = random.choice(entries)
    if not util.get_entry(title):
        return render(request, "encyclopedia/error.html", {
            "message": "page doesn't exist", "title_random":title_random
        })
    entry = markdown2.markdown(util.get_entry(title))
    return render(request, "encyclopedia/page.html", {
        "entry": entry, "title": title, "title_random":title_random
    })
    

def search(request):
    if request.method =="POST":
        title=request.POST.get("q")
        entries = util.list_entries()
        
        if not util.get_entry(title):
            title= title.lower()
            results =[] 
            for entry in entries:
                if title in entry.lower():
                    results.append(entry)
            return render(request, "encyclopedia/search_results.html", {
                "title": title,  "title_random":title_random, "entry": entry, "results": results
            })
                #else:
                    #return render(request, "encyclopedia/error.html", {
                    #"message": "page doesn't exist", "title_random":title_random
                    #})
        return render(request, "encyclopedia/page.html", {
            "entry": util.get_entry(title), "title": title, "title_random": title_random
        })

def add(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html", {
            "title_random": title_random
        })
    if request.method == "POST":
        title = request.POST.get("title")
        if title in util.list_entries():
            return render(request, "encyclopedia/error.html", {
                "message": "page already exists"
            })
        else:
            content=request.POST.get("content")
            util.save_entry(title, content)
            return render(request, "encyclopedia/page.html", {
            "title": title, "entry": util.get_entry(title), "title_random": title_random
            })



def edit(request, title):
    
    if request.method =="GET":
        
        content = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/edit.html", {
            "entry": content , "title": title,"title_random":title_random 
        })
    if request.method =="POST":
        content=request.POST.get("content")
        util.save_entry(title, content)
        return render(request, "encyclopedia/page.html", {
            "title": title, "entry": util.get_entry(title), "title_random":title_random
            })







        

    

    