from django.shortcuts import render
import random
import requests 
# Fro redirect
from django.http import HttpResponseRedirect
# fro reverse
from django.urls import reverse

from . import util



#Global entries Function
def MyEntries():
    entries_list = {"entries": util.list_entries()}
    for en in entries_list:
        entry = entries_list[en]
    
    return entry

#Global lower entries
def LowerEntries():
    entries_list = {"entries": util.list_entries()}
    e_low = []
    for en in entries_list:
        entry = entries_list[en]
        for e in entry:
            e_low.append(e.capitalize())
    
    return e_low 



def index(request):
        entry = MyEntries()

        return render(request, "encyclopedia/index.html",{
        "lists": entry,
        }
        )

#EDIT
def edit_page(request, name):
    #content = MyEntries
    content = util.get_entry(name)
    if request.method == 'POST':
        textEntry = request.POST.get('title')
        print(textEntry)
        contentEntry = request.POST.get('new_entry')
        print(contentEntry)
        util.save_entry(textEntry, contentEntry)

        return HttpResponseRedirect( reverse("encyclopedia:index"))

    return render(request, 'encyclopedia/edit.html',{
        "content": content,
        "name": name
    })



# Cearte a new page
def new_page(request):
    allEntries = MyEntries()
    name = 'Cearte Entry'
    if request.method == 'POST' and request.POST.get('title') != '':
        textEntry = request.POST.get('title').capitalize()
        contentEntry = request.POST.get('new_entry')

        try:
            error = textEntry

            if textEntry in allEntries:
                print('Yes is containe', textEntry)
                raise Exception('There the same entry!')
        except:
                return render(request, 'encyclopedia/info.html',{
                    "error": error,
                })

        util.save_entry(textEntry, contentEntry)

        return HttpResponseRedirect( reverse("encyclopedia:index"))

   
    return render(request, 'encyclopedia/info.html',{
        "name":name
    })



# Search bar
def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('search').capitalize()
        entry = MyEntries()
        empty = False

        # see if q containe first letter in the entries
        for q in entry:
            #Check if it more than 1 letter
            if q.startswith(query) and len(query) > 1:
                moreLetter = q
                
                return render(request,"encyclopedia/search_result.html",{
                "moreLetter": moreLetter,
                "entry": entry,        
                "query": query
                })

            elif q.startswith(query) and not query == '':
                print('PLEASE STRAT HERE!!!!')
                searchList = []
                s = query
                length  = len(entry)
                print("HERE LEN:", s, length)
                print(entry[0][0])

                for x in range(0, length):
                    if s == entry[x][0] and len(s) < 2:
                        d = entry[x]
                        searchList.append(d)

                print('IS MATCH:',searchList)
                return render(request,"encyclopedia/search_result.html",    {
                "list": searchList,
                "entries": entry,        
                "query": query
                })
            else:
                #Title based on the whole word!
                for qu in entry:
                    var = qu
                    print('VAR:', var) 
                    if var == query:
                        getTitle = util.get_entry(var)

                        return render(request,"encyclopedia/search.html",{
                        "query": query,        
                        "q": getTitle 
                    }) 
            
    return render(request,"encyclopedia/search_result.html",{
    "query": query,
    "entry": entry,
    "empty": empty        
    })


# Get a specific entry
def getPage(request, name):
   
    #entry = MyEntries()
    get = util.get_entry(name)
    
    return render(request, "encyclopedia/info.html",{
        "get": get,
        "name": name

    })

#Random 
def randomPage(request):
    entry = MyEntries()
    ran = random.choice(entry)
    get = util.get_entry(ran)
    name = get
    print(ran)

    return render(request, "encyclopedia/random.html",{
        "get": name,
        "name": ran,
        "title": ran,
        "content": get
    })



