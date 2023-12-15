from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views import generic, View
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


@method_decorator(login_required, name='dispatch')
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class StoryUpdateView(View):
    model = NewsStory
    form_class = StoryForm
    template_name = 'news/updateStory.html'
    success_url = "/news/"

    def get(self, request, pk):
        post = get_object_or_404(NewsStory, id=pk, author=request.user)
        form = StoryForm(instance=post)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        post = get_object_or_404(NewsStory, id=pk, author=request.user)
        form = StoryForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})