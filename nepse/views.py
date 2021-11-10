from django.shortcuts import render
import requests

# Create your views here.


def nepse(request):

    url = 'https://nepse-data-api.herokuapp.com/data/todaysprice'
    response = requests.get(url)
    data = response.json()
    stockname = ''
    isCompany = False

    # get the data from GET request
    try:
        stockname = request.GET['stock']

        # print(stockname)
    except:
        stockname = ''

    # find the companyName and append to list
    company_name = []
    for i in data:
        company_name.append(i['companyName'])

    # print(company_name)

    for i in data:
        if i['companyName'] == stockname:
            data = i
            isCompany = True
            break

    params = {
        'company_name': company_name,
        'data': data,
        'isCompany': isCompany

    }

    return render(request, 'nepse/nepse.html', params)
