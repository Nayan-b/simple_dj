from django.shortcuts import render

from bs4 import BeautifulSoup
import requests
import urllib.request

# Create your views here.


def dictionary(request):
    isWord = False

    if request.method == 'POST':
        print(request.POST)
        isWord = True

        # get the word from the form
        word = request.POST['text']
        # get the url of the dictionary
        url = "https://www.vocabulary.com/dictionary/" + word
        htmlfile = urllib.request.urlopen(url)
        soup = BeautifulSoup(htmlfile, 'html.parser')
        soup1 = soup.find(class_="short")
        try:
            soup1 = soup1.get_text()
            shortText = soup1
        except AttributeError:
            shortText = "No definition found"
            # Print short meaning
            print('Cannot find such word! Check spelling.')

        # Print long meaning
        soup2 = soup.find(class_="long")
        try:
            soup2 = soup2.get_text()
            longText = soup2
        except AttributeError:
            longText = ''
            # Print instances like Synonyms, Antonyms, etc.
            print('Cannot find such word! Check spelling.')

        soup3 = soup.find(class_="instances")
        try:
            txt1 = soup3.get_text()
            synonymAntonym = ' '.join(txt1.split())
        except AttributeError:
            synonymAntonym = ' '
            print('Cannot find such word! Check spelling.')

        return render(request, 'dictionary/dictionary.html', {'word': word, 'shortText': shortText, 'longText': longText, 'synonymAntonym': synonymAntonym, 'isWord': isWord})

    else:
        return render(request, 'dictionary/dictionary.html')
