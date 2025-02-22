from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Task

def index(request):
    return render(request, 'pages/index.html')

def search(request):
    query = request.POST.get('q', '')
    page_number = request.POST.get('page', 1)
    
    tasks = Task.objects.filter(title__icontains=query).order_by('-created_at')
    paginator = Paginator(tasks, 10)  # 10 tasks per page
    page = paginator.get_page(page_number)
    
    if request.headers.get('HX-Request'):  # Changed from request.htmx
        if 'hx-trigger' in request.headers and request.headers['hx-trigger'] == 'intersect':
            # This is a scroll request
            return render(request, 'components/task_list.html', {'page': page})
        # This is a search request
        return render(request, 'components/results.html', {'page': page})
        
    return render(request, 'pages/search.html', {'page': page})

def validate_title(request):
    title = request.POST.get('title', '')
    if len(title) < 3:
        return HttpResponse(
            '<span class="text-red-600">Title must be at least 3 characters long</span>'
        )
    if Task.objects.filter(title=title).exists():
        return HttpResponse(
            '<span class="text-red-600">A task with this title already exists</span>'
        )
    return HttpResponse(
        '<span class="text-green-600">Title is valid</span>'
    )

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        if len(title) < 3:
            return HttpResponse(
                '<div class="text-red-600">Title must be at least 3 characters long</div>',
                status=422
            )
            
        task = Task.objects.create(
            title=title,
            description=description
        )
        
        # Get updated task list
        tasks = Task.objects.all().order_by('-created_at')
        paginator = Paginator(tasks, 10)
        page = paginator.get_page(1)
        
        return render(request, 'components/results.html', {'page': page})