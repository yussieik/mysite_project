from django.shortcuts import render
from django.urls import reverse
from datetime import date
from .models import Post, Author
from .forms import CommentForm, CustomUserCreationForm
from django.views.generic import ListView, DetailView, CreateView


class SignUpView(CreateView):

    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    # success_url = 'login'

    def get_success_url(self):
        return reverse('login')


class HomepageView(ListView):

    model = Post
    template_name = 'homepage.html'
    context_object_name = 'posts'
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = date.today()
        return context


class AuthorsView(ListView):

    model = Author
    template_name = 'authors.html'
    context_object_name = 'authors'


class AuthorPostsView(DetailView):

    model = Author
    template_name = 'author_posts.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        context['posts'] = author.posts.all()
        return context


def post_details(request, id):

    post = Post.objects.get(id=id)
    comments = post.comment_set.all()

    comment_form = CommentForm() # Empty form

    if request.method == 'POST':
        # II - POST mode 
        filled_comment_form = CommentForm(request.POST) # Filled Form
        filled_comment_form.save()


    context = {'post': post, 'comments': comments, 'form': comment_form}

    return render(request, 'post.html', context)










# # Create your views here.
# def homepage(request):

#     # render
#     # - request object
#     # - template_name -> html name ('homepage.html')
#     # - context -> dictionary of data

#     all_posts = Post.objects.all().order_by('-date_created') # All of the posts

#     context = {'time': date.today(), 'posts': all_posts}
#     return render(request, 'homepage.html', context)

# def authors(request):
    
#     all_authors = Author.objects.all()
#     context = {'authors': all_authors}

#     return render(request, 'authors.html', context)


# # Gets all posts of a specific author
# def author_posts(request, id):

#     author = Author.objects.get(id=id)
#     author_posts = author.posts.all()
    
    # context = {'author': author, 'posts': author_posts}

#     return render(request, 'author_posts.html', context)
