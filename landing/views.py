from django.shortcuts import render
import pandas as pd

# read the json data from the highcharts website to use later
addi = pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')
# the attributes in the json file are: code3, name, value, code

# the index page function for the main processing
def index_page(request):

    # getting the data from our source (gets updated regularly)
    # the total confirmed counts globally
    confirmed_global_counts = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
                                            encoding='utf-8',
                                            na_values=None)

    # calcing the total count with the "sum" function (the last column has the actual numbers, hence the "-1")
    total_count = confirmed_global_counts[confirmed_global_counts.columns[-1]].sum

    # global number of deaths
    death_global_counts = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

    # calcing the total death counts
    death_total_counts = death_global_counts[death_global_counts.columns[-1]].sum

    # store all of the countries by grouping to avoid reps
    bar_chart_data = confirmed_global_counts[['Country/Region', confirmed_global_counts.columns[-1]]].groupby('Country/Region').sum()

    # reset the indexes to assign them manually as "Country/Region" and "values" (which represents date)
    bar_chart_data = bar_chart_data.reset_index()
    bar_chart_data.columns = ['Country/Region', 'values']

    # sort the dates by a descending format
    bar_chart_data = bar_chart_data.sort_values(by = 'values', ascending = False)

    # create 2 lists for bar chart, one for the dates and one for the countries' names
    bar_chart_values = bar_chart_data['values'].values.tolist()
    countries_names = bar_chart_data['Country/Region'].values.tolist()

    # using the "map_data" function for getting the data needed
    data_of_map = map_data(bar_chart_data, countries_names)

    # use this later to determine whether a map should be shown or not
    show_map_cond = 'True'

    # a dict for storing the data and passing it
    context = {
        'total_count': total_count,
        'death_total_counts': death_total_counts,
        'countries_names': countries_names,
        'bar_chart_values': bar_chart_values,
        'data_of_map': data_of_map,
        'show_map_cond': show_map_cond
    }

    return render(request, 'index.html', context)


def map_data(bar_chart_data, countries_names):

    # a list for storing the data of the map later
    data_of_map = []

    # cycle through
    for i in countries_names:
        try:
            # store the names by their name
            temp_addi = addi[addi['name'] == i]

            # the dict needed for storing the attributes
            temp_dict = {}

            # store the list form of the data for "code3" part
            temp_dict["code3"] = list(temp_addi['code3'].values)[0]

            # store the names by the name of each country
            temp_dict["name"] = i

            # store the vals using the data from bar chart (passed it), get the sum of all places which have the name of that country
            temp_dict["value"] = bar_chart_data[bar_chart_data['Country/Region'] == i]['values'].sum()

            # store a list of codes of the col
            temp_dict["code"] = list(temp_addi['code'].values)[0]

            # at last, add the data to the world map data
            data_of_map.append(temp_dict)
        except:
            pass

    return data_of_map


def individual_country_data(request):

    # get the name of that particular country
    country_name_gotten = request.POST.get('country_name_loop')

    # getting the previous data
    confirmed_global_counts = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
                                            encoding='utf-8',
                                            na_values=None)

    total_count = confirmed_global_counts[confirmed_global_counts.columns[-1]].sum

    death_global_counts = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

    death_total_counts = death_global_counts[death_global_counts.columns[-1]].sum

    bar_chart_data = confirmed_global_counts[['Country/Region', confirmed_global_counts.columns[-1]]].groupby('Country/Region').sum()

    bar_chart_data = bar_chart_data.reset_index()
    bar_chart_data.columns = ['Country/Region', 'values']

    bar_chart_data = bar_chart_data.sort_values(by = 'values', ascending = False)

    bar_chart_values = bar_chart_data['values'].values.tolist()
    countries_names = bar_chart_data['Country/Region'].values.tolist()

    show_map_cond = 'False'


    # for analysing a single country and making its graph
    each_country_data = pd.DataFrame(confirmed_global_counts[confirmed_global_counts['Country/Region'] == country_name_gotten][confirmed_global_counts.columns[7:-1]].sum()).reset_index()
    each_country_data.columns = ['country','values']
    each_country_data['lagVal'] = each_country_data['values'].shift(1).fillna(0)
    each_country_data['incrementVal'] = each_country_data['values'] - each_country_data['lagVal']

    # calc the moving/rolling mean for each country for the past 1 week
    each_country_data['rollingMean'] = each_country_data['incrementVal'].rolling(window = 7).mean()
    each_country_data = each_country_data.fillna(0)

    # this consists of the 2 dicts
    datasets_for_line = [
                            {'label': ' > Moving/Rolling Mean 1 Week  ', 'data': each_country_data['rollingMean'].values.tolist(), 'linestyle': 'dashed', 'backgroundColor': '#0c48b7'},
                            {'label': ' > Daily Cumulated Data  ', 'data': each_country_data['values'].values.tolist(), 'linestyle': 'solid', 'backgroundColor': '#d6e3ff'}
                        ]

    # calc the values for the axis
    axisvalues = each_country_data.index.tolist()

    # this context has 2 extra fields
    context = {
        'axisvalues': axisvalues,
        'country_name': country_name_gotten,
        'total_count': total_count,
        'death_total_counts': death_total_counts,
        'countries_names': countries_names,
        'bar_chart_values': bar_chart_values,
        'show_map_cond': show_map_cond,
        'datasets_for_line': datasets_for_line
    }

    return render(request, 'index.html', context)
