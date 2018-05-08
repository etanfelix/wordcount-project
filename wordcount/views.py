from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = {}
    for word in fulltext.split():
        if word not in wordlist:
            wordlist[word] = 1
        else:
            wordlist[word] += 1
    sortedwords = sorted(wordlist.items(), key=operator.itemgetter(1), reverse=True)

    # You need to pass wordlist as list (of two values - see below) as the template expects
    # two values from wordlist during iteration
    # [('A', 3), ('B', 2), ('C', 1)]
    return render(request, 'count.html', {'fulltext': fulltext, 'ctr': len(fulltext.split()), 'sortedwords': sortedwords})
