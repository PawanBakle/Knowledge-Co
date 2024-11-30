from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def users(request):
    #pull data from third party rest api
    response = requests.get('https://codeforces.com/api/problemset.problems')
    #convert reponse data into json
    
    
    problems = response.json()['result']['problems']
    return render(request, 'qnsBank.html', {'problems':problems})
    

# def problem_list_view(request):
#     problems = users()
#     context = {'problems': problems}
#     print(problems)
#     return render(request, 'qnsBank.html', context)








