from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm, SearchForm

from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html' , { 'tweets' : tweets})

@login_required # wrap the view inside this condition or more function(method)
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user #add user in the the tweet model form
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
        return render(request, 'tweet_form.html', { 'form' : form })

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet) # instance modify existing
        if form.is_valid():
            form.save() # no need to assign user manually because we are updating existing one
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
        return render(request, 'tweet_form.html', { 'form' : form })
    
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    else:
        return render(request, 'tweet_confirm_delete.html', { 'tweet' : tweet })

#we only made registration view because it is unique for each website
#so django doens't provide by default
#but login logout are provided by django don't need write
#since it is same for all websites
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1']) #so that we need only password1
            user.save()
            login(request, user) # automatically login
            return redirect('tweet_list')
    else:            
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', { 'form' : form })
    
def search(request):
    form = SearchForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['text']
        tweets = get_list_or_404(Tweet, text__icontains=text)
    else:
        tweets = []
    return render(request, 'search.html', {'tweets': tweets})