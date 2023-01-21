from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    purpose=''       
    analyzed=""
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcounter=request.POST.get('charcounter','off')
    if(removepunc=='on'):
 
        punctuation='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed+char
        purpose+='|Removed Punctuation'
        djtext=analyzed
    if(fullcaps=='on'):
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
      
        purpose+='|Changed to Upper Case'
        djtext=analyzed
    if(spaceremover=='on'):
        analyzed=''
        for index,char in enumerate(djtext):
            if djtext[index]==' ' and djtext[index+1]==' ':
                continue
            else:
                analyzed=analyzed+char
        purpose+='|Extra space removed'
        djtext=analyzed
    if charcounter == 'on':
        analyzed=('No. of characters given in the text are : '+str(len(djtext)))
        purpose+='|Characers Counted'
        if(removepunc!='on'and fullcaps!='on' and spaceremover!='on' and charcounter!='on'):
            return HttpResponse("Error:No option selected")
    params = {'purpose': purpose, 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
