from django.shortcuts import render,HttpResponse,redirect
from home.models import contact
from django.contrib import messages
from django.contrib.auth.models import User
from org.models import Post
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'home/home.html')
   

def Contact(request):
    #messages.info(request,'welcome')
    if request.method=='POST':
        
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        collegename = request.POST.get("collegename")
        describe = request.POST.get("describe")
        print (fname,lname,email,collegename,describe)
        
        if len(fname)<2 or len(lname)<2 or len(collegename)<2 or len(describe)<10:
            messages.error(request,"Please fill the form correctly")
            #return redirect('home')
            
            
        else:
            contact_in= contact(fname=fname,lname=lname,email=email,collegename=collegename,describe=describe)
            contact_in.save()
            messages.success(request,"you form has been filled successfully")
            #return HttpResponse(f"Form submitted! First Name: {fname}, Email: {email}")
            #return redirect('home')
    return render(request,'home/contact.html')

def search(request):
    #query = request.get('query', '')
    query=request.GET['query']
    if len(query)>50:
        allPosts=Post.objects.none()
    else:
        allPoststitle=Post.objects.filter(title__icontains=query)
        allPostscontent=Post.objects.filter(content__icontains=query)
        allPosts=allPoststitle.union(allPostscontent)
        
        
    if allPosts.count() == 0: 
         messages.warning(request,"No search results found. Please refine your query.")    
    params={'allPosts': allPosts,'query': query}
    return render(request,'home/search.html',params)
    #return HttpResponse('This is search')
    
def handleSignup(request):
    if request.method=="POST":
        #Get the post prameters
        username=request.POST['username']
        fullname=request.POST['fullname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        #errors
        if len(username)>20:
            messages.error(request,"Username must be under 20 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request,"Username must only contain letters and numbers")
            return redirect('home')
        if password1 !=password2:
            messages.error(request,"Psswords don't match")
            return redirect('home')
            
        
        #user
        myuser=User.objects.create_user(username,email,password1)
        myuser.full_name=fullname
        myuser.save()
        messages.success(request,"Your account has been successfully created!!!")
        return redirect('home')
    else:
        return HttpResponse('404 - not found')        
def handleLogin(request):
    if request.method=="POST":
        username1=request.POST['username1']
        pass1=request.POST['pass1']
        
        user=authenticate(username=username1,
        password=pass1)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in!")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials ,please try again")
            return redirect('home')
    
    return HttpResponse('404- not found')




def handleLogout(request):
    #if request.method=="POST":
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect('home')
        
    
    return HttpResponse('handleLogout')
        


def about(request):
    return render(request,'home/about.html')
    