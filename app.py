import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from html import unescape
from dash.exceptions import PreventUpdate

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# external_stylesheets = ['bootstrap.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# Load CSV file from Datasets folder
df1 = df2 = new_df = new_df2 = pd.read_csv('ForeignExchange.csv')

dfDecade = df1
dfDecade['Date'] = pd.to_datetime(dfDecade['Date'])
dfCurrentDecade = dfDecade[dfDecade['Date'].dt.year >= 2010]

dfYear = df1
dfYear['Date'] = pd.to_datetime(dfYear['Date'])
dfCurrentYear = dfYear[dfYear['Date'].dt.year == 2019]

new_df['Date'] = pd.to_datetime(new_df['Date'])

multiline_df = df1
trace1_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['AUSTRALIA - AUSTRALIAN DOLLAR/US$'], mode='lines',
                              name='AUSTRALIA - AUSTRALIAN DOLLAR/US$')
trace2_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['EURO AREA - EURO/US$'], mode='lines',
                              name='EURO AREA - EURO/US$')
trace3_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['NEW ZEALAND - NEW ZELAND DOLLAR/US$'],
                              mode='lines', name='NEW ZEALAND - NEW ZELAND DOLLAR/US$')
data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]

data_duoline = [trace1_multiline, trace2_multiline]

# Get the conversion rate for the currencies (most recent data)
df_aud = df1['AUSTRALIA - AUSTRALIAN DOLLAR/US$'].iloc[-1]
df_eur = df1['EURO AREA - EURO/US$'].iloc[-1]
df_nzd = df1['NEW ZEALAND - NEW ZELAND DOLLAR/US$'].iloc[-1]
df_gbp = df1['UNITED KINGDOM - UNITED KINGDOM POUND/US$'].iloc[-1]
df_brl = df1['BRAZIL - REAL/US$'].iloc[-1]
df_cad = df1['CANADA - CANADIAN DOLLAR/US$'].iloc[-1]
df_cny = df1['CHINA - YUAN/US$'].iloc[-1]
df_hkd = df1['HONG KONG - HONG KONG DOLLAR/US$'].iloc[-1]
df_inr = df1['INDIA - INDIAN RUPEE/US$'].iloc[-1]
df_krw = df1['KOREA - WON/US$'].iloc[-1]
df_mxn = df1['MEXICO - MEXICAN PESO/US$'].iloc[-1]
df_zar = df1['SOUTH AFRICA - RAND/US$'].iloc[-1]
df_sgd = df1['SINGAPORE - SINGAPORE DOLLAR/US$'].iloc[-1]
df_dkk = df1['DENMARK - DANISH KRONE/US$'].iloc[-1]
df_jpy = df1['JAPAN - YEN/US$'].iloc[-1]
df_myr = df1['MALAYSIA - RINGGIT/US$'].iloc[-1]
df_nok = df1['NORWAY - NORWEGIAN KRONE/US$'].iloc[-1]
df_sek = df1['SWEDEN - KRONA/US$'].iloc[-1]
df_lkr = df1['SRI LANKA - SRI LANKAN RUPEE/US$'].iloc[-1]
df_chf = df1['SWITZERLAND - FRANC/US$'].iloc[-1]
df_twd = df1['TAIWAN - NEW TAIWAN DOLLAR/US$'].iloc[-1]
df_thb = df1['THAILAND - BAHT/US$'].iloc[-1]
df_usd = 1.0

# Global Variables
from_conversion_symbol = 'USD'
to_conversion_symbol = 'USD'
amount_value = 0.0
converted_value = 0.0
message = ""
selected_currency = ""

data_frame_label = {
        'Australian Dollar':'AUSTRALIA - AUSTRALIAN DOLLAR/US$',
        'Euro Members':'EURO AREA - EURO/US$',
        'New Zealand Dollar':'NEW ZEALAND - NEW ZELAND DOLLAR/US$',
        'United Kingdom Pound':'UNITED KINGDOM - UNITED KINGDOM POUND/US$',
        'Brazil Real':'BRAZIL - REAL/US$',
        'Canada Dollar':'CANADA - CANADIAN DOLLAR/US$',
        'China Yuan':'CHINA - YUAN/US$',
        'Hong Kong Dollar':'HONG KONG - HONG KONG DOLLAR/US$',
        'India Rupee':'INDIA - INDIAN RUPEE/US$',
        'South Korea Won':'KOREA - WON/US$',
        'Mexico Peso':'MEXICO - MEXICAN PESO/US$',
        'South Africa Rand':'SOUTH AFRICA - RAND/US$',
        'Singapore Dollar':'SINGAPORE - SINGAPORE DOLLAR/US$',
        'Denmark Krone':'DENMARK - DANISH KRONE/US$',
        'Japan' + unescape('&nbsp;') + 'Yen':'JAPAN - YEN/US$',
        'Malaysia Ringgit':'MALAYSIA - RINGGIT/US$',
        'Norway Krone':'NORWAY - NORWEGIAN KRONE/US$',
        'Sweden Krona':'SWEDEN - KRONA/US$',
        'Sri Lanka Rupee':'SRI LANKA - SRI LANKAN RUPEE/US$',
        'Switzerland Franc':'SWITZERLAND - FRANC/US$',
        'Taiwan New Dollar':'TAIWAN - NEW TAIWAN DOLLAR/US$',
        'Thailand Baht':'THAILAND - BAHT/US$',
}


conversion_dict = {
                    'AUD':df_aud, 'BRL':df_brl, 'CAD':df_cad, 'CHF':df_chf, 'CNY':df_cny,
                    'DKK':df_dkk, 'EUR':df_eur, 'GBP':df_gbp, 'HKD':df_hkd, 'INR':df_inr,
                    'JPY':df_jpy, 'KRW':df_krw, 'LKR':df_lkr, 'MXN':df_mxn, 'MYR':df_myr,
                    'NOK':df_nok, 'NZD':df_nzd, 'SGD':df_sgd, 'ZAR':df_zar, 'SEK':df_sek,
                    'THB':df_thb, 'TWD':df_twd, 'USD':df_usd,
                   }

long_name_dict = {
                    'AUD':'Australian Dollar', 'BRL':'Brazil Real',     'CAD':'Canada Dollar',
                    'CHF':'Switzerland Franc', 'CNY':'China Yuan',      'DKK':'Denmark Krone',
                    'EUR':'Euro Members',      'GBP':'United Kingdom Pound',
                    'HKD':'Hong Kong Dollar',  'INR':'India Rupee',     'JPY':'Japan' + unescape('&nbsp;') + 'Yen',
                    'KRW':'South Korea Won',   'LKR':'Sri Lanka Rupee', 'MXN':'Mexico Peso',
                    'MYR':'Malaysia Ringgit',  'NOK':'Norway Krone',    'NZD':'New Zealand Dollar',
                    'SGD':'Singapore Dollar',  'ZAR':'South Africa Rand',
                    'SEK':'Sweden Krona',      'THB':'Thailand Baht',   'TWD':'Taiwan New Dollar',
                    'USD':'U.S. Dollar',
                }

dropdown_options = [
    {'label': 'Australian Dollar', 'value': 'AUD'},
    {'label': 'Brazil Real', 'value': 'BRL'},
    {'label': 'Canada Dollar', 'value': 'CAD'},
    {'label': 'China Yuan', 'value': 'CNY'},
    {'label': 'Denmark Krone', 'value': 'DKK'},
    {'label': 'Euro Members', 'value': 'EUR'},
    {'label': 'Hong Kong Dollar', 'value': 'HKD'},
    {'label': 'India Rupee', 'value': 'INR'},
    {'label': 'Japan' + unescape('&nbsp;') + 'Yen', 'value': 'JPY'},
    {'label': 'Malaysia Ringgit', 'value': 'MYR'},
    {'label': 'Mexico Peso', 'value': 'MXN'},
    {'label': 'New Zealand Dollar', 'value': 'NZD'},
    {'label': 'Norway Krone', 'value': 'NOK'},
    {'label': 'Singapore Dollar', 'value': 'SGD'},
    {'label': 'South Africa Rand', 'value': 'ZAR'},
    {'label': 'South Korea Won', 'value': 'KRW'},
    {'label': 'Sri Lanka Rupee', 'value': 'LKR'},
    {'label': 'Sweden Krona', 'value': 'SEK'},
    {'label': 'Switzerland Franc', 'value': 'CHF'},
    {'label': 'Taiwan New Dollar', 'value': 'TWD'},
    {'label': 'Thailand Baht', 'value': 'THB'},
    {'label': 'United Kingdom Pound', 'value': 'GBP'},
    {'label': 'U.S. Dollar', 'value': 'USD'},
]



app.layout = html.Div([

    html.H6('Convert from:', style={'color': '#666'}),
    dcc.Dropdown(
        id='convert_from-dropdown',
        options=dropdown_options,
        placeholder="Select a currency",
        value='USD',
    ),

    html.Div(id='convert_from-output-container'),

    html.H6('Convert to:', style={'color': '#666'}),
    dcc.Dropdown(
        id='convert_to-dropdown',
        options=dropdown_options,
        placeholder="Select a currency",
        value='USD',
    ),

    html.Div(id='convert_to-output-container'),

    html.H6('Amount', style={'color': '#666'}),
    dcc.Input(
        id='num-amount',
        type='number',
        debounce=True,
        placeholder=0.00,
    ),

    html.H4(id='message_container'),
    html.Hr(),

    html.H6('All Currencies:', style={'color': '#666'}),
    html.Table([
        html.Tr([html.Td(html.H6('Currency')), html.Td(html.H6('Symbols')), html.Td(html.H6(' ')), html.Td(html.H6('Value'))]),
        html.Tr([html.Td('Australia Dollar'), html.Td('AUD'), html.Td('A' + unescape('&#36;')), html.Td(id='aud')]),
        html.Tr([html.Td('Brazil Real'), html.Td(['BRL', ]), html.Td('R'+ unescape('&#36;')), html.Td(id='brl')]),
        html.Tr([html.Td('Canada Dollar'), html.Td(['CAD', ]), html.Td('C'+ unescape('&#36;')), html.Td(id='cad')]),
        html.Tr([html.Td('China Yuan'), html.Td(['CNY', ]), html.Td(unescape('&#20803;')), html.Td(id='cny')]),
        html.Tr([html.Td('Denmark Krone'), html.Td(['DKK', ]), html.Td('kr'), html.Td(id='dkk')]),
        html.Tr([html.Td('Euro Members'), html.Td(['EUR', ]), html.Td(unescape('&#8364;')), html.Td(id='eur')]),
        html.Tr([html.Td('Hong Kong Dollar'), html.Td(['HKD', ]), html.Td('HK' + unescape('&#36;')), html.Td(id='hkd')]),
        html.Tr([html.Td('India Rupee'), html.Td(['INR', ]), html.Td(unescape('&#8377;')), html.Td(id='inr')]),
        html.Tr([html.Td('Japan Yen'), html.Td(['JPY', ]), html.Td(unescape('&#165;')), html.Td(id='jpy')]),
        html.Tr([html.Td('Malaysia Ringgit'), html.Td(['MYR', ]), html.Td('RM'), html.Td(id='myr')]),
        html.Tr([html.Td('Mexico Peso'), html.Td(['MXN', ]), html.Td('Mex' + unescape('&#36;')), html.Td(id='mxn')]),
        html.Tr([html.Td('New Zealand Dollar'), html.Td(['NZD', ]), html.Td('NZ' + unescape('&#36;')), html.Td(id='nzd')]),
        html.Tr([html.Td('Norway Krone'), html.Td(['NOK', ]), html.Td('kr'), html.Td(id='nok')]),
        html.Tr([html.Td('Singapore Dollar'), html.Td(['SGD', ]), html.Td('S' + unescape('&#36;')), html.Td(id='sgd')]),
        html.Tr([html.Td('South Africa Rand'), html.Td(['ZAR', ]), html.Td('R'), html.Td(id='zar')]),
        html.Tr([html.Td('South Korea Won'), html.Td(['KRW', ]), html.Td(unescape('&#8361;')), html.Td(id='krw')]),
        html.Tr([html.Td('Sri Lanka Rupee'), html.Td(['LKR', ]), html.Td('Rs'), html.Td(id='lkr')]),
        html.Tr([html.Td('Sweden Krona'), html.Td(['SEK', ]), html.Td('kr'), html.Td(id='sek')]),
        html.Tr([html.Td('Switzerland Franc'), html.Td(['CHF', ]), html.Td('fr'), html.Td(id='chf')]),
        html.Tr([html.Td('Taiwan New Dollar'), html.Td(['TWD', ]), html.Td('NT' + unescape('&#36;')), html.Td(id='twd')]),
        html.Tr([html.Td('Thailand Baht'), html.Td(['THB', ]), html.Td(unescape('&#3647;')), html.Td(id='thb')]),
        html.Tr([html.Td('United Kingdom Pound'), html.Td(['GBP', ]), html.Td(unescape('&#163;')), html.Td(id='gbp')]),
        html.Tr([html.Td('U.S. Dollar'), html.Td(['USD', ]), html.Td('$'), html.Td(id='usd')]),
    ]),

########################### First Graph #############################

    html.Hr(),
    html.H3('Multi Line chart'),
    dcc.Graph(id='graph1',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='Foreign Exchange Rate 2000-2019',
                      xaxis={'title': 'Time'}, yaxis={'title': 'Exchange Rate'})
              }
              ),

    html.Div('Please select a timeframe', style={'color': '#ef3e18', 'margin': '10px'}),
    dcc.Dropdown(
        id='select-timeframe',
        options=[
            {'label': 'Year', 'value': 'Year'},
            {'label': 'Decade', 'value': 'Decade'},
            {'label': 'All time', 'value': 'All time'},
        ],
        value='Year'
    ),
    html.Hr(),
#])

######################### End First Graph ####################
######################## Begin Second Graph ##################

html.H3('Multi Line chart', style={'color': '#df1e56'}),
dcc.Graph(id='graph2',
          figure={
              'data': data_multiline,
              'layout': go.Layout(
                  title='Foreign Exchange Rate 2000-2019',
                  xaxis={'title': 'Time'}, yaxis={'title': 'Exchange Rate'})
          }
          ),
html.Div('Please select a currency', style={'color': '#ef3e18', 'margin': '10px'}),
# dcc.Dropdown(
#         id='select-currency',
#         options=data_frame_label,
#         placeholder="Select a currency",
#         value='AUSTRALIA - AUSTRALIAN DOLLAR/US$',
#     ),
dcc.Dropdown(
    id='select-currency',
    placeholder="Select a currency",
    options=[
         {'label': 'Australian Dollar', 'value': 'AUSTRALIA - AUSTRALIAN DOLLAR/US$'},
         {'label': 'Euro Members', 'value': 'EURO AREA - EURO/US$'},
         {'label': 'New Zealand Dollar', 'value': 'NEW ZEALAND - NEW ZELAND DOLLAR/US$'},
         {'label': 'United Kingdom Pound', 'value': 'UNITED KINGDOM - UNITED KINGDOM POUND/US$'},
         {'label': 'Brazil Real', 'value': 'BRAZIL - REAL/US$'},
         {'label': 'Canada Dollar', 'value': 'CANADA - CANADIAN DOLLAR/US$'},
         {'label': 'China Yuan', 'value': 'CHINA - YUAN/US$'},
         {'label': 'Hong Kong Dollar', 'value': 'HONG KONG - HONG KONG DOLLAR/US$'},
         {'label': 'India Rupee', 'value': 'INDIA - INDIAN RUPEE/US$'},
         {'label': 'South Korea Won', 'value': 'KOREA - WON/US$'},
         {'label': 'Mexico Peso', 'value': 'MEXICO - MEXICAN PESO/US$'},
         {'label': 'South Africa Rand', 'value': 'SOUTH AFRICA - RAND/US$'},
         {'label': 'Singapore Dollar', 'value': 'SINGAPORE - SINGAPORE DOLLAR/US$'},
         {'label': 'Denmark Krone', 'value': 'DENMARK - DANISH KRONE/US$'},
         {'label': 'Japan' + unescape('&nbsp;') + 'Yen', 'value': 'JAPAN - YEN/US$'},
         {'label': 'Malaysia Ringgit', 'value': 'MALAYSIA - RINGGIT/US$'},
         {'label': 'Norway Krone', 'value': 'NORWAY - NORWEGIAN KRONE/US$'},
         {'label': 'Sweden Krona', 'value': 'SWEDEN - KRONA/US$'},
         {'label': 'Sri Lanka Rupee', 'value': 'SRI LANKA - SRI LANKAN RUPEE/US$'},
         {'label': 'Switzerland Franc', 'value': 'SWITZERLAND - FRANC/US$'},
         {'label': 'Taiwan New Dollar', 'value': 'TAIWAN - NEW TAIWAN DOLLAR/US$'},
         {'label': 'Thailand Baht', 'value': 'THAILAND - BAHT/US$'},
    ],
    value='AUSTRALIA - AUSTRALIAN DOLLAR/US$',
    ),


######################## End Second Graph ####################
#################### Begin Third Graph #######################

    html.Hr(),
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='Foreign Exchange Rate 2000-2019',
                      xaxis={'title': 'Time'}, yaxis={'title': 'Exchange Rate'})
              }
              ),
    html.Div('Please select a first country to compare.', style={'color': '#ef3e18', 'margin': '10px'}),
    dcc.Dropdown(
        id='comparison1',
        placeholder="Select a currency",
        options=[
            {'label': 'Australian Dollar', 'value': 'AUSTRALIA - AUSTRALIAN DOLLAR/US$'},
            {'label': 'Euro Members', 'value': 'EURO AREA - EURO/US$'},
            {'label': 'New Zealand Dollar', 'value': 'NEW ZEALAND - NEW ZELAND DOLLAR/US$'},
            {'label': 'United Kingdom Pound', 'value': 'UNITED KINGDOM - UNITED KINGDOM POUND/US$'},
            {'label': 'Brazil Real', 'value': 'BRAZIL - REAL/US$'},
            {'label': 'Canada Dollar', 'value': 'CANADA - CANADIAN DOLLAR/US$'},
            {'label': 'China Yuan', 'value': 'CHINA - YUAN/US$'},
            {'label': 'Hong Kong Dollar', 'value': 'HONG KONG - HONG KONG DOLLAR/US$'},
            {'label': 'India Rupee', 'value': 'INDIA - INDIAN RUPEE/US$'},
            {'label': 'South Korea Won', 'value': 'KOREA - WON/US$'},
            {'label': 'Mexico Peso', 'value': 'MEXICO - MEXICAN PESO/US$'},
            {'label': 'South Africa Rand', 'value': 'SOUTH AFRICA - RAND/US$'},
            {'label': 'Singapore Dollar', 'value': 'SINGAPORE - SINGAPORE DOLLAR/US$'},
            {'label': 'Denmark Krone', 'value': 'DENMARK - DANISH KRONE/US$'},
            {'label': 'Japan' + unescape('&nbsp;') + 'Yen', 'value': 'JAPAN - YEN/US$'},
            {'label': 'Malaysia Ringgit', 'value': 'MALAYSIA - RINGGIT/US$'},
            {'label': 'Norway Krone', 'value': 'NORWAY - NORWEGIAN KRONE/US$'},
            {'label': 'Sweden Krona', 'value': 'SWEDEN - KRONA/US$'},
            {'label': 'Sri Lanka Rupee', 'value': 'SRI LANKA - SRI LANKAN RUPEE/US$'},
            {'label': 'Switzerland Franc', 'value': 'SWITZERLAND - FRANC/US$'},
            {'label': 'Taiwan New Dollar', 'value': 'TAIWAN - NEW TAIWAN DOLLAR/US$'},
            {'label': 'Thailand Baht', 'value': 'THAILAND - BAHT/US$'},
        ],
        value='AUSTRALIA - AUSTRALIAN DOLLAR/US$'
    ),
    html.Div('Please select a second country to compare.', style={'color': '#ef3e18', 'margin': '10px'}),
    dcc.Dropdown(
        id='comparison2',
        placeholder="Select a currency",
        options=[
            {'label': 'Australian Dollar', 'value': 'AUSTRALIA - AUSTRALIAN DOLLAR/US$'},
            {'label': 'Euro Members', 'value': 'EURO AREA - EURO/US$'},
            {'label': 'New Zealand Dollar', 'value': 'NEW ZEALAND - NEW ZELAND DOLLAR/US$'},
            {'label': 'United Kingdom Pound', 'value': 'UNITED KINGDOM - UNITED KINGDOM POUND/US$'},
            {'label': 'Brazil Real', 'value': 'BRAZIL - REAL/US$'},
            {'label': 'Canada Dollar', 'value': 'CANADA - CANADIAN DOLLAR/US$'},
            {'label': 'China Yuan', 'value': 'CHINA - YUAN/US$'},
            {'label': 'Hong Kong Dollar', 'value': 'HONG KONG - HONG KONG DOLLAR/US$'},
            {'label': 'India Rupee', 'value': 'INDIA - INDIAN RUPEE/US$'},
            {'label': 'South Korea Won', 'value': 'KOREA - WON/US$'},
            {'label': 'Mexico Peso', 'value': 'MEXICO - MEXICAN PESO/US$'},
            {'label': 'South Africa Rand', 'value': 'SOUTH AFRICA - RAND/US$'},
            {'label': 'Singapore Dollar', 'value': 'SINGAPORE - SINGAPORE DOLLAR/US$'},
            {'label': 'Denmark Krone', 'value': 'DENMARK - DANISH KRONE/US$'},
            {'label': 'Japan' + unescape('&nbsp;') + 'Yen', 'value': 'JAPAN - YEN/US$'},
            {'label': 'Malaysia Ringgit', 'value': 'MALAYSIA - RINGGIT/US$'},
            {'label': 'Norway Krone', 'value': 'NORWAY - NORWEGIAN KRONE/US$'},
            {'label': 'Sweden Krona', 'value': 'SWEDEN - KRONA/US$'},
            {'label': 'Sri Lanka Rupee', 'value': 'SRI LANKA - SRI LANKAN RUPEE/US$'},
            {'label': 'Switzerland Franc', 'value': 'SWITZERLAND - FRANC/US$'},
            {'label': 'Taiwan New Dollar', 'value': 'TAIWAN - NEW TAIWAN DOLLAR/US$'},
            {'label': 'Thailand Baht', 'value': 'THAILAND - BAHT/US$'},
        ],
        value='EURO AREA - EURO/US$'
    ),
    html.Div('Please enter a year between 2000 and 2019 to filter timeframe of the graph.', style={'color': '#ef3e18', 'margin': '10px'}),
    html.Div(dcc.Input(id='timeframe2', type='text')),
    html.Br(),
    html.Button('Submit', id='button'),
    html.Br(),
    html.Br()
])

#################### End Third Graph #########################

@app.callback(
    Output('aud', 'children'),
    Output('brl', 'children'),
    Output('cad', 'children'),
    Output('cny', 'children'),
    Output('dkk', 'children'),
    Output('eur', 'children'),
    Output('hkd', 'children'),
    Output('inr', 'children'),
    Output('jpy', 'children'),
    Output('myr', 'children'),
    Output('mxn', 'children'),
    Output('nzd', 'children'),
    Output('nok', 'children'),
    Output('sgd', 'children'),
    Output('zar', 'children'),
    Output('krw', 'children'),
    Output('lkr', 'children'),
    Output('sek', 'children'),
    Output('chf', 'children'),
    Output('twd', 'children'),
    Output('thb', 'children'),
    Output('gbp', 'children'),
    Output('usd', 'children'),
    Input('num-amount', 'value'))
def callback_a(x):
    global amount_value
    amount_value = x
    if x is None:
        raise PreventUpdate
    else:
        return np.round(x / conversion_dict[from_conversion_symbol] * df_aud, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_brl, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_cad, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_cny, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_dkk, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_eur, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_hkd, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_inr, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_jpy, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_myr, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_mxn, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_nzd, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_nok, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_sgd, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_zar, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_krw, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_lkr, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_sek, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_chf, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_twd, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_thb, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_gbp, 2), \
           np.round(x / conversion_dict[from_conversion_symbol] * df_usd, 2),

@app.callback(
    Output('convert_from-output-container', 'children'),
    Output('num-amount', 'value'),
    Input('convert_from-dropdown', 'value')
)
def update_convert_from(value):
    if value is None:
        raise PreventUpdate
    else:
        global from_conversion_symbol
        from_conversion_symbol = value
    # return ['Conversion Rate, USD to {} : {}'.format(value, np.round(conversion_dict[value],2)), amount_value]
    return['', amount_value]


@app.callback(
    Output('convert_to-output-container', 'children'),
    # Output('num-amount', 'value'),
    Input('convert_to-dropdown', 'value')
)
def update_convert_to(value):
    if value is None:
        raise PreventUpdate
    else:
        global to_conversion_symbol
        to_conversion_symbol = value
    # return ['Conversion Rate, USD to {} : {}'.format(value, np.round(conversion_dict[value],2))]
    return['', '']

@app.callback(
    Output('message_container', 'children'),
    Input('convert_to-dropdown', 'value'),
    Input('num-amount', 'value')
)
def update_message(value, value2):
    if amount_value is None:
        raise PreventUpdate
    else:
        global message
        message = ['{} {} is equivalent to {} {}'.format(amount_value,
            long_name_dict[from_conversion_symbol], # from_conversion_symbol,
            np.round(amount_value / conversion_dict[from_conversion_symbol] * conversion_dict[to_conversion_symbol], 2),
            long_name_dict[to_conversion_symbol])] # to_conversion_symbol)]
        return message


######################### Begin First Graph Callback ######################


# @app.callback(Output('graph1', 'figure'), [Input('select-timeframe', 'value')])


################### End First Graph Callback ##############################
######################### Begin Second Graph ##############################
#selected_currency = conversion_dict['value']

@app.callback(Output('graph2', 'figure'), [Input('select-currency', 'value')])
def update_figure(selected_currency):
    # print(data_frame_label[selected_currency])
    # selected = data_frame_label[selected_currency]
    if selected_currency is None:
        raise PreventUpdate
    else:
        country = selected_currency
        trace1_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df[country],
                                  mode='lines', name=country)
        data_multiline = [trace1_multiline]

    return {'data': data_multiline,
            'layout': go.Layout(title='Foreign Exchange Rates for ' + selected_currency,
                                xaxis={'title': 'Time'},
                                yaxis={'title': 'Exchange Rate'})}

@app.callback(Output('graph1', 'figure'), [Input('select-timeframe', 'value')])
def update_figure(selected_timeframe):
    if selected_timeframe is None:
        raise PreventUpdate
    else:
        filtered_df = multiline_df

    if (selected_timeframe == 'Year'):
        filtered_df = dfCurrentYear
    if (selected_timeframe == 'Decade'):
        filtered_df = dfCurrentDecade
    if (selected_timeframe == 'All time'):
        filtered_df = multiline_df

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    trace1_multiline = go.Scatter(x=filtered_df['Date'], y=filtered_df['AUSTRALIA - AUSTRALIAN DOLLAR/US$'],
                                  mode='lines',
                                  name='AUSTRALIA - AUSTRALIAN DOLLAR/US$')

    trace2_multiline = go.Scatter(x=filtered_df['Date'], y=filtered_df['EURO AREA - EURO/US$'],
                                  mode='lines',
                                  name='EURO AREA - EURO/US$')

    trace3_multiline = go.Scatter(x=filtered_df['Date'], y=filtered_df['NEW ZEALAND - NEW ZELAND DOLLAR/US$'],
                                  mode='lines',
                                  name='NEW ZEALAND - NEW ZELAND DOLLAR/US$')

    data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]
    return {'data': data_multiline,
            'layout': go.Layout(title='Foreign Exchange Rates for ' + selected_timeframe,
                                xaxis={'title': 'Time'},
                                yaxis={'title': 'Exchange Rate'})}


################### End Second Graph Callback #############################

@app.callback(Output('graph3', 'figure'),[Input('comparison1', 'value')],[Input('comparison2', 'value')],[Input('button', 'n_clicks')],state=[State('timeframe2', 'value')])
def update_figure2(selected_currency1, selected_currency2, n_clicks, selected_timeframe):
    if ((selected_currency1 is None) or (selected_currency2 is None) or (selected_timeframe is None)):
        raise PreventUpdate
    else:
        filtered_df = multiline_df
        currency1 = selected_currency1
        currency2 = selected_currency2
        if(selected_timeframe != None):
            if(selected_timeframe.isdigit()):
                if (int(selected_timeframe) >= 2000 and int(selected_timeframe) <= 2019):
                    dfTime = new_df2
                    dfTime['Date'] = pd.to_datetime(dfTime['Date'])
                    dfCurrentTime = dfTime[dfTime['Date'].dt.year >= int(selected_timeframe)]
                    filtered_df = dfCurrentTime
        filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        newTrace1_multiline = go.Scatter(x=filtered_df['Date'], y=filtered_df[currency1],
                                    mode='lines', name=currency1)
        newTrace2_multiline = go.Scatter(x=filtered_df['Date'], y=filtered_df[currency2], mode='lines',
                                    name=currency2)
        data_multiline2 = [newTrace1_multiline, newTrace2_multiline]
    return {'data': data_multiline2,
            'layout': go.Layout(title='Foreign Exchange Rates for ' + selected_currency1 + ' and' + selected_currency2,
                                xaxis={'title': 'Time'},
                                yaxis={'title': 'Exchange Rate'})}


if __name__ == '__main__':
    app.run_server(debug=True)
