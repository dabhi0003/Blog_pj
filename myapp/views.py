from django.shortcuts import render,redirect
from .models import PostModel,Comment, User
from .forms import PostModelform,PostUpdate_Form,CommentForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    posts=PostModel.objects.all()
    if request.method=="POST":
        form=PostModelform(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            form.save()
            return redirect('index')
    else:
        form=PostModelform()
    context={
        'posts':posts,'form':form
    }
    return render(request,'index.html',context)

@login_required
def post_detail(request,id):
    post=PostModel.objects.get(id=id)
    
    if request.method=="POST":
        print(request.POST)
        c_form=CommentForm(request.POST)
        instance = c_form.save(commit=False)
        instance.user=request.user
        instance.post=post
        instance.save()
        c_form.save()
        return redirect('post_details',id=id)
    else:
        c_form=CommentForm()

    context={
        'post':post,
        'c_form':c_form, 
    }
    return render(request,'post_details.html',context)

@login_required
def post_edit(request,id):
    post=PostModel.objects.get(id=id)
    if request.method=="POST":
        form=PostUpdate_Form(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_details',id=id)
    else:
        form=PostUpdate_Form(instance=post)
    context={
        'post':post,
        'form':form,
    }
    return render(request,'post_edit.html',context)

@login_required
def post_delete(request,id):
    post=PostModel.objects.get(id=id)
    if request.method=="POST":
        post.delete()
        return redirect("index")
    context={
        'post':post
    }
    return render(request,"post_delete.html",context)