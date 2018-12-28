from django.shortcuts import render
import operator

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

    sortedworddict = sorted(worddict.items() , key=operator.itemgetter(1) ,reverse=True)

    return render(request,'count.html',{'text':text,'wordcount':len(wlist),'worddict':sortedworddict})
