import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from html import unescape

# Global Variables
from_conversion_symbol = 'USD'
to_conversion_symbol = 'USD'
amount_value: float = 0.0
converted_value: float = 0.0
message = ""
selected_currency = ""

# Load CSV file from Datasets folder
df1 = new_df = new_df2 = pd.read_csv('./datasets/ForeignExchange.csv') #df2

dfDecade = df1
dfDecade['Date'] = pd.to_datetime(dfDecade['Date'])
dfCurrentDecade = dfDecade[dfDecade['Date'].dt.year >= 2010]

dfYear = df1
dfYear['Date'] = pd.to_datetime(dfYear['Date'])
dfCurrentYear = dfYear[dfYear['Date'].dt.year == 2019]

new_df['Date'] = pd.to_datetime(new_df['Date'])

multiline_df = df1

trace1_multiline = go.Scatter(x=multiline_df['Date'],
                              y=multiline_df['AUSTRALIA - AUSTRALIAN DOLLAR/US$'],
                              mode='lines',
                              name='AUD/US$')
trace2_multiline = go.Scatter(x=multiline_df['Date'],
                              y=multiline_df['EURO AREA - EURO/US$'],
                              mode='lines',
                              name='EUR/US$')
trace3_multiline = go.Scatter(x=multiline_df['Date'],
                              y=multiline_df['NEW ZEALAND - NEW ZELAND DOLLAR/US$'],
                              mode='lines',
                              name='NZD/US$')
trace4_multiline = go.Scatter(x=multiline_df['Date'],
                              y=multiline_df['UNITED KINGDOM - UNITED KINGDOM POUND/US$'],
                              mode='lines',
                              name='GBP/US$')
trace5_multiline = go.Scatter(x=multiline_df['Date'],
                              y=multiline_df['BRAZIL - REAL/US$'],
                              mode='lines',
                              name='BRL/US$')
trace6_multiline = go.Scatter(x=multiline_df['Date'],
                              y=multiline_df['CANADA - CANADIAN DOLLAR/US$'],
                              mode='lines',
                              name='CAD/US$')
trace7_multiline = go.Scatter(x=multiline_df['Date'],
                              y=multiline_df['CHINA - YUAN/US$'],
                              mode='lines',
                              name='CNY/US$')
trace8_multiline = go.Scatter(x=multiline_df['Date'],
                              y=multiline_df['HONG KONG - HONG KONG DOLLAR/US$'],
                              mode='lines',
                              name='HKD/US$')
trace9_multiline = go.Scatter(x=multiline_df['Date'],
                              y=multiline_df['INDIA - INDIAN RUPEE/US$'],
                              mode='lines',
                              name='INR/US$')
trace10_multiline = go.Scatter(x=multiline_df['Date'],
                               y=multiline_df['KOREA - WON/US$'],
                               mode='lines',
                               name='KRW/US$')
trace11_multiline = go.Scatter(x=multiline_df['Date'],
                               y=multiline_df['MEXICO - MEXICAN PESO/US$'],
                               mode='lines',
                               name='MXN/US$')
trace12_multiline = go.Scatter(x=multiline_df['Date'],
                               y=multiline_df['SOUTH AFRICA - RAND/US$'],
                               mode='lines',
                               name='ZAR/US$')
trace13_multiline = go.Scatter(x=multiline_df['Date'],
                               y=multiline_df['SINGAPORE - SINGAPORE DOLLAR/US$'],
                               mode='lines',
                               name='SGD/US$')
trace14_multiline = go.Scatter(x=multiline_df['Date'],
                               y=multiline_df['DENMARK - DANISH KRONE/US$'],
                               mode='lines',
                               name='DKK/US$')
trace15_multiline = go.Scatter(x=multiline_df['Date'],
                               y=multiline_df['JAPAN - YEN/US$'],
                               mode='lines',
                               name='JPY/US$')
trace16_multiline = go.Scatter(x=multiline_df['Date'],
                               y=multiline_df['MALAYSIA - RINGGIT/US$'],
                               mode='lines',
                               name='MYR/US$')
trace17_multiline = go.Scatter(x=multiline_df['Date'],
                               y=multiline_df['NORWAY - NORWEGIAN KRONE/US$'],
                               mode='lines',
                               name='NOK/US$')
trace18_multiline = go.Scatter(x=multiline_df['Date'],
                               y=multiline_df['SWEDEN - KRONA/US$'],
                               mode='lines',
                               name='SEK/US$')
trace19_multiline = go.Scatter(x=multiline_df['Date'],
                               y=multiline_df['SRI LANKA - SRI LANKAN RUPEE/US$'],
                               mode='lines',
                               name='LKR/US$')
trace20_multiline = go.Scatter(x=multiline_df['Date'],
                               y=multiline_df['SWITZERLAND - FRANC/US$'],
                               mode='lines',
                               name='CHF/US$')
trace21_multiline = go.Scatter(x=multiline_df['Date'],
                               y=multiline_df['TAIWAN - NEW TAIWAN DOLLAR/US$'],
                               mode='lines',
                               name='TWD/US$')
trace22_multiline = go.Scatter(x=multiline_df['Date'],
                               y=multiline_df['THAILAND - BAHT/US$'],
                               mode='lines',
                               name='THB/US$')

data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline, trace4_multiline,
                  trace5_multiline, trace6_multiline, trace7_multiline, trace8_multiline,
                  trace11_multiline, trace12_multiline,
                  trace13_multiline,trace14_multiline, trace16_multiline,
                  trace17_multiline, trace18_multiline, trace20_multiline,]

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

data_frame_label = {
                    'AUSTRALIA - AUSTRALIAN DOLLAR/US$':'Australian Dollar',
                    'EURO AREA - EURO/US$':'Euro Members',
                    'NEW ZEALAND - NEW ZELAND DOLLAR/US$':'New Zealand Dollar',
                    'UNITED KINGDOM - UNITED KINGDOM POUND/US$':'United Kingdom Pound',
                    'BRAZIL - REAL/US$':'Brazil Real',
                    'CANADA - CANADIAN DOLLAR/US$':'Canada Dollar',
                    'CHINA - YUAN/US$':'China Yuan',
                    'HONG KONG - HONG KONG DOLLAR/US$':'Hong Kong Dollar',
                    'INDIA - INDIAN RUPEE/US$':'India Rupee',
                    'KOREA - WON/US$':'South Korea Won',
                    'MEXICO - MEXICAN PESO/US$':'Mexico Peso',
                    'SOUTH AFRICA - RAND/US$':'South Africa Rand',
                    'SINGAPORE - SINGAPORE DOLLAR/US$':'Singapore Dollar',
                    'DENMARK - DANISH KRONE/US$':'Denmark Krone',
                    'JAPAN - YEN/US$':'Japan' + unescape('&nbsp;') + 'Yen',
                    'MALAYSIA - RINGGIT/US$':'Malaysia Ringgit',
                    'NORWAY - NORWEGIAN KRONE/US$':'Norway Krone',
                    'SWEDEN - KRONA/US$':'Sweden Krona',
                    'SRI LANKA - SRI LANKAN RUPEE/US$':'Sri Lanka Rupee',
                    'SWITZERLAND - FRANC/US$':'Switzerland Franc',
                    'TAIWAN - NEW TAIWAN DOLLAR/US$':'Taiwan New Dollar',
                    'THAILAND - BAHT/US$':'Thailand Baht',
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

navigation = html.Div(className='nav', children=[
        html.Ul([
            html.Li(dcc.Link('Convert', href='/currency_converter')),
            html.Li(dcc.Link('Overview', href='/high_level_overview')),
            html.Li(dcc.Link('Focus', href='/single_currency_focus')),
            html.Li(dcc.Link('Compare', href='/currency_comparison')),
            html.Li(dcc.Link('Help', href='/user_instructions'))
        ])
    ])

#################### Begin Currency Converter #####################

currency_converter = html.Div([
    navigation,
    html.Div(style={'text-align': 'center'}, children=[
         html.H2('Foreign Currency Exchange', style={'color': '#559C3E'}),
    ]),
    html.Div(className='inner_container', children=[

    html.Div(className='row', children=[
    html.Div(className='six columns', children=[

    html.H6('Convert from:', style={'color': '#559C3E', 'font-weight': 'bold'}),
    dcc.Dropdown(
        id='convert_from-dropdown',
        options=dropdown_options,
        placeholder="Select a currency",
        value='USD',
    ),

    html.Div(id='convert_from-output-container'),

    html.H6('Convert to:', style={'color': '#559C3E', 'font-weight': 'bold'}),
    dcc.Dropdown(
        id='convert_to-dropdown',
        options=dropdown_options,
        placeholder="Select a currency",
        value='USD',
    ),

    html.Div(id='convert_to-output-container'),

    html.H6('Amount', style={'color': '#559C3E', 'font-weight': 'bold'}),
    dcc.Input(
        id='num-amount',
        type='number',
        debounce=False,
        placeholder=0.00,
    ),

    html.H4(id='message_container', style={'color': '#3C77AF', 'margin': '10px'}),
]),

    html.Div(className='six columns', children=[
    html.H6('All Currencies:'),
    html.Table([
        html.Tr([html.Td(html.H6('Currency', style={'color': '#3C77AF'})), html.Td(html.H6(' ')),
        html.Td(html.H6(' ')), html.Td(html.H6('Value', style={'color': '#3C77AF'}))]),
        html.Tr([html.Td('Australia Dollar'), html.Td('AUD'), html.Td('A' + unescape('&#36;')), html.Td(id='aud', style={'color': '#3C77AF'})]), #3300FF
        html.Tr([html.Td('Brazil Real'), html.Td(['BRL', ]), html.Td('R'+ unescape('&#36;')), html.Td(id='brl', style={'color': '#ED8635'})]), #6633FF
        html.Tr([html.Td('Canada Dollar'), html.Td(['CAD', ]), html.Td('C'+ unescape('&#36;')), html.Td(id='cad', style={'color': '#559C3E'})]), #0000CC
        html.Tr([html.Td('China Yuan'), html.Td(['CNY', ]), html.Td(unescape('&#20803;')), html.Td(id='cny', style={'color': '#C33B32'})]), #0000FF
        html.Tr([html.Td('Denmark Krone'), html.Td(['DKK', ]), html.Td('kr'), html.Td(id='dkk', style={'color': '#8C6BB8'})]), #3366CC
        html.Tr([html.Td('Euro Members'), html.Td(['EUR', ]), html.Td(unescape('&#8364;')), html.Td(id='eur', style={'color': '#84584D'})]), #33CCFF
        html.Tr([html.Td('Hong Kong Dollar'), html.Td(['HKD', ]), html.Td('HK' + unescape('&#36;')), html.Td(id='hkd', style={'color': '#D37FBE'})]), #00CC00
        html.Tr([html.Td('India Rupee'), html.Td(['INR', ]), html.Td(unescape('&#8377;')), html.Td(id='inr', style={'color': '#7F7F7F'})]), #006633
        html.Tr([html.Td('Japan Yen'), html.Td(['JPY', ]), html.Td(unescape('&#165;')), html.Td(id='jpy', style={'color': '#BDBC45'})]), #0099CC
        html.Tr([html.Td('Malaysia Ringgit'), html.Td(['MYR', ]), html.Td('RM'), html.Td(id='myr', style={'color': '#5CBBCC'})]), #CC9900
        html.Tr([html.Td('Mexico Peso'), html.Td(['MXN', ]), html.Td('Mex' + unescape('&#36;')), html.Td(id='mxn', style={'color': '#3C77AF'})]), #FF9900
        html.Tr([html.Td('New Zealand Dollar'), html.Td(['NZD', ]), html.Td('NZ' + unescape('&#36;')), html.Td(id='nzd', style={'color': '#ED8635'})]), #FF3300
        html.Tr([html.Td('Norway Krone'), html.Td(['NOK', ]), html.Td('kr'), html.Td(id='nok', style={'color': '#559C3E'})]), #CC0033
        html.Tr([html.Td('Singapore Dollar'), html.Td(['SGD', ]), html.Td('S' + unescape('&#36;')), html.Td(id='sgd', style={'color': '#C33B32'})]), #FF3333
        html.Tr([html.Td('South Africa Rand'), html.Td(['ZAR', ]), html.Td('R'), html.Td(id='zar', style={'color': '#8C6BB8'})]), #CC0000
        html.Tr([html.Td('South Korea Won'), html.Td(['KRW', ]), html.Td(unescape('&#8361;')), html.Td(id='krw', style={'color': '#C1ABA6'})]), #CC0066
        html.Tr([html.Td('Sri Lanka Rupee'), html.Td(['LKR', ]), html.Td('Rs'), html.Td(id='lkr', style={'color': '#D37FBE'})]), #990066
        html.Tr([html.Td('Sweden Krona'), html.Td(['SEK', ]), html.Td('kr'), html.Td(id='sek', style={'color': '#7F7F7F'})]), #FF33FF
        html.Tr([html.Td('Switzerland Franc'), html.Td(['CHF', ]), html.Td('fr'), html.Td(id='chf', style={'color': '#BDBC45'})]), #6600CC
        html.Tr([html.Td('Taiwan New Dollar'), html.Td(['TWD', ]), html.Td('NT' + unescape('&#36;')), html.Td(id='twd', style={'color': '#5CBBCC'})]), #330099
        html.Tr([html.Td('Thailand Baht'), html.Td(['THB', ]), html.Td(unescape('&#3647;')), html.Td(id='thb', style={'color': '#3C77AF'})]), #9900FF
        html.Tr([html.Td('United Kingdom Pound'), html.Td(['GBP', ]), html.Td(unescape('&#163;')), html.Td(id='gbp', style={'color': '#ED8635'})]), #9966FF
        html.Tr([html.Td('U.S. Dollar'), html.Td(['USD', ]), html.Td('$'), html.Td(id='usd', style={'color': '#559C3E'})]), #3300CC
        ]),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
    ]),
    ]),
]),
])

#################### Begin High Level Overview #####################

high_level_overview = html.Div([
    navigation,
    html.Div(className='inner_container', children=[
    html.H3('High Level Overview', style={'color': '#559C3E'}),
    dcc.Graph(id='graph1',
          figure={
              'data': data_multiline,
              'layout': go.Layout(
                  title='Foreign Exchange Rate 2000-2019',
                  xaxis={'title': 'Time'}, yaxis={'title': 'Exchange Rate'})
          }
          ),
    html.Div('Please select a timeframe', style={'color': '#F7B02', 'margin': '10px', 'font-weight': 'bold'}),
    html.Div(className='five columns', children=[
    dcc.Dropdown(
        id='select-timeframe',
        placeholder="Select a timeframe",
        options=[
            {'label': 'Year', 'value': 'Year'},
            {'label': 'Decade', 'value': 'Decade'},
            {'label': 'All time', 'value': 'All time'},
        ],
    value='Year'
    ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    ]),
    ]),
])

#################### Begin Currency Focus #####################

single_currency_focus = html.Div([
    navigation,
    html.Div(className='inner_container', children=[
    html.H3('Single Currency Focus', style={'color': '#559C3E'}),
    dcc.Graph(id='graph2',
          figure={
              'data': data_multiline,
              'layout': go.Layout(
                  title='Foreign Exchange Rate 2000-2019',
                  xaxis={'title': 'Time'}, yaxis={'title': 'Exchange Rate'})
          }
          ),
    html.Div('Please select a currency', style={'color': '#F7B02', 'margin': '10px', 'font-weight': 'bold'}),
    html.Div(className='five columns', children=[
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
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    ]),
    ]),
])

#################### Begin Currency Comparison #######################

currency_comparison = html.Div([
    navigation,
    html.Div(className='inner_container', children=[
    html.H3('Currency Comparison', style={'color': '#559C3E'}),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_duoline,
                  'layout': go.Layout(
                      title='Foreign Exchange Rate 2000-2019',
                      xaxis={'title': 'Time'}, yaxis={'title': 'Exchange Rate'}),
              }
              ),
    html.Div(className='five columns', children=[
    html.Div('Please select first country to compare.', style={'color': '#F7B02', 'margin': '10px', 'font-weight': 'bold'}),
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
    html.Div('Please select second country to compare.', style={'color': '#F7B02', 'margin': '10px', 'font-weight': 'bold'}),
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
    ]),
    html.Div(className='seven columns', children=[
    html.Div('Please enter a year between 2000 and 2019 to filter timeframe of the graph.', style={'color': '#F7B02', 'margin': '10px', 'font-weight': 'bold'}),
    html.Div(dcc.Input(id='timeframe2', type='text')),
    html.Button('Filter', id='button'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    ]),
    html.Br(),
    ]),
])

#################### User Instructions #########################

user_instructions = html.Div([
    navigation,
    html.Div(className='markdown_container', children=[
    html.H3('Instructions', style={'color': '#559C3E', 'margin-left': '10px'}),
    dcc.Markdown('''
            ##### Description:
            
            Foreign Currency Exchange is designed to pull currency conversion data from a consistent source and perform currency conversion from one unit of currency to another, as well as display the historical rates of currency conversion with a graph.
            
            ##### To Convert one currency to another:

                * From the Convert tab, select a currency using the "Convert From" dropdown menu.
                      * For example, If you want to convert 10 US dollars to a equivalent sum of Euros, you would select "U.S Dollar" from the dropdown menu.

                * Select a currency from the "Convert To" dropdown menu and choose the currency you wish to convert to.
                      * For the above example, you would select "European Union Euros"
                * In the input field under "Amount", Type the amount of the currency you wish to convert.
                      * In the Above example, you would type 10 into the input field.
                * The application will display the result below the user selections.
                * Additionally, the conversions for all currencies are shown in the large output box. These currencies are updated as each digit is entered into the "Amount" input field.

            ##### To View the Exchange Rate changes for the Year via a visual representation:

                * Click or tap the "Overview" tab at the top of the screen.
                * Under the words "Foreign Exchange Rates for the Year", you should see a visual representation of the currency rates as imported from the Data.
                * The chart is interactive. Use the icons on the top-right corner of the graph to modify the views. Tooltips should appear when you mouse over the top right corner of the graph.
                * Note the ability to select timeframes by clicking and dragging over a section of the graph. The graph can be reset by clicking the "Reset axes" icon on the top right of the graph.
                * Timeframes for the current year, decade, and all time can also be quickly accessed by using the dropdown menu below the graph.

            ##### To view a more focused chart based on a single currency of your choosing:

                * Click or tap the "Focus" tab at the top of the screen.
                * Under the text "Please select a currency", in the interface, select a currency you wish to view.
                * The graph above the dropdown selector will display the selected currency timeseries.
                * Be sure to explore the tooltips at the top right corner of the graph.

            ##### To view a chart focused on comparison between two currencies of your choosing:

                * Click or tap the "Compare" tab at the top of the screen.
                * Under the text "Please select a first country to compare", in the interface, select your first Currency
                * Under the text "Please select a second country to compare", in the interface, select your second Currency
                * Under the text "Please enter a year between 2000 and 2019 to filter timeframe of the graph", select a year between 2000 and 2019. This year should indicate the center of the time period you wish to represent.
                * You should see your graph updated to reflect the data you entered.
                * Be sure to explore the tooltips at the top right corner of the graph.
        '''),
    ]),
])