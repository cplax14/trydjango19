from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from urllib import quote_plus
from django.utils import timezone
from django.db.models import Q
# Create your views here.

from .models import Post
from .forms import PostForm

def posts_create(request):

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Succesfully created.")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Form not valid.")
	# if request.method == 'POST':
	# 	print request.POST.get("content")
	context = {"form": form}
	#context = {"title": "List"}
	return render(request,"post_form.html",context)

def posts_detail(request,slug=None):
	#instance = Post.objects.get(id=4)
	instance = get_object_or_404(Post,slug=slug)
	if instance.draft or instance.publish > timezone.now().date():
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content)
	#instance = get_object_or_404(Post,title='New Post')
	context = {"title": instance.title, "instance": instance,
		"share_string":share_string}
	#return render(request,"index.html",context)
	return render(request,"post_detail.html",context)

def posts_list(request):
	#return HttpResponse("<h1>List</h1")
	# if request.user.is_authenticated():
	# 	context = {"title": "My User List"}
	# else:
	# 	context = {"title": "List"}
	#queryset_list = Post.objects.filter(draft=False).filter(publish__lte=timezone.now())#.order_by("-timestamp")
	today = timezone.now().date()
	queryset_list = Post.objects.active()
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query) |
			Q(user__first_name__icontains=query) |
			Q(user__last_name__icontains=query) 
			).distinct()
	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page

	page_request_var = 'page'
	page = request.GET.get(page_request_var)
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list" : queryset,
		"title": "List",
		"page_request_var":page_request_var,
		"today":today}
	
	return render(request,"post_list.html",context)

def posts_update(request, slug=None):		
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post,slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title, 
		"instance": instance,
		"form":form}
	#return render(request,"index.html",context)
	return render(request,"post_form.html",context)
	

def posts_delete(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	
	return redirect("posts:list")

def listing(request):
    contact_list = Contacts.objects.all()


    return render(request, 'list.html', {'contacts': contacts})