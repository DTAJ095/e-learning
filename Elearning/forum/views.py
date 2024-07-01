from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Forum, Thread, Reply

@login_required
def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'forum/forum_list.html', {'forums': forums})

@login_required
def thread_list(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    threads = forum.threads.all()
    return render(request, 'forum/thread_list.html', {'forum': forum, 'threads': threads})

@login_required
def thread_detail(request, forum_id, thread_id):
    thread = get_object_or_404(Thread, id=thread_id, forum_id=forum_id)
    replies = thread.replies.all()
    return render(request, 'forum/thread_detail.html', {'thread': thread, 'replies': replies})

@login_required
def create_thread(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        thread = Thread.objects.create(title=title, content=content, forum=forum, author=request.user)
        return redirect('thread_detail', forum_id=forum.id, thread_id=thread.id)
    return render(request, 'forum/create_thread.html', {'forum': forum})

@login_required
def create_reply(request, forum_id, thread_id):
    thread = get_object_or_404(Thread, id=thread_id, forum_id=forum_id)
    if request.method == 'POST':
        content = request.POST['content']
        reply = Reply.objects.create(content=content, thread=thread, author=request.user)
        return redirect('thread_detail', forum_id=thread.forum.id, thread_id=thread.id)
    return render(request, 'forum/create_reply.html', {'thread': thread})
