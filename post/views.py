from django.shortcuts import render
from . models import PostModel
from . forms import PostForm
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
# Create your views here.

def PostListView(request): 
    post=PostModel.objects.order_by('-created_at').all()
    return render(request, 'post.html', {'post':post})
    

def PostAdd(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
        else:
            print(form.errors) 

    return HttpResponseRedirect('/') 

# def index(request):
#     return HttpResponse('<h1>Jeorge</h1>')
    
def PostLikeAdd(request, post_id):

    post_object = PostModel.objects.get(id=post_id)
    post_object.count = post_object.count + 1 
    post_object.save() 
    return HttpResponseRedirect('/')

def PostDelete(request,post_id):
    post=PostModel.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
    
def PostEdit(request,post_id):
    post=PostModel.objects.get(id=post_id)
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else :
            return HttpResponseRedirect('form data invalid')
    else :
        return render(request,'edit.html', {'post':post})
        
            
            
        
    