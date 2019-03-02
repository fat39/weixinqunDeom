from django.views import View
from django.shortcuts import render

class qunsInfo(View):
    def get(self,request):
        return render(request,"list.html")