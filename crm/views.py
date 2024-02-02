from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from bussines_customer.models import Request
from bussines_customer.decorators import staff_member_required
from datetime import datetime, timedelta
from django.utils.dateformat import DateFormat
from django.http import HttpResponseForbidden

# Create your views here.
@staff_member_required
def admin_index(request):
	#get by status
	total_request = Request.objects.filter().count
	pending_request = Request.objects.filter(status= "pending".lower()).count
	approved_request = Request.objects.filter(status= "approved".lower()).count
	rejected_request = Request.objects.filter(status= "rejected".lower()).count

	#get by date
	today = datetime.today()
	today_request = Request.objects.filter(created_date__year=today.year, created_date__month=today.month, created_date__day=today.day).count
	month_request = Request.objects.filter(created_date__year=today.year, created_date__month=today.month).count
	year_request = Request.objects.filter(created_date__year=today.year).count
	one_week_ago = datetime.today() - timedelta(days=7)
	week_request = Request.objects.filter(created_date__gte=one_week_ago).count
	return render(request, "crm/index.html", context={"total_requests":total_request, 
												   "approved_requests":approved_request, 
												   "pending_requests":pending_request,
												   "rejected_requests":rejected_request, 
												   "today_requests":today_request,
													"week_requests":week_request,
													"month_requests":month_request,
													"year_requests":year_request})

@staff_member_required
def get_admin_requests(request, status):
	get_requests = Request.objects.filter(status=status.lower())
	return render(request, "crm/get_requests.html", context={"get_requests": get_requests, "status":status})

@staff_member_required
def admin_requests(request):
	all_requests = Request.objects.filter()
	return render(request, "crm/requests.html", context={"requests": all_requests})

@staff_member_required
def admin_view_request(request, id):
	view_request = Request.objects.get(id=id)
	return render(request, "crm/admin_view_request.html", context={"request":view_request})

@staff_member_required
def approve_request(request, id):
	request = Request.objects.get(id=id)
	if request is not None:
		request.status = "approved"
		request.save()
	else:
		return HttpResponseForbidden("The request is not found")
	return redirect("successful", message = "approved")

@staff_member_required
def reject_request(request, id):
	request = Request.objects.get(id=id)
	if request is not None:
		request.status = "rejected"
		request.save()
	else:
		return HttpResponseForbidden("The request is not found")
	return redirect("successful", message = "rejected")

@staff_member_required
def successful(request, message):
	return render(request, "crm/successful.html", context={"message":message})