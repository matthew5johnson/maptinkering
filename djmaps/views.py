from django.shortcuts import render

# Create your views here.
def default_map(request):
	return render(request, 'default.html', {'mapbox_access_token': 'pk.eyJ1IjoiZ2VhdXhzaGVhdXgiLCJhIjoiY2pxcjI5MW5oMGlsYzQycWptMThqbm81cSJ9.MGGgmGzgWbUXqkTWjvK8uQ'})