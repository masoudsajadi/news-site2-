from django.shortcuts import render, redirect 
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UpdateUserForm, UpdateProfileForm
from blog.models import Post, Category
from .forms import SimplePostForm


def home(request):
    return render(request, 'users/home.html')




class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})





# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)





@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})



@login_required
def upload_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        short_description = request.POST.get('short_description')
        content = request.POST.get('content')
        banner_path = request.FILES.get('banner_path')
        category_id = request.POST.get('category')  # Get the selected category ID

        # Create and save the post
        post = Post(
            user=request.user,
            title=title,
            short_description=short_description,
            content=content,
            banner_path=banner_path,
            category=Category.objects.get(id=category_id)  # Get the category instance
        )
        post.save()
        messages.success(request, 'Post uploaded successfully!')
        return redirect(to='users/profile.html')  # Replace with your success URL
    else:
        categories = Category.objects.all()  # Get all categories to display in the form
        return render(request, 'users/upload_post.html', {'categories': categories})











""" 
@login_required
def upload_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        short_description = request.POST['short_description']
        content = request.POST['content']
        banner_path = request.FILES['banner_path']
        meta_keywords = request.POST['meta_keywords']
        slug = request.POST['slug']
        seotitle = request.POST.get('seotitle', "")
        seo_description = request.POST.get('seo_description', "")
        seo_script = request.POST.get('seo_script', "")
        status = 'status' in request.POST

        post = Post(
            user=request.user,
            title=title,
            short_description=short_description,
            content=content,
            banner_path=banner_path,
            meta_keywords=meta_keywords,
            slug=slug,
            seotitle=seotitle,
            seo_description=seo_description,
            seo_script=seo_script,
            status=status
        )
        post.save()
        return redirect('success_url')  

    return render(request, 'upload_post.html' ) """
 

""" 
@login_required
def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Create the post instance but do not save it yet
            post = form.save(commit=False)
            post.user = request.user  # Set the user to the current logged-in user
            
            # Get the category from the form data
            category = request.POST.get('name')
            post.category = category.name  # Assuming the Post model has a category field
            
            post.save()  # Now save the post to the database
            messages.success(request, 'Post uploaded successfully!')
            return redirect('success_url')  # Redirect to a success page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PostForm()  # Create an empty form for GET requests

    return render(request, 'users/upload_post.html', {'form': form})


 """














""" def upload_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            category = request.POST.get('category')
            post = PostForm.('category' = category)
            post = form.save(commit=False)  # Do not save yet
            post.user = request.user  # Set the user to the current logged-in user
            post.save()  # Now save the post to the database
            messages.success(request, 'Post uploaded successfully!')
            return redirect('success_url')  # Redirect to a success page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PostForm()  # Create an empty form for GET requests

    return render(request, 'users/upload_post.html', {'form': form})

 """
    