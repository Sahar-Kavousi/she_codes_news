from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import NewsStory, Comment
from .forms import StoryForm, CommentForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()[3:]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by(
            "-pub_date")[:3]
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]

        form = CommentForm()
        post = get_object_or_404(NewsStory, pk=pk)
        comments = post.comments.all()

        context['story'] = post
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = NewsStory.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comments.all()

        context['story'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['text']

            comment = Comment.objects.create(
                name=name, email=email, text=content, story=post
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)


class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StoryUpdateView(UpdateView):
    # specify the model you want to use
    model = NewsStory
    form_class = StoryForm
    template_name = 'news/updateStory.html'
    # specify the fields
    # fields = [
    #     "title",
    #     "content",
    #     "image"
    # ]

    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = "/news/"
