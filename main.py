import pandas as pd
import plotly.express as px
import dash
import plotly.graph_objs as go
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

df_2015 = pd.read_csv('2015.csv')
df_2016 = pd.read_csv('2016.csv')
df_2017 = pd.read_csv('2017.csv')
df_2018 = pd.read_csv('2018.csv')
df_2019 = pd.read_csv('2019.csv')

common_countries = set(df_2015['Country']) & set(df_2016['Country']) & set(df_2017['Country']) & set(df_2018['Country or region']) & set(df_2019['Country or region'])

# Filter the datasets to retain only the common countries
df_2015 = df_2015[df_2015['Country'].isin(common_countries)]
df_2016 = df_2016[df_2016['Country'].isin(common_countries)]
df_2017 = df_2017[df_2017['Country'].isin(common_countries)]
df_2018 = df_2018[df_2018['Country or region'].isin(common_countries)]
df_2019 = df_2019[df_2019['Country or region'].isin(common_countries)]

# For 2015 dataset
df_2015.rename(columns={
    "Country": "Country or Region",
    "Happiness Rank": "Happiness Rank",
    "Happiness Score": "Happiness Score",
    "Economy (GDP per Capita)": "Economy (GDP per Capita)",
    "Family": "Family",
    "Health (Life Expectancy)": "Health (Life Expectancy)",
    "Freedom": "Freedom",
    "Trust (Government Corruption)": "Trust (Government Corruption)",
    "Generosity": "Generosity",
    "Dystopia Residual": "Dystopia Residual"
}, inplace=True)

# Remove the Region and Standard Error columns for 2015 dataset
df_2015.drop(columns=['Region', 'Standard Error'], inplace=True)

# Reorder the columns in the 2015 file
df_2015 = df_2015[['Country or Region', 'Happiness Rank', 'Happiness Score', 'Economy (GDP per Capita)',
                   'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)',
                   'Generosity', 'Dystopia Residual']]

# For 2016 dataset
df_2016.rename(columns={
    "Country": "Country or Region",
    "Happiness Rank": "Happiness Rank",
    "Happiness Score": "Happiness Score",
    "Economy (GDP per Capita)": "Economy (GDP per Capita)",
    "Family": "Family",
    "Health (Life Expectancy)": "Health (Life Expectancy)",
    "Freedom": "Freedom",
    "Trust (Government Corruption)": "Trust (Government Corruption)",
    "Generosity": "Generosity",
    "Dystopia Residual": "Dystopia Residual"
}, inplace=True)

# Remove the Region, Lower Confidence Interval, and Upper Confidence Interval columns
df_2016.drop(columns=['Region', 'Lower Confidence Interval', 'Upper Confidence Interval'], inplace=True)

# Reorder the columns in the 2016 file
df_2016 = df_2016[['Country or Region', 'Happiness Rank', 'Happiness Score', 'Economy (GDP per Capita)',
                   'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)',
                   'Generosity', 'Dystopia Residual']]

# For 2017 dataset

# Rename the columns in the 2017 file
df_2017.rename(columns={
    "Country": "Country or Region",
    "Happiness.Rank": "Happiness Rank",
    "Happiness.Score": "Happiness Score",
    "Economy..GDP.per.Capita.": "Economy (GDP per Capita)",
    "Health..Life.Expectancy.": "Health (Life Expectancy)",
    "Trust..Government.Corruption.": "Trust (Government Corruption)",
    "Dystopia.Residual": "Dystopia Residual"
}, inplace=True)

# Remove the Whisker.high and Whisker.low columns
df_2017.drop(columns=['Whisker.high', 'Whisker.low'], inplace=True)

# Reorder the columns
df_2017 = df_2017[['Country or Region', 'Happiness Rank', 'Happiness Score', 'Economy (GDP per Capita)',
                   'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)',
                   'Generosity', 'Dystopia Residual']]

# For 2018 dataset

df_2018.rename(columns={'Country or region': 'Country or Region',
                        'Score': 'Happiness Score',
                        'GDP per capita': 'Economy (GDP per Capita)',
                        'Overall rank': 'Happiness Rank',
                        'Healthy life expectancy': 'Health (Life Expectancy)',
                        'Freedom to make life choices': 'Freedom'}, inplace=True)

# Remove columns
df_2018.drop(['Social support', 'Perceptions of corruption'], axis=1, inplace=True)

# Calculate the average values for Family, Trust, and Dystopia Residual
avg_family_values_2018 = (df_2015.groupby('Country or Region')['Family'].mean() +
                     df_2016.groupby('Country or Region')['Family'].mean() +
                     df_2017.groupby('Country or Region')['Family'].mean()) / 3

avg_trust_values_2018 = (df_2015.groupby('Country or Region')['Trust (Government Corruption)'].mean() +
                    df_2016.groupby('Country or Region')['Trust (Government Corruption)'].mean() +
                    df_2017.groupby('Country or Region')['Trust (Government Corruption)'].mean()) / 3

avg_dystopia_values_2018 = (df_2015.groupby('Country or Region')['Dystopia Residual'].mean() +
                       df_2016.groupby('Country or Region')['Dystopia Residual'].mean() +
                       df_2017.groupby('Country or Region')['Dystopia Residual'].mean()) / 3

# Fill the new columns with the average values based on country names
df_2018['Family'] = df_2018['Country or Region'].map(avg_family_values_2018)
df_2018['Trust (Government Corruption)'] = df_2018['Country or Region'].map(avg_trust_values_2018)
df_2018['Dystopia Residual'] = df_2018['Country or Region'].map(avg_dystopia_values_2018)

# Reorder columns in the 2018 file
df_2018 = df_2018[['Country or Region', 'Happiness Rank', 'Happiness Score',
                   'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)',
                   'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']]

# For 2019 dataset

df_2019.rename(columns={'Country or region': 'Country or Region',
                        'Score': 'Happiness Score',
                        'GDP per capita': 'Economy (GDP per Capita)',
                        'Overall rank': 'Happiness Rank',
                        'Healthy life expectancy': 'Health (Life Expectancy)',
                        'Freedom to make life choices': 'Freedom'}, inplace=True)

# Remove columns in the 2019 file
df_2019.drop(['Social support', 'Perceptions of corruption'], axis=1, inplace=True)

# Calculate the average values for Family, Trust, and Dystopia Residual
avg_family_values_2019 = (df_2015.groupby('Country or Region')['Family'].mean() +
                     df_2016.groupby('Country or Region')['Family'].mean() +
                     df_2017.groupby('Country or Region')['Family'].mean() +
                     df_2018.groupby('Country or Region')['Family'].mean()) / 4

avg_trust_values_2019 = (df_2015.groupby('Country or Region')['Trust (Government Corruption)'].mean() +
                    df_2016.groupby('Country or Region')['Trust (Government Corruption)'].mean() +
                    df_2017.groupby('Country or Region')['Trust (Government Corruption)'].mean() +
                    df_2018.groupby('Country or Region')['Trust (Government Corruption)'].mean()) / 4

avg_dystopia_values_2019 = (df_2015.groupby('Country or Region')['Dystopia Residual'].mean() +
                       df_2016.groupby('Country or Region')['Dystopia Residual'].mean() +
                       df_2017.groupby('Country or Region')['Dystopia Residual'].mean() +
                       df_2018.groupby('Country or Region')['Dystopia Residual'].mean()) / 4

# Fill the new columns with the average values based on the 'Country or Region' column
df_2019['Family'] = df_2019['Country or Region'].map(avg_family_values_2019)
df_2019['Trust (Government Corruption)'] = df_2019['Country or Region'].map(avg_trust_values_2019)
df_2019['Dystopia Residual'] = df_2019['Country or Region'].map(avg_dystopia_values_2019)

# Reorder columns
df_2019 = df_2019[['Country or Region', 'Happiness Rank', 'Happiness Score',
                   'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)',
                   'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']]

# Add a "Year" column to each dataframe
df_2015['Year'] = 2015
df_2016['Year'] = 2016
df_2017['Year'] = 2017
df_2018['Year'] = 2018
df_2019['Year'] = 2019

# Concatenate all the dataframes into one
data = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019])

# Reset index after concatenation
data.reset_index(drop=True, inplace=True)

# Part of the dash

# List of countries for dropdown options
countries = data['Country or Region'].unique()

# Geographical Happiness Map
fig_map = px.choropleth(data, locations="Country or Region", locationmode="country names",
                        color="Happiness Score", hover_name="Country or Region",
                        animation_frame="Year", projection="natural earth",
                        title="World Happiness Report - Happiness Scores by Country (2015-2019)")

# Bubble Chart of Happiness vs. GDP
fig_bubble = px.scatter(data, x='Economy (GDP per Capita)', y='Happiness Score',
                        size='Happiness Score', color='Country or Region',
                        title='World Happiness Report - Happiness vs GDP Bubble Chart')

# Define the factors to plot over the years
factors = ['Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)',
           'Freedom', 'Generosity', 'Trust (Government Corruption)']

# Factors Contributing to Happiness Line Chart
fig_factors = px.line(data, x='Year', y=factors, color_discrete_map = {'Economy (GDP per Capita)': 'blue',
                                                                        'Family': 'green',
                                                                        'Health (Life Expectancy)': 'red',
                                                                        'Freedom': 'orange',
                                                                        'Generosity': 'purple',
                                                                        'Trust (Government Corruption)': 'brown'},
                      title='Factors Contributing to Happiness Over the Years')

# Calculate the correlation matrix
correlation_matrix = data[['Happiness Score', 'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']].corr()

# Correlation Heatmap
fig_heatmap = go.Figure(data=go.Heatmap(
    z=correlation_matrix.values,
    x=correlation_matrix.columns,
    y=correlation_matrix.columns,
    colorscale='Viridis_r',
    colorbar=dict(title='Correlation'),
))

fig_heatmap.update_layout(title='Correlation Heatmap')

# Filter data for the specified countries
countries_in_our_region = ['Armenia', 'Georgia', 'Iran', 'Russia', 'Turkey', 'Azerbaijan']
filtered_data = data[data['Country or Region'].isin(countries_in_our_region)]

# Filter data for Armenia
armenia_df = data[data['Country or Region'] == 'Armenia']

# Define options for dropdown
axis_options = [
    {'label': 'Happiness Score', 'value': 'Happiness Score'},
    {'label': 'Economy (GDP per Capita)', 'value': 'Economy (GDP per Capita)'},
    {'label': 'Family', 'value': 'Family'},
    {'label': 'Health (Life Expectancy)', 'value': 'Health (Life Expectancy)'},
    {'label': 'Freedom', 'value': 'Freedom'},
    {'label': 'Trust (Government Corruption)', 'value': 'Trust (Government Corruption)'},
    {'label': 'Generosity', 'value': 'Generosity'},
    {'label': 'Dystopia Residual', 'value': 'Dystopia Residual'}
]

# Find the country with the highest Happiness Score for each year
max_happiness_countries = data.loc[data.groupby('Year')['Happiness Score'].idxmax()]

external_stylesheets = ['http://your-external-assets-folder-url/']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H1("World Happiness Report Visualizations"),

    html.Hr(),  # Horizontal line separator
    html.Hr(),  # Horizontal line separator

    html.H2("Country Specific Dashboard"),

    # Dropdown for selecting a country
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value=countries[0],
        style={'width': '50%'}
    ),

    html.Div(id='country-dashboard'),

    html.Hr(),  # Horizontal line separator

    html.H2("Geographical Happiness Map:"),
    dcc.Graph(figure=fig_map),

    html.Hr(),  # Horizontal line separator

    html.H2("Bubble Chart of Happiness vs GDP:"),
    dcc.Graph(figure=fig_bubble),

    html.Hr(),  # Horizontal line separator

    html.H2("Factors Contributing to Happiness - Line Chart:"),
    dcc.Graph(figure=fig_factors),

    html.Hr(),  # Horizontal line separator

    html.H2("Correlation Heatmap - Factors with Happiness Score"),
    dcc.Graph(
        id='correlation-heatmap',
        figure=px.imshow(correlation_matrix, color_continuous_scale='viridis_r',
                         title='Correlation Heatmap of Factors with Happiness Score')
        .update_layout(width=800, height=600)
    ),

    html.Hr(),  # Horizontal line separator

    html.H2("Happiness Score by selected countries and years"),

    dcc.Graph(id='graph-with-slider'),
        dcc.Slider(
            min=filtered_data['Year'].min(),
            max=filtered_data['Year'].max(),
            step=None,
            value=filtered_data['Year'].min(),
            marks={str(year): str(year) for year in filtered_data['Year'].unique()},
            id='year-slider'
        ),

    html.Hr(),  # Horizontal line separator

    html.H2("Happiness Score by selected countries and years"),

    dcc.Graph(id='line-chart'),
        dcc.Checklist(
            options=[{'label': country, 'value': country} for country in countries_in_our_region],
            value=countries_in_our_region,
            id='country-selector', style={'color': 'black'}
        ),

    html.Hr(),  # Horizontal line separator

    html.H2("Indicators for Armenia"),

    dcc.Dropdown(
                id='axis-dropdown',
                options=axis_options,
                value='Happiness Score'
            ),
            dcc.Graph(id='bar-plot'),

    html.Hr(),  # Horizontal line separator

    html.H2("Happiness Score for the Country with the Highest Score Each Year"),

    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in max_happiness_countries['Year']],
        value=max_happiness_countries['Year'].iloc[0]
    ),
    html.Div(id='cards-container', className='row')

])


@app.callback(
    Output('country-dashboard', 'children'),
    Input('country-dropdown', 'value')
)
def display_country_dashboard(selected_country):
    # Filter data for the selected country
    country_data = data[data['Country or Region'] == selected_country]

    # Figures for scores, factors contributing to happiness, and trends over the years
    fig_scores = px.line(country_data, x='Year', y='Happiness Score', title='Happiness Scores Over the Years')
    fig_factors = px.line(country_data, x='Year', y=['Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)',
                                                     'Freedom', 'Generosity', 'Trust (Government Corruption)'],
                          title='Factors Contributing to Happiness Over the Years')

    # A summary dashboard for the selected country
    country_dashboard = html.Div([
        html.H2(f"Detailed Information for {selected_country}"),
        dcc.Graph(figure=fig_scores),
        dcc.Graph(figure=fig_factors)
    ])

    return country_dashboard

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value')
)
def update_figure(selected_year):
    filtered_year_data = filtered_data[filtered_data['Year'] == selected_year]

    fig = px.scatter(filtered_year_data, x="Economy (GDP per Capita)", y="Happiness Score",
                     color="Country or Region", hover_name="Country or Region",
                     size_max=30,
                     title=f'Happiness Score in {selected_year}')

    fig.update_traces(marker=dict(size=30, opacity=0.8), selector=dict(mode='markers'))

    fig.update_layout(transition_duration=500)

    return fig

@app.callback(
    Output('line-chart', 'figure'),
    Input('country-selector', 'value')
)
def update_line_chart(selected_countries):
    filtered_countries_data = filtered_data[filtered_data['Country or Region'].isin(selected_countries)]

    fig = px.line(filtered_countries_data, x='Year', y='Happiness Score',
                  color='Country or Region', title='Happiness Score Over Years')

    return fig

@app.callback(
    Output('bar-plot', 'figure'),
    Input('axis-dropdown', 'value')
)
def update_bar_plot(selected_axis):
    fig = px.bar(armenia_df, x='Year', y=selected_axis, title=f'{selected_axis} Trend for Armenia')
    return fig

@app.callback(
    Output('cards-container', 'children'),
    Input('year-dropdown', 'value')
)
def generate_card(selected_year):
    filtered_country = max_happiness_countries[max_happiness_countries['Year'] == selected_year]
    row = filtered_country.iloc[0]
    card = html.Div([
        html.Div([
            html.H2(f"Year: {row['Year']}"),
            html.H3(f"Country: {row['Country or Region']}"),
            html.P(f"Happiness Score: {row['Happiness Score']}")
        ], className='card')
    ])
    return card

if __name__ == '__main__':
    app.run_server(debug=True)