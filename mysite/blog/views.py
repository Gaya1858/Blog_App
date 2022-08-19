from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView
from .forms import EmailPostForm

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
# Create your views here.
# def post_list(request):
#     posts = Post.published.all()
#     return render(request, 'blog/post/list.html' ,{'posts': posts},)

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)

    return render(request, 'blog/post/details.html', {'post': post})

'''
    Handles the email forma and sends an email when its successfully submittted
'''
def post_share(request, post_id):
     # Retrieve post byt id
    post = get_object_or_404(Post, id=post_id, status ='published')
    # use the below line if you use your SMTP server for sending emails

    if request.method == 'POST':
        # form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed  validation, then you use the below form.cleaned_data to access the form data.
            cd = form.cleaned_data
            # use the below code if you choose to setup your own SMTP server
            # post_url = request.build_absolute_uri(post.get_absolute_url())
            # subject = f'{cd.name} recommends you read {post.title}'
            # message = f'Read {post.title} at {post_url}\n\n {cd.name}\'s comments: {cd.comments}'
            # send_mail (subject, message, 'admin@myblog.com', cd.to)
            # sent = True
            # send email
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html',{'post':post, 'form': form})
#   this is for your own SMTP server
#   return render(request, 'blog/post/share.html',{'post':post, 'form': form}, 'sent':sent)


