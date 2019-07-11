from django.http import HttpResponse
from django.shortcuts import render 
import operator
def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = { }

    for i in wordlist:
        if i in worddictionary:
           #increment no  
            worddictionary[i] += 1
        else:   
            #add element 
            worddictionary[i] = 1


    sortedword =  sorted(worddictionary.items(), key=operator.itemgetter(1),reverse = True)        
    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist),'sortedword':sortedword})


def about(request):
    return render(request, 'about.html')