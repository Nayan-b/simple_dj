from django.shortcuts import render
import requests
# Create your views here.

# create view to fetch the data of covid report using API and display it in the html page


def covid(request):
    # fetching the data from API
    url = 'https://api.covid19api.com/summary'
    response = requests.get(url)
    data = response.json()
    isCountry = False

    # print(data)
    # creating a dictionary to store the data
    
    # else:

    # country_data = {}
    # for country in data['Countries']:
    #     country_data[country['Country']] = {
    #         'confirmed': country['TotalConfirmed'],
    #         # 'recovered': country['TotalRecovered'],
    #         'deaths': country['TotalDeaths'],
    #         'new_confirmed': country['NewConfirmed'],
    #         # 'new_recovered': country['NewRecovered'],
    #         'new_deaths': country['NewDeaths']
    #     }
    #return render(request, 'covid/covid_report.html', {'data': country_data})

    # covid_data = {
    #     'confirmed': data['Global']['TotalConfirmed'],
    #     # 'recovered': data['Global']['TotalRecovered'],
    #     'deaths': data['Global']['TotalDeaths'],
    #     'new_confirmed': data['Global']['NewConfirmed'],
    #     # 'new_recovered': data['Global']['NewRecovered'],
    #     'new_deaths': data['Global']['NewDeaths'],
    #     'countries': data['Countries']
    # }
    # crete a dictionary to store country wise data

    # print country names
    country_names = []
    for country in data['Countries']:
        country_names.append(country['Country'])


    params = {
        'worlddata': data['Global'],
        
        'countryname': country_names
    }
    
    if request.method == 'POST':
        country_data = {}

        country = request.POST['country']
        data = data['Countries']
        for i in data:
            if i['Country'] == country:
                country_data = i
                break

        #print(country_data)
        isCountry = True

        return render(request, 'covid/covid_report.html', {'country_data': country_data , 'countryname': country_names,'isCountry':isCountry})


    # passing the data to the html page
    return render(request, 'covid/covid_report.html', params)
