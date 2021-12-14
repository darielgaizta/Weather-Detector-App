from django.shortcuts import render
from datetime import datetime
import urllib.request
import json

# Create your views here.
def index(request):
	if request.method == 'POST':
		city = request.POST['city'].capitalize()
		reqs = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=747d4b37f9dcceeab5b7a08995048ff4').read()
		resp = json.loads(reqs)
		data = {
			'city':city,
			'cc':str(resp['sys']['country']),
			'weather':str(resp['weather'][0]['main']),
			'desc':str(resp['weather'][0]['description']),
			'date':str(datetime.utcfromtimestamp(int(resp['dt'])).strftime('%Y-%m-%d %H:%M:%S')),
			'coordinate':str(resp['coord']['lon'])+' '+str(resp['coord']['lat']),
			'temp':str(resp['main']['temp']),
			'pressure':str(resp['main']['pressure']),
			'humidity':str(resp['main']['humidity'])
		}
	else:
		data = {}
	return render(request, 'index.html', data)