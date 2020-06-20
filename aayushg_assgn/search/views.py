import json
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from spam.models import Spam
from myauth.models import UserContacts
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import re



class Search(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request, ip):
		#checking whether string or number given as input
		try:
			query = int(ip)

			output = {"code" : 200, "status": "OK",  "type" : "Search-By-Number", "output" : []}

			# registered or not check
			query2 = User.objects.filter(username = query)
			if len(query2) != 0:
				for each in query2:
					number = each.username
					obj = User.objects.get(username = number)
					name = obj.first_name

					try:
						obj2 = Spam.objects.get(spam_mobno = number)
						count = obj2.spam_count

					except:
						count = 0

					data = {"name" : name, "mobile" : number, "count" : count}
					output["output"].append(data)

			else:
				query3 = UserContacts.objects.filter(uc_mobno = query)
				for each in query3:
					number = each.uc_mobno
					obj = UserContacts.objects.get(uc_mobno = number)
					name = obj.uc_name

					try:
						obj2 = Spam.objects.get(spam_mobno = number)
						count = obj2.spam_count

					except:
						count = 0

					data = {"name" : name, "mobile" : number, "count" : count}
					output["output"].append(data)

			return JsonResponse(output, safe= False)


		# searched by name
		except:
			query = str(ip)
			output = {"code" : 200, "status": "OK", "type" : "Search-By-Name", "output" : []}

			# exact match
			query2 = User.objects.filter(first_name__iexact = query)
			query3 = UserContacts.objects.filter(uc_name__iexact = query)


			# partial match
			query4 = User.objects.filter(first_name__icontains = query)
			query5 = UserContacts.objects.filter(uc_name__icontains = query)

			if len(query2) != 0:
				for each in query2:
					number = each.username
					#print (number)
					obj = User.objects.get(username = number)
					name = obj.first_name

					try:
						obj2 = Spam.objects.get(spam_mobno = number)
						count = obj2.spam_count

					except:
						count = 0

					data = {"name" : name, "mobile" : number, "count" : count}
					output["output"].append(data)


			if len(query3) != 0:
				for each in query3:
					number = each.uc_mobno
					obj = UserContacts.objects.get(uc_mobno = number)
					name = obj.uc_name

					try:
						obj2 = Spam.objects.get(spam_mobno = number)
						count = obj2.spam_count

					except:
						count = 0

					data = {"name" : name, "mobile" : number, "count" : count}
					output["output"].append(data)


			if len(query4) != 0:
				for each in query4:
					number = each.username
					obj = User.objects.get(username = number)
					name = obj.first_name

					try:
						obj2 = Spam.objects.get(spam_mobno = number)
						count = obj2.spam_count

					except:
						count = 0

					data = {"name" : name, "mobile" : number, "count" : count}
					output["output"].append(data)


			if len(query5) != 0:
				for each in query5:
					number = each.uc_mobno
					obj = UserContacts.objects.get(uc_mobno = number)
					name = obj.uc_name

					try:
						obj2 = Spam.objects.get(spam_mobno = number)
						count = obj2.spam_count

					except:
						count = 0

					data = {"name" : name, "mobile" : number, "count" : count}
					output["output"].append(data)

			#print (output)
			return JsonResponse(output, safe= False)
  	
