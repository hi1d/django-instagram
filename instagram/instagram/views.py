from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):

    def get(self, request):
        print("Get으로 호출")
        return render(request, "instagram/main.html")

    def post(self, request):
        print("Post로 호출")
        return render(request, "instagram/main.html")
