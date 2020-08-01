from django.shortcuts import render,get_object_or_404
from TestApp.models import Post, Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.mail import send_mail
from TestApp.forms import EmailSendForm, CommentForm, SignUpForm, FeedbackForm
from django.http import HttpResponseRedirect
from taggit.models import Tag
from django.db.models import Count
from django.contrib.auth.decorators import login_required
# Create your views here.
def list_view(request,tag_slug=None):
    data=Post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        data=data.filter(tags__in=[tag])
    paginator=Paginator(data,3)
    page_number=request.GET.get('page')
    try:
        data=paginator.page(page_number)
    except PageNotAnInteger:
        data=paginator.page(1)
    except EmptyPage:
        data=paginator.page(paginator.num_pages)
    return render(request,"TestApp/list.html",{"data":data,'tag':tag})




def post_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status="published",publish__year=year,publish__month=month,publish__day=day)
    post_tags_ids=post.tags.values_list('id',flat=True)
    similar_posts=Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts=similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','publish')[:4]
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()
    return render(request,"TestApp/post.html",{"post":post,'form':form,'comments':comments,'csubmit':csubmit,'similar_posts':similar_posts})







def mail_view(request,id):
    post=get_object_or_404(Post,id=id,status="published")
    sent=False
    if request.method=="POST":
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject='{}({}) Recommends You To Read"{}"'.format(cd['name'],cd['email'],post.title)
            message='Read Post At: \n {}\n\n{}\'Comments:\n{}'.format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,"s7549692084",[cd["to"]])
            sent=True
    else:
        form=EmailSendForm()
    return render(request,"TestApp/sharebymail.html",{'post':post,'form':form,'sent':sent})


def logout_view(request):
    return render(request,"TestApp/logout.html")


def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'Testapp/signup.html',{'form':form})


def about_view(request):
    return render(request,"TestApp/about.html")



def feedback_view(request):
    form=FeedbackForm()
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank")
    return render(request,"TestApp/feed.html",{"form":form})


def thanks_view(request):
    return render(request,"TestApp/thanks.html")
@login_required
def contact_view(request):
    return render(request,"TestApp/contact.html")
