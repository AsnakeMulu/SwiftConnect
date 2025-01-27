from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as loginUser, authenticate, logout as logoutUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from .forms import NewUserForm, RequestForm
from .models import Request
from .decorators import allowed_users
from datetime import datetime
from django.http import HttpResponseForbidden

# Create your views here.
def login(request):

	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				loginUser(request, user)

				#messages.info(request, f"You are now logged in as {username}.")
				if user.is_staff:
					return redirect("admin_index")
				else:
					return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()

	return render( request=request, template_name="customer/login.html",  context={'login_form': form} )

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			group, _ = Group.objects.get_or_create(name='customer')
			
			user = form.save()
			user.groups.add(group)
			#loginUser(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		else:
			#form = NewUserForm()
			messages.error(request, "Unsuccessful registration. Invalid information.")
	if request.method == "GET":
		form = NewUserForm()
	return render (request=request, template_name="customer/register.html", context={"register_form":form})

@login_required(login_url='login')
def logout(request):
    logoutUser(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def index(request):
	current_user = request.user.id
	customer = User.objects.get(id=current_user)
	total_request = Request.objects.filter(customer=customer).count
	pending_request = Request.objects.filter(customer=customer, status= "pending".lower()).count
	approved_request = Request.objects.filter(customer=customer, status= "approved".lower()).count
	rejected_request = Request.objects.filter(customer=customer, status= "rejected".lower()).count
	all_requests = Request.objects.filter(customer=customer)
	return render(request, "customer/index.html", context={"requests": all_requests, "total_requests":total_request, "approved_requests":approved_request, "pending_requests":pending_request,"rejected_requests":rejected_request })

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def requests(request):
	current_user = request.user.id
	customer = User.objects.get(id=current_user)
	all_requests = Request.objects.filter(customer=customer)
	return render(request, "customer/requests.html", context={"requests": all_requests})

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def get_requests(request, status):
	current_user = request.user.id
	customer = User.objects.get(id=current_user)
	get_requests = Request.objects.filter(customer=customer, status=status.lower())
	return render(request, "customer/get_requests.html", context={"get_requests": get_requests, "status":status})

@login_required(login_url='login')
def view_request(request, id):
	view_request = Request.objects.get(id=id)
	if view_request is not None:
		return render(request, "customer/view_request.html", context={"request":view_request})
	else:
		return HttpResponseForbidden("The request is not found")


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def new_request(request):
	current_user = request.user.id
	customer = User.objects.get(id=current_user)
	
	if request.method == "POST":
		form = RequestForm(request.POST)
		if form.is_valid():
			sender_BIC=request.POST['sender_BIC']
			sender_name=request.POST['sender_name']
			receiver_BIC=request.POST['receiver_BIC']
			receiver_name=request.POST['receiver_name']
			request_description=request.POST['request_description']
			#bank_name=request.POST['bank_name']
			#transaction_number=request.POST['transaction_number']
			request = Request.objects.create(
				sender_BIC=sender_BIC, 
				sender_name=sender_name, 
				receiver_BIC=receiver_BIC,
				receiver_name=receiver_name, 
				request_description=request_description, 
				#bank_name=bank_name, 
				#transaction_number=transaction_number, 
				status = "pending",
				customer = customer,
				created_date = datetime.now())
			request.save()
			return redirect("confirmation")
		else:
			messages.error(request, "Unsuccessful. Invalid information.")
	if request.method == "GET":
		form = RequestForm()
	return render(request, "customer/new_request.html", context={"request_form":form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def confirmation(request):
	return render(request, "customer/confirmation.html")