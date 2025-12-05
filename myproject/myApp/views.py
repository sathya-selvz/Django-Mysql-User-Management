from django.shortcuts import render, redirect, get_object_or_404
from .models import UserData, UserProfile


def get_user_details(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        address = request.POST.get('address')
        contact = request.POST.get('contact')

       
        user = UserData.objects.create(
            name=name,
            email=email,
            age=age
        )

       
        UserProfile.objects.create(
            user=user,
            address=address,
            contact=contact
        )

        return redirect('display_user_data')

    return render(request, 'myapp/user_details_form.html')


def display_user_data(request):
    profiles = UserProfile.objects.select_related('user').all()
    return render(request, 'myapp/user_data_table.html', {
        'profiles': profiles
    })

def edit_user(request, user_id):
    user = get_object_or_404(UserData, id=user_id)
    profile = get_object_or_404(UserProfile, user=user)

    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.age = request.POST.get('age')
        user.save()

        profile.address = request.POST.get('address')
        profile.contact = request.POST.get('contact')
        profile.save()

        return redirect('display_user_data')

    return render(request, 'myapp/edit_user_form.html', {
        'user': user,
        'profile': profile
    })


def delete_user(request, user_id):
    user = get_object_or_404(UserData, id=user_id)
    user.delete()
    return redirect('display_user_data')
