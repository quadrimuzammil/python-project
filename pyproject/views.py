from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, "index.html")
def about(request):
    temp = request.GET.get('text', 'default')
    chec = request.GET.get('removepunc', 'default')
    upp = request.GET.get('uppercase', 'default')
    # print(temp)
    # print(chec)
    # print(upp)
    strings = ""
    if chec == "on" or upp =="on":
        for i in temp:
            if i not in ["!","@","#","$",";","%","^","&","*","(",")","{","}","[","]"]:
                strings += i
        if upp == "on":
            temp = strings.upper
            # print(temp)
            param = {"name":temp}
            return render(request, "analysepage.html", param)
        else:
            param = {"name":strings}
            return render(request, "analysepage.html",param)
    
    else:     
        return render(request, "error.html")
