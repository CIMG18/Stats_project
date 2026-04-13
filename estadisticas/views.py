from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from nba_api.stats.static import teams
import pandas as pd

from django.shortcuts import render
from nba_api.stats.static import teams
import pandas as pd

def home(request):
    # 1. Obtenemos todos los equipos de la NBA
    nba_teams = teams.get_teams()
    
    # 2. Lo convertimos a un DataFrame de Pandas para practicar
    df = pd.DataFrame(nba_teams)
    
    # 3. Lo pasamos a HTML
    tabla_html = df[['full_name', 'city', 'state']].to_html(classes='table table-striped')

    return render(request, 'index.html', {'tabla': tabla_html})
