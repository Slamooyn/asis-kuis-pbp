from django.shortcuts import render
from main.models import Experience


def show_main(request):
    context = {
        'name': 'Muhammad Salman Fahri',
        'npm': '2206000000',
        'study_program': 'S1 Sistem Informasi',
        'bio': 'Mahasiswa Sistem Informasi Universitas Indonesia yang tertarik pada pengembangan web full-stack dan rekayasa perangkat lunak.',
    }
    return render(request, 'index.html', context)


def show_experience(request):
    experience_list = Experience.objects.all()
    context = {
        'name': 'Muhammad Salman Fahri',
        'experience_list': experience_list,
    }
    return render(request, 'experience.html', context)