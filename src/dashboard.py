# Plotly Dash for interactive web dashboards
# Documentation: https://dash.plotly.com/
# Version: 2.14.2
from dash import Dash, html, dcc, Input, Output

# Plotly Express for data visualization
# Documentation: https://plotly.com/python/plotly-express/
# Version: 5.17.0
import plotly.express as px
import plotly.graph_objects as go

from .data_loader import load_and_anonymize_data
from .data_processor import OlympicAnalyzer
import os

# Skapa app med enhetlig design
app = Dash(__name__, external_stylesheets=['/assets/style.css'])
app.title = "Olympic Games Analysis"

# Ladda data
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'athlete_events.csv')
df = load_and_anonymize_data(data_path)
analyzer = OlympicAnalyzer(df)

# Layout - användarvänlig och enhetlig design
app.layout = html.Div([
    html.H1("Olympiska Spelen - Analys Dashboard", className='header'),
    
    # LAND-ANALYS SEKTION
    html.Div([
        html.H2("Uppgift 1: Landstatistik"),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': noc, 'value': noc} for noc in sorted(df['NOC'].unique())],
            value='CAN',  # Kanada
            className='dropdown'
        ),
        dcc.Graph(id='medals-by-sport'),
        dcc.Graph(id='medals-per-year'),
        dcc.Graph(id='age-histogram'),
        dcc.Graph(id='medal-types')
    ], className='section'),
    
    # SPORT-ANALYS SEKTION
    html.Div([
        html.H2("Uppgift 2: Sportstatistik"),
        dcc.Dropdown(
            id='sport-dropdown',
            options=[{'label': sport, 'value': sport} for sport in sorted(df['Sport'].unique())],
            value='Swimming',
            className='dropdown'
        ),
        dcc.Graph(id='sport-medals'),
        dcc.Graph(id='sport-ages'),
        dcc.Graph(id='sport-gender'),
        dcc.Graph(id='sport-medal-types')
    ], className='section')
    
], className='container')


# CALLBACKS - Interaktivitet
# Dash callback pattern for interactive updates
# Reference: Plotly Dash documentation - https://dash.plotly.com/basic-callbacks

@app.callback(
    [Output('medals-by-sport', 'figure'),
     Output('medals-per-year', 'figure'),
     Output('age-histogram', 'figure'),
     Output('medal-types', 'figure')],
    Input('country-dropdown', 'value')
)
def update_country_plots(country):
    """Uppdaterar alla land-specifika visualiseringar"""
    
    # Top sports
    top_sports = analyzer.top_sports_by_medals(country)
    fig1 = px.bar(
        x=top_sports.values, 
        y=top_sports.index,
        orientation='h', 
        color=top_sports.values,
        color_continuous_scale='viridis',  # Color-blind friendly palette - Plotly Express
        title=f'{country} - Top {len(top_sports)} sporter med flest medaljer',
        labels={'x': 'Antal medaljer', 'y': 'Sport'}
    )
    fig1.update_layout(showlegend=False)
    
    # Medals per Olympics
    medals_year = analyzer.medals_per_olympics(country)
    fig2 = px.line(
        x=medals_year.index, 
        y=medals_year.values,
        markers=True, 
        color=medals_year.values,
        color_continuous_scale='plasma',  # Color-blind friendly palette - Plotly Express
        title=f'{country} - Medaljer per OS',
        labels={'x': 'År', 'y': 'Antal medaljer'}
    )
    fig2.update_layout(showlegend=False)
    
    # Age histogram
    ages = analyzer.age_distribution(country)
    fig3 = px.histogram(
        ages, 
        nbins=30, 
        color_discrete_sequence=['#2A9D8F'],
        title=f'{country} - Åldersfördelning',
        labels={'value': 'Ålder', 'count': 'Antal idrottare'}
    )
    
    # Medal types
    medal_stats = analyzer.get_medal_statistics(country)
    fig4 = px.pie(
        values=medal_stats.values,
        names=medal_stats.index,
        title=f'{country} - Fördelning av medaljtyper',
        color_discrete_map={'Gold': '#FFD700', 'Silver': '#C0C0C0', 'Bronze': '#CD7F32'}
    )
    
    return fig1, fig2, fig3, fig4


@app.callback(
    [Output('sport-medals', 'figure'),
     Output('sport-ages', 'figure'),
     Output('sport-gender', 'figure'),
     Output('sport-medal-types', 'figure')],
    Input('sport-dropdown', 'value')
)
def update_sport_plots(sport):
    """Uppdaterar alla sport-specifika visualiseringar"""
    
    if not sport:
        # Returnera tomma figurer om ingen sport vald
        empty_fig = go.Figure()
        empty_fig.add_annotation(text="Välj en sport", showarrow=False)
        return empty_fig, empty_fig, empty_fig, empty_fig
    
    analysis = analyzer.sport_analysis(sport)
    
    # Medal distribution by country
    medal_countries = analysis['medal_countries'].head(10)
    fig1 = px.bar(
        x=medal_countries.values,
        y=medal_countries.index,
        orientation='h',
        title=f'{sport} - Medaljer per land (Top 10)',
        labels={'x': 'Antal medaljer', 'y': 'Land (NOC)'},
        color=medal_countries.values,
        color_continuous_scale='viridis'
    )
    fig1.update_layout(showlegend=False)
    
    # Age distribution
    age_dist = analysis['age_distribution']
    fig2 = px.histogram(
        age_dist, 
        nbins=25,
        title=f'{sport} - Åldersfördelning',
        labels={'value': 'Ålder', 'count': 'Antal idrottare'},
        color_discrete_sequence=['#E76F51']
    )
    
    # Gender split
    gender_split = analysis['gender_split']
    fig3 = px.pie(
        values=gender_split.values,
        names=gender_split.index,
        title=f'{sport} - Könsfördelning',
        color_discrete_map={'M': '#4ECDC4', 'F': '#FF6B6B'}
    )
    
    # Medal types
    medal_types = analysis['medal_types']
    fig4 = px.pie(
        values=medal_types.values,
        names=medal_types.index,
        title=f'{sport} - Fördelning av medaljtyper',
        color_discrete_map={'Gold': '#FFD700', 'Silver': '#C0C0C0', 'Bronze': '#CD7F32'}
    )
    
    return fig1, fig2, fig3, fig4


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)

