#!/usr/bin/env python
# coding: utf-8

# In[69]:


#Importeren functies en vaststellen kleurschema
import plotly.express as px
import plotly.io as pio
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns
import ipywidgets as widgets
import plotly.graph_objects as go
import pandas as pd
import requests
import streamlit as st
from pandas import json_normalize


# In[43]:



color_map = ["cyan", "darkcyan", "cornflowerblue"] 
st.title('2022-2023 sem-1 Case 2: Blog')
st.header('Lego door de jaren heen')
st.subheader(' Team 7: Tuncay, Umut, Annika, Estelle') 

st.text('Welkom op onze pagina. Wij zijn vier studenten van de Hoogeschool van Amsterdam. Wij hebben de opdracht gekregen om een blog te maken over een zelf gekozen dataset.')
st.text('Wij hebben de dataset LEGO gekozen. Wij zetten alle leuke feitjes over de lego kleurtjes, themas en sets voor jouw op een rij.')
st.text('Wij leren jullie op een leuke manier om datasets te leren gebruiken aan de hand van de leukste dataset LEGO.' )
st.text ("Wij nemen jouw mee in het proces die wij hebben gedaan om achter deze feitjes te komen")
st.text('Ben jij je al nieuwsgierig geworden in de inzichten van de lego dataset? En hoe wij tot de weetjes zijn gekomen? ')
st.text("Lees maar snel verder en dan leren wij jouw eenn coole lego dataset bouwen" )     


# In[44]:


st.subheader('Stap 1 de dataset vormen ') 
st.text('We beginnen bij het begin, we lezen eerst via een API de gebruikte data sets in')
st.text('Daarvoor zijn bepaalde packages nodig om deze te instaleren, maar voordat we deze gebruiken is het nodig om te controleren of we API kunnen gebruiken.')
st.text('Dit doen we doormiddel van de response code.')
       
    


# In[85]:



#Controle of de gebruikte API's werken
import requests
import pandas as pd

#API: color
response_color = requests.get("https://rebrickable.com/api/v3/lego/colors/?key=1596f7b76482d264ab289aa7a9c16cb0")
print(f"Response code voor API 'color': {response_color.status_code}")

#API: sets
response_sets = requests.get("https://rebrickable.com/api/v3/lego/sets/?key=1596f7b76482d264ab289aa7a9c16cb0")
print(f"Response code voor API 'sets': {response_sets.status_code}")

#API: themes
response_themes= requests.get("https://rebrickable.com/api/v3/lego/themes/?key=1596f7b76482d264ab289aa7a9c16cb0")
print(f"Response code voor API 'themes': {response_themes.status_code}") 


# In[46]:


st.text('Top! Dit is gelukt. De 200 geeft aan dat de API goed is voor gebruik. Nu gaan we verder met de overige package importeren')
        


# In[ ]:





# In[47]:


st.header('Importeren van de API s &CSV bestanden')
st.text('Nu gaan we de API en de csv bestanden inlanden')


# In[86]:


# Importeren van de API's : color, sets, themes
url_colors ="https://rebrickable.com/api/v3/lego/colors/?key=1596f7b76482d264ab289aa7a9c16cb0"
url_sets = "https://rebrickable.com/api/v3/lego/sets/?key=1596f7b76482d264ab289aa7a9c16cb0"
url_themes = "https://rebrickable.com/api/v3/lego/themes/?key=1596f7b76482d264ab289aa7a9c16cb0"


# Doormiddel van package 'request' de url omzetten naar response: r
r_colors = requests.get(url_colors)
r_sets = requests.get(url_sets)
r_themes = requests.get(url_themes)


# Decode de JSON data naar een dictionary: json_data
#color
json_colors = r_colors.json()
df_colors = pd.json_normalize(json_colors,record_path=['results'])  # Maak van json een DataFrame
df_colors = pd.DataFrame(df_colors, columns=['id', 'name', 'rgb', 'is_trans'])
df_colors.drop(index=df_colors.index[0], # Haal de eerste rij weg, id=-1 en andere variabelen slaan nergens op
        axis=0,
        inplace=True)

#sets
json_sets = r_sets.json()
df_sets = pd.json_normalize(json_sets,record_path=['results']) # Maak van json een DataFrame
df_sets = pd.DataFrame(df_sets, columns=['set_num', 'name', 'year', 'theme_id', 'num_parts'])

#themes
json_themes = r_themes.json()
df_themes = pd.json_normalize(json_themes,record_path=['results']) # Maak van json een DataFrame
df_themes = pd.DataFrame(df_themes)

#Inladen overige csv waarvan API niet beschikbaar was: inventories, inventory, themes
df_inventories = pd.read_csv('inventories.csv')
df_inventory_parts = pd.read_csv('inventory_parts.csv')
df1_themes = pd.read_csv('themes.csv')
df_csv_sets = pd.read_csv('sets.csv')


# In[91]:


code1='''
# Importeren van de API's : color, sets, themes
url_colors ="https://rebrickable.com/api/v3/lego/colors/?key=1596f7b76482d264ab289aa7a9c16cb0"
url_sets = "https://rebrickable.com/api/v3/lego/sets/?key=1596f7b76482d264ab289aa7a9c16cb0"
url_themes = "https://rebrickable.com/api/v3/lego/themes/?key=1596f7b76482d264ab289aa7a9c16cb0"


# Doormiddel van package 'request' de url omzetten naar response: r
r_colors = requests.get(url_colors)
r_sets = requests.get(url_sets)
r_themes = requests.get(url_themes)


# Decode de JSON data naar een dictionary: json_data
#color
json_colors = r_colors.json()
df_colors = pd.json_normalize(json_colors,record_path=['results'])  # Maak van json een DataFrame
df_colors = pd.DataFrame(df_colors, columns=['id', 'name', 'rgb', 'is_trans'])
df_colors.drop(index=df_colors.index[0], # Haal de eerste rij weg, id=-1 en andere variabelen slaan nergens op
        axis=0,
        inplace=True)

#sets
json_sets = r_sets.json()
df_sets = pd.json_normalize(json_sets,record_path=['results']) # Maak van json een DataFrame
df_sets = pd.DataFrame(df_sets, columns=['set_num', 'name', 'year', 'theme_id', 'num_parts'])

#themes
json_themes = r_themes.json()
df_themes = pd.json_normalize(json_themes,record_path=['results']) # Maak van json een DataFrame
df_themes = pd.DataFrame(df_themes)

#Inladen overige csv waarvan API niet beschikbaar was: inventories, inventory, themes
df_inventories = pd.read_csv('inventories.csv')
df_inventory_parts = pd.read_csv('inventory_parts.csv')
df1_themes = pd.read_csv('themes.csv')
df_csv_sets = pd.read_csv('sets.csv')
'''
st.code(code1, language = 'python')


# In[49]:


st.header('CSV & API dataframes doormiddel functie merge samenvoegen') 



# In[95]:



#inventories(csv) + sets (api)
years = df_inventories.merge(df_sets, on='set_num')

#inventories (csv)+ sets(API) + themes(csv)
df_sets_themes = years.merge(df1_themes, how="left", left_on = ['theme_id'], right_on = ['id'], suffixes=('_sets', '_theme'))

#inventories (csv)+ sets(API) + themes(csv) + iventories_parts (csv)
df_sets_themes_parts = df_sets_themes.merge(df_inventory_parts, how="left", left_on = ['id_sets'], right_on = ['inventory_id'], suffixes=('_', '_parts'))

#inventories (csv)+ sets(API) + themes(csv) + iventories_parts (csv)+ colors (API)
df_totaal = df_sets_themes_parts.merge(df_colors, how="left", left_on = ['color_id'], right_on = ['id'], suffixes=('_', '_colour'))
df_totaal['date']=pd.to_datetime(df_totaal['year'], format="%Y")

# root_id is parent_id of theme_id, mocht er geen parent id zijn (kwaliteit dataset verbeteren)
df_totaal.parent_id = df_totaal.parent_id.fillna(value=df_totaal.id_theme)

#Voeg is_trans en kleur bij elkaar (kwaliteit dataset verbeteren)
df_totaal["is_transa"] = np.where(df_totaal["is_trans"]==True, '#TT' ,'#FF' )                  
df_totaal['rgba'] = df_totaal['rgb'] + df_totaal['is_transa']
df_totaal['rgba'] = df_totaal['rgb'] + df_totaal['is_transa']

#Vermenigvuldig de rows met de hoeveelheid quantity (kwaliteit dataset verbeteren)
df_totaal = df_totaal[df_totaal['quantity'].notna()]
df_totaal=df_totaal.loc[df_totaal.index.repeat(df_totaal.quantity)]

#Neem alleen nuttige data mee 
df_totaal = df_totaal[['set_num','name_sets','year','num_parts','name_theme','theme_id','parent_id','color_id','name','rgba','date','is_trans']]
df_totaal=df_totaal.reset_index()

#Creeren van de kolom count en date (kwaliteit dataset verbeteren)
df_totaal['count'] = df_totaal.index
df_totaal['date']=pd.to_datetime(df_totaal['year'], format="%Y")


#Schoone dataset:
st.text('Hieronder staat de gebruikte op geschoonde dataset.')
st.dataframe(df_totaal)
df_totaal
st.dataframe(df_totaal)


# In[96]:


code2= '''
#inventories(csv) + sets (api)
years = df_inventories.merge(df_sets, on='set_num')

#inventories (csv)+ sets(API) + themes(csv)
df_sets_themes = years.merge(df1_themes, how="left", left_on = ['theme_id'], right_on = ['id'], suffixes=('_sets', '_theme'))

#inventories (csv)+ sets(API) + themes(csv) + iventories_parts (csv)
df_sets_themes_parts = df_sets_themes.merge(df_inventory_parts, how="left", left_on = ['id_sets'], right_on = ['inventory_id'], suffixes=('_', '_parts'))

#inventories (csv)+ sets(API) + themes(csv) + iventories_parts (csv)+ colors (API)
df_totaal = df_sets_themes_parts.merge(df_colors, how="left", left_on = ['color_id'], right_on = ['id'], suffixes=('_', '_colour'))
df_totaal['date']=pd.to_datetime(df_totaal['year'], format="%Y")

# root_id is parent_id of theme_id, mocht er geen parent id zijn (kwaliteit dataset verbeteren)
df_totaal.parent_id = df_totaal.parent_id.fillna(value=df_totaal.id_theme)

#Voeg is_trans en kleur bij elkaar (kwaliteit dataset verbeteren)
df_totaal["is_transa"] = np.where(df_totaal["is_trans"]==True, '#TT' ,'#FF' )                  
df_totaal['rgba'] = df_totaal['rgb'] + df_totaal['is_transa']
df_totaal['rgba'] = df_totaal['rgb'] + df_totaal['is_transa']

#Vermenigvuldig de rows met de hoeveelheid quantity (kwaliteit dataset verbeteren)
df_totaal = df_totaal[df_totaal['quantity'].notna()]
df_totaal=df_totaal.loc[df_totaal.index.repeat(df_totaal.quantity)]

#Neem alleen nuttige data mee 
df_totaal = df_totaal[['set_num','name_sets','year','num_parts','name_theme','theme_id','parent_id','color_id','name','rgba','date','is_trans']]
df_totaal=df_totaal.reset_index()

#Creeren van de kolom count en date (kwaliteit dataset verbeteren)
df_totaal['count'] = df_totaal.index
df_totaal['date']=pd.to_datetime(df_totaal['year'], format="%Y")


#Schoone dataset:
st.text('Hieronder staat de gebruikte op geschoonde dataset.')
st.dataframe(df_totaal)
df_totaal
st.dataframe(df_totaal)
'''
st.code(code2,language='python')


# In[51]:


st.subheader('Stap 2: dataverkening op de dataset') 
st.text('Nu gaan we onderzoeken welke of de data die we nu hebben wel bruikbaar is. Dit doen wij doormiddel van een functie die zoekt naar missende waardes')
st.text('Hieruit blijkt dat we data missen in een paar kolomen')
st.text('Wij hebben er voor gekozen om deze data op te vullen met de waarde nul')
st.text('Dit hebben we gedaan om als nog bepaalde visualisatie te kunnen doen. Stel we hadden deze NA waardes weghaald, dan zouden we niet veel over bepaalde andere waardes kunnen zeggen.')


# In[55]:


#Hoeveel missende data is er?
missende_data = df_totaal.isnull().sum().sort_values(ascending=False)
print(missende_data)

#Missende data wegfilteren: df 
#df = df_totaal.dropna()
df = df_totaal.fillna(0)


# In[97]:


code3='''
#Hoeveel missende data is er?
missende_data = df_totaal.isnull().sum().sort_values(ascending=False)
print(missende_data)

#Missende data wegfilteren: df 
#df = df_totaal.dropna()
df = df_totaal.fillna(0)
st.code(code)
'''
st.code(code3,language='python')


# In[98]:


st.subheader('Importeer  CSV vs API  (kwaliteitskeuze)')


# In[62]:


col1, col2, = st.columns(2)

with col1:
    parts_by_year = df_sets[['year', 'num_parts']].groupby('year').mean().reset_index()

fig_p_y = px.scatter(parts_by_year, 
              x="year", 
              y="num_parts",
              labels={"year": "Jaar",
                      "num_parts": "Aantal onderdelen"},
              title='API: Gemiddeld aantal onderdelen per set over de jaren')
fig_p_y.show() 
st.plotly_chart(fig_p_y)

with col2: 

     parts_year = df_csv_sets[['year', 'num_parts']].groupby('year').mean().reset_index()

fig_p = px.scatter(parts_year, 
              x="year", 
              y="num_parts",
              labels={"year": "Jaar",
                      "num_parts": "Aantal onderdelen"},
              title='CSV: Gemiddeld aantal onderdelen per set over de jaren met')

fig_p.show()
st.plotly_chart(fig_p)


# In[99]:


#Importeren van visualisatie thema
import plotly.io as pio
pio.templates
pio.templates.default = "plotly_dark"
color_map = ["cyan", "darkcyan", "cornflowerblue"]


# ### Visualisaties

# In[65]:


#hoeveelheid parts uitgebracht in een jaar 
parts_by_year = df_sets[['year', 'num_parts']].groupby('year').mean().reset_index()

fig_g_y = px.line(parts_by_year, 
              x="year", 
              y="num_parts",
              labels={"year": "Jaar",
                      "num_parts": "Aantal onderdelen"},
              title='Gemiddeld aantal onderdelen per set over de jaren')
fig_g_y.show() 
st.plotly_chart(fig_g_y)


# ##### Sets: gemiddel aantal onderdel per set

# In[100]:


##sets
df_aantal_per_sets = pd.DataFrame(df['name_sets'].value_counts().sort_values(ascending=False))
#print(df_aantal_per_sets)


fig_bar = px.bar(df_aantal_per_sets, 
              x=df_aantal_per_sets.index, 
              y="name_sets",
              labels={"name_sets": "Aantal onderdelen",
                     'index': "Set"},
              title='Gemiddeld aantal onderdelen per set')
fig_bar.update_xaxes(tickangle=70)
fig_bar.show()
st.plotly_chart(fig_bar)


# ##### Thema: gemiddel aantal sets per thema

# In[71]:


#theme
df_aantal_sets_per_thema = pd.DataFrame(df['name_theme'].value_counts().sort_values(ascending=False))
#print(df_aantal_per_sets)


fig_bar_th = px.bar(df_aantal_sets_per_thema, 
              x=df_aantal_sets_per_thema.index, 
              y="name_theme",
              labels={"name_theme": "Aantal sets",
                     'index': "Thema"},
              title='Gemiddeld aantal sets per thema')
fig_bar_th.update_xaxes(tickangle=70)
fig_bar_th.show()
st.plotly_chart(fig_bar_th)


# ##### Color: gemiddel aantal blokjes per kleur

# In[73]:


##color
df_aantal_blokjes_per_kleur = pd.DataFrame(df['name'].value_counts().sort_values(ascending=False))
#print(df_aantal_blokjes_per_kleur)

fig_b_k = px.bar(df_aantal_blokjes_per_kleur, 
              x=df_aantal_blokjes_per_kleur.index, 
              y="name",
              labels={"name": "Aantal",
                     'index': "Kleur"},
              title='Gemiddeld aantal blokjes per kleur')
fig_b_k.update_xaxes(tickangle=70)
fig_b_k.show()
st.plotly_chart(fig_b_k)


# ### Slider:
# ### Aantal nieuwe legosets door de jaren heen

# In[78]:


df_sets['date']=pd.to_datetime(df_sets['year'], format="%Y")
df_sets["date"]=pd.to_numeric(df_sets['year'])

#print(df_sets)
fig_set, ax = plt.subplots(1,1,figsize=(25, 8))
sns.countplot(data= df_sets, x='year')
plt.xticks(rotation=90)
plt.title('Geschiedenis van Lego Sets')
plt.show()


df1_sets = df_sets.sort_values('date',ascending=True)
fig_set = px.bar(data_frame=df_sets,   
                 x='name',  
                 color='name',  
                 animation_frame="date"
            )

fig_set.update_layout({'yaxis': {'range': [0, 10]},'xaxis': {'range': [-1, 20]}})
fig_set['layout'].pop('updatemenus')
fig_set['layout']['sliders'][0]['pad']=dict(r= 10, t= 150,)

fig_set.update_layout(
    title="Aantal nieuwe legosets door de jaren heen",
    xaxis_title="Jaar",
    yaxis_title="Aantal sets",
    legend_title="Set")

fig_set.show()
st.plotly_chart(fig_set)


# ### Checkbox: 
# ### Hoeveelheid parts uitgebracht in een jaar is transparant wel of niet

# In[79]:


# df_colors['is_trans'].value_counts()
# transparent = df_colors['is_trans'] == 'True'
# non_transparent = df_colors['is_trans'] == 'False'

fig_part = px.bar(df, x="date", 
             color='is_trans', 
            barmode='group',
             labels={"count":"Aantal",
                    "date":"Jaar",
                    "is_trans":"Transparant"},
             title='Hoeveelheid parts per jaar per transparantie',
             height=700)

newnames = {'False':'Niet transparant', 'True': 'Wel transparant'}

fig_part.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     )
                  )

fig_part.show()
st.plotly_chart(fig_part)


# ### Dropdown menu:  
# ### Aantal blokjes per kleur per jaar

# In[84]:


# Maak de variabele per kleur de som van 
df_black = df[df["name"] == 'Black'].groupby('year').sum()['count'].reset_index()
df_blue = df[df["name"] == "Blue"].groupby('year').sum()['count'].reset_index()
df_brown = df[df["name"] == "Brown"].groupby('year').sum()['count'].reset_index()
df_dark_gray = df[df["name"] == "Dark Gray"].groupby('year').sum()['count'].reset_index()
df_green = df[df["name"] == "Green"].groupby('year').sum()['count'].reset_index()
df_milky_white = df[df["name"] == "Milky White"].groupby('year').sum()['count'].reset_index()
df_red = df[df["name"] == "Red"].groupby('year').sum()['count'].reset_index()
df_trans_clear = df[df["name"] == "Trans-Clear"].groupby('year').sum()['count'].reset_index()
df_trans_green = df[df["name"] == "Trans-Green"].groupby('year').sum()['count'].reset_index()
df_trans_light_blue = df[df["name"] == "Trans-Light Blue"].groupby('year').sum()['count'].reset_index()
df_trans_red = df[df["name"] == "Trans-Red"].groupby('year').sum()['count'].reset_index()
df_trans_yellow = df[df["name"] == "Trans-Yellow"].groupby('year').sum()['count'].reset_index()
df_white = df[df["name"] == "White"].groupby('year').sum()['count'].reset_index()
df_yellow = df[df["name"] == "Yellow"].groupby('year').sum()['count'].reset_index()


# Creeer de lijn
fig_drop = go.Figure()
z= fig_drop.add_trace(go.Scatter(x=df_black['year'], y=df_black["count"], mode='lines+markers', line_color='#5A5A5A', name='Zwart'))
b= fig_drop.add_trace(go.Scatter(x=df_blue['year'], y=df_blue["count"], mode='lines+markers', line_color='blue', name='Blauw'))
br= fig_drop.add_trace(go.Scatter(x=df_brown['year'], y=df_brown["count"], mode='lines+markers', line_color='#964B00', name='Bruin'))
dg= fig_drop.add_trace(go.Scatter(x=df_dark_gray['year'], y=df_dark_gray["count"], mode='lines+markers', line_color='gray', name='Donker grijs'))
g= fig_drop.add_trace(go.Scatter(x=df_green['year'], y=df_green["count"], mode='lines+markers', line_color='green', name='Groen'))
lb= fig_drop.add_trace(go.Scatter(x=df_trans_light_blue['year'], y=df_trans_light_blue["count"], mode='lines+markers', line_color=' #add8e6', name='Doorzichtig lichtblauw'))
r= fig_drop.add_trace(go.Scatter(x=df_trans_red['year'], y=df_trans_red["count"], mode='lines+markers', line_color=' #ffcccb', name='Doorzichtig rood'))
ty= fig_drop.add_trace(go.Scatter(x=df_trans_yellow['year'], y=df_trans_yellow["count"], mode='lines+markers', line_color='#ffffe0', name='Doorzichtig geel'))
w= fig_drop.add_trace(go.Scatter(x=df_white['year'], y=df_white["count"], mode='lines+markers', line_color='white', name='Wit'))
y= fig_drop.add_trace(go.Scatter(x=df_yellow['year'], y=df_yellow["count"], mode='lines+markers', line_color='yellow', name='Geel'))

# Creer de dropdownbutton per kleur
dropdown_buttons = [
{'label': "Alle kleuren", 'method': "update", 'args': [{"visible": [True,True,True, True, True, True, True, True,True,True]}, {'title': 'Aantal gemaakte blokjes per kleur door de jaren heen'}]},
{'label': "Zwart", 'method': "update", 'args': [{"visible": [True, False, False, False, False, False, False,False,False,False]}, {'title': 'Aantal gemaakte blokjes zwart door de jaren heen'}]},
{'label': "Blauw", 'method': "update", 'args': [{"visible": [False,True,False, False, False, False, False,False,False,False]}, {'title': 'Aantal gemaakte blokjes blauw door de jaren heen'}]},
{'label': "Bruin", 'method': "update", 'args': [{"visible":[ False,False,True, False, False, False, False, False,False,False]}, {'title': 'Aantal gemaakte blokjes bruin door de jaren heen'}]},
{'label': "Donker grijs", 'method': "update", 'args': [{"visible": [False,False,False, True, False, False, False, False,False,False]}, {'title': 'Aantal gemaakte blokjes grijs door de jaren heen'}]},
{'label': "Groen", 'method': "update", 'args': [{"visible": [False,False,False, False, True, False, False, False,False,False]}, {'title': 'Aantal gemaakte blokjes groen door de jaren heen'}]},
{'label': "Doorzichtig licht blauw", 'method': "update", 'args': [{"visible": [False,False,False, False, False, True, False, False,False,False]}, {'title': 'Aantal gemaakte blokjes zwart door de jaren heen'}]},
{'label': "Doorzicht rood", 'method': "update", 'args': [{"visible": [False,False,False, False, False, False, True, False,False,False]}, {'title': 'Aantal gemaakte blokjes doorzichtig blauw door de jaren heen'}]},
{'label': "Doorzichtig geel", 'method': "update", 'args': [{"visible": [False,False,False, False, False, False, False, True,False,False]}, {'title': 'Aantal gemaakte blokjes doorzichtig rood door de jaren heen'}]},
{'label': "Wit", 'method': "update", 'args': [{"visible": [False,False,False, False, False, False, False, False,True,False]}, {'title': 'Aantal gemaakte blokjes wit door de jaren heen'}]},
{'label': "Geel", 'method': "update", 'args': [{"visible": [False,False,False, False, False, False, False, False,False,True]}, {'title': 'Aantal gemaakte blokjes geel door de jaren heen'}]}
]

# Update het figuur en voeg de dropdownmenu toe
fig_drop.update_layout({
    'updatemenus':[{
            'type': 'dropdown',
            'x': 1.3, 'y': 1.2,
            'buttons': dropdown_buttons
            }]},
    title="Aantal blokjes per kleur per jaar",
    xaxis_title="Jaar",
    yaxis_title="Aantal blokjes",
    legend_title="Kleur")

# Show het figuur 
fig_drop.show()     
st.plotly_chart(fig_drop)


# In[ ]:




