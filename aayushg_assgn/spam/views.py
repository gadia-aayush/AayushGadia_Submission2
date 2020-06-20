from django.http import JsonResponse
from .models import Spam
from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import re


class SpamMarker(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		mobno = int(request.data.get('mobno'))

		#validate mobile number [must be 10 digits. assumed that all are of India, so ignored prefixed country codes]
		phoneregex = re.compile(r'^[1-9]\d{9}$')
		if phoneregex.search(str(mobno)):
			pass
		else:
			data = {"code" : 422, "status" : "Unprocessable Entity", "message" : "Mobile Number should be of 10 digits- ^[1-9]\d{9}$"}
			return JsonResponse(data)

		query = Spam.objects.filter(spam_mobno = mobno)
		if len(query) == 0:
			s1 = Spam(spam_mobno = mobno, spam_count = 1)
			s1.save()

		else:
			obj = Spam.objects.get(spam_mobno = mobno)
			count = obj.spam_count
			Spam.objects.filter(spam_mobno = mobno).update(spam_count = count + 1)

		data = {"code" : 201, "status" : "Created", "message" : "Spam Count Updated"}
		return JsonResponse(data)

