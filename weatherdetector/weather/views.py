from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city'].capitalize()
        api_url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=imperial&appid=464c8282c801635fa9c8936bc645117b' 
        url = api_url.replace(' ', '%20')
        res = urllib.request.urlopen(url).read()
        json_data = json.loads(res)
        data = {
            'country_code' : str(json_data['sys']['country']),
            'coordinate' : str(json_data['coord']['lon']) + '' + str(json_data['coord']['lat']),
            'temperature' : str(json_data['main']['temp']) + ' F',
            'pressure' : str(json_data['main']['pressure']) + ' hPa',
            'humidity' : str(json_data['main']['humidity']) + '%',
            'sea_level' : str(json_data['main']['sea_level']) + ' hPa',
            'ground_level' : str(json_data['main']['grnd_level']) + ' hPa',
        }
    else:
        city = ''
        data = {}
    return render(request, 'templates/index.html', {'city': city, 'data': data})

def error_404(request, exception):
    return render(request, 'templates/404.html', status=404)

def error_500(request):
    return render(request, 'templates/404.html', status=500)