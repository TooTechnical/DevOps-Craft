from django.shortcuts import render

def list_services(request):
    # Sample data for services (replace with database query later)
    services = [
        {'id': 1, 'name': 'Web Development', 'description': 'Build modern websites', 'price': 500},
        {'id': 2, 'name': 'Digital Marketing', 'description': 'Grow your online presence', 'price': 300},
    ]
    return render(request, 'services/list.html', {'services': services})
