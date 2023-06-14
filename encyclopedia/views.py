from django.shortcuts import render,redirect
import markdown2
from . import util
from django.core.handlers.wsgi import WSGIRequest



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        substring = [entry for entry in util.list_entries()]
        return render(request, "encyclopedia/search.html", 
            {"searched":searched,
             "substring":substring,
             "entry": markdown2.markdown(util.get_entry(searched))})
    
        
    
    
def editor(request, title):
    if "title" and "content" in request.GET:
        return save(request)
    
    if title in util.list_entries():
        return render(request, "encyclopedia/editor.html", {
            "title": title,
            "content": util.get_entry(title)
        })
    else:
        return render(request, "encyclopedia/editor.html", {
            "title": "New",
            "content": "# My page"
        })


def save(request: WSGIRequest):
    title = request.GET["title"]
    content = request.GET["content"]

    if request.POST:
        util.save_entry(title, content)
        return page(request, title)
    else:
        util.save_entry(title, content)
        return page(request, title) 

def new_page (request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if util.get_entry(title) is not None:
                return redirect("index", {
                     
                })
        else:
            util.save_entry(title,content)
            return render(request, "encyclopedia/new_page.html", {
                "title": title,
                "entry": markdown2.markdown(util.get_entry(title))
            })
    else:
        return render(request, "encyclopedia/new_page.html")


def page(request, page):
    page_entry = util.get_entry(page)
    page_html = markdown2.markdown(page_entry)

    return render(request, "encyclopedia/page.html", {
        "title": page,
        "entry": page_html
    })
