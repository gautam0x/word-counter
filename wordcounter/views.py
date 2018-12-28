from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    text = request.GET['stringtxt']
    wlist = text.split()

    worddict = {}

    for word in wlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    return render(request,'count.html',{'text':text,'wordcount':len(wlist),'worddict':worddict})
