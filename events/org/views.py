from django.shortcuts import render,HttpResponse,redirect
from org . models import Post,orgcomment
from django.contrib import messages
from org.templatetags import extras

# Create your views here.
def orghome(request):
    allPosts=Post.objects.all
    context={'allPosts':allPosts}
    return render(request,'org/orghome.html',context)
   # return HttpResponse('this is orghome all posts here')

def orgpost(request, slug):
    post=Post.objects.filter(slug=slug).first()
    comments=orgcomment.objects.filter(post=post,parent=None)
    replies=orgcomment.objects.filter(post=post).exclude(parent=None) 
    repDict={}
    for reply in replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno]=[reply]
        else:
            repDict[reply.parent.sno].append(reply)    
    print(repDict) 
    
    context={'post':post,'comments':comments,'user':request.user, 'repDict':repDict}
    return render(request,'org/orgpost.html',context)
    #return HttpResponse(f'This is orgpost: {slug}')

def postComment(request):
    if request.method=="POST":
        
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post =Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno=="":
            comment=orgcomment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
   
        else:
            parent=orgcomment.objects.get(sno=parentSno)
            comment=orgcomment(comment=comment,user=user,post=post,parent=parent)
                
        #comment = orgcomment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
    return redirect(f"/org/{post.slug}")
    
    #post=Post.objects.filter(slug=slug).first 
    #context={'post':post}
    #return render(request,'org/orgpost.html',context)
    