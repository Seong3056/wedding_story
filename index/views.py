from django.shortcuts import render
from api import address
# Create your views here.
def index(request):
    print(request.POST)
    # print(request.POST["address1"])
    # print(request.POST["address2"])
    address1 = request.POST["address1"]
    address2 = request.POST["address2"]
    # address1 = "서울시"
    # address2 = "마포구"
    keyword = "웨딩메이크업"
    data = address.search(address1, address2, keyword)
    context = {
        "data" : data
    }


    return render(request, "index.html", context)