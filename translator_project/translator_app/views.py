from django.http import HttpResponse
from django.template import loader
import requests


def translate(request):
    
    if  request.method =='POST':
        text = request.POST.get('trans')
        print(text)

        url = f'https://api.mymemory.translated.net/get?q={text}&langpair=en|el'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            template = loader.get_template('translate.html')
            if 'translatedText' in data['responseData']:
                translated_text = data['responseData']['translatedText']                           
            else:
                translated_text = "Error! Unable to translate"
        else:
            translated_text = "error"
        
        context = {
                    'translated_text': translated_text,
                } 
        print(context)
        
        return HttpResponse(template.render(context, request)) 
    
    