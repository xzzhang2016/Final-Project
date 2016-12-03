# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import render

# from django.urls import reverse # future versions.
from django.core.urlresolvers import reverse_lazy


from os.path import join
from django.conf import settings


import numpy as np, pandas as pd
import matplotlib.pyplot as plt


from .forms import CountriesForm, VariablesForm
from .models import COUNTRIES_DICT, VARIABLES_DICT

import geopandas as gpd, folium


import seaborn as sns
sns.set(font_scale = 1.7)

from io import BytesIO


def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def project(request):
    return render(request,'project.html')

def datasource(request):
    return render(request,'datasource.html')

def factors(request):

    country = request.GET.get('country', 'China')

    filename = join(settings.STATIC_ROOT, 'myapp/merged.csv')

    df = pd.read_csv(filename)
    df = df[df["country"] == country]
    if not df.size: return HttpResponse("No data!")

    table = df.to_html(float_format = "%.5f", classes = "table table-striped", index = False)
    table = table.replace('border="10"','border="5"')
    table = table.replace('style="text-align: right;"', "")

    params = {'title' : country.title,
              'form_action' : reverse_lazy('myapp:factors'),
              'form_method' : 'get',
              'form' : CountriesForm({'country' : country}),
              'html_table' : table}


    return render(request, 'factors.html', params)



from .forms import VariablesForm
def view_pic(request, c="r"):

    variable = request.GET.get('variable', 'national income per capita')

    params = {'title' : variable.title,
              'form_action' : reverse_lazy('myapp:view_pic'),
              'form_method' : 'get',
              'form' : VariablesForm({'variable' : variable}),
              'pic_source' : reverse_lazy("myapp:plot", kwargs = {'c' : variable})}

    return render(request, 'view_pic.html', params)

def plot(request, c = "population density"):

    indicator = VARIABLES_DICT[c]

    filename = join(settings.STATIC_ROOT, 'myapp/merged.csv')

    df = pd.read_csv(filename)

    plt.figure() # needed, to avoid adding curves in plot
    lm = pd.ols(x=df[indicator], y=df['life expectancy'])
    plt.plot(df[indicator], df["life expectancy"],'ro', color = "blue")
    plt.plot(df[indicator], lm.y_fitted, 'r', linewidth=2)
    plt.tight_layout()
    plt.ylabel('life expectancy')
    plt.xlabel(indicator)
    plt.title( 'Regression between ' + 'life expectancy and '+ indicator, fontsize=15)

 # write bytes instead of file.
    from io import BytesIO
    figfile = BytesIO()

 # this is where the color is used.
    try: plt.savefig(figfile, format = 'png')
    except ValueError: raise Http404("No such color")

    figfile.seek(0) # rewind to beginning of file
    return HttpResponse(figfile.read(), content_type="image/png")


def view_map(request):
    filename= join(settings.STATIC_ROOT, 'myapp/life 2013.csv')
    a_df = pd.read_csv(filename,index_col = "Country")
    a_df["Numeric"] = a_df["Numeric"].astype(int)

    filename = join(settings.STATIC_ROOT, 'myapp/TM_WORLD_BORDERS_SIMPL-0.3.shp')

    geo_df = gpd.read_file(filename)

    geo_df.set_index("NAME",inplace = True)

    merged = geo_df.join(a_df, how = "left")
    merged = merged[merged['Numeric'] > 0]

    m = folium.Map([9, -10], tiles='cartodbpositron', zoom_start=2, max_zoom=14, min_zoom=2)

    ft = "Numeric"
    cmap = folium.colormap.linear.YlOrRd.scale(merged[ft].min(), merged[ft].max())

    folium.GeoJson(merged,
               style_function=lambda feature: {
                'fillColor': cmap(feature['properties'][ft]),
                'fillOpacity' : 0.8,
                'weight' : 2, 'color' : 'white'
               }).add_to(m)
    cmap.caption = 'World Life Expectancy (2013)'
    cmap.add_to(m)

    map_string = m._repr_html_().replace("width:100%;", "width:60%;float:right;", 1)

    return render(request, 'view_map.html', { "map_string" : map_string})
    
def change(request):
    filename= join(settings.STATIC_ROOT, 'myapp/change.csv')
    a_df = pd.read_csv(filename,index_col = "Country")
    a_df["Numeric"] = a_df["Numeric"].astype(int)

    filename = join(settings.STATIC_ROOT, 'myapp/TM_WORLD_BORDERS_SIMPL-0.3.shp')

    geo_df = gpd.read_file(filename)

    geo_df.set_index("NAME",inplace = True)

    merged = geo_df.join(a_df, how = "left")
    merged = merged[merged['Numeric'] > -50]

    m = folium.Map([9, -10], tiles='cartodbpositron', zoom_start=2, max_zoom=14, min_zoom=2)

    ft = "Numeric"
    cmap = folium.colormap.linear.YlOrRd.scale(merged[ft].min(), merged[ft].max())

    folium.GeoJson(merged,
               style_function=lambda feature: {
                'fillColor': cmap(feature['properties'][ft]),
                'fillOpacity' : 0.8,
                'weight' : 2, 'color' : 'white'
               }).add_to(m)
    cmap.caption = 'Living longer: from 2000 to 2013'
    cmap.add_to(m)

    map_string = m._repr_html_().replace("width:80%;", "width:70%;", 1)

    return render(request, 'change.html', {"title" : "Countries' Change in Life Expectancy from 2000 to 2013",
                                           "map_string" : map_string})
