from django.shortcuts import render
from main.models import Experience
from main.models import Achievement

def show_main(request):
    context = {
        'name': 'Muhammad Salman Fahri',
        'npm': '2206000000',
        'study_program': 'S1 Sistem Informasi',
        'bio': 'Mahasiswa Sistem Informasi Universitas Indonesia yang tertarik pada pengembangan web full-stack dan rekayasa perangkat lunak.',
    }
    return render(request, 'index.html', context)


def show_experience(request):
    experience_list = Experience.objects.all().filter(category = 'internship')
    context = {
        'name': 'Muhammad Salman Fahri',
        'experience_list': experience_list,
    }
    return render(request, 'experience.html', context)


def show_achievement(request) :
    achievement_list = Achievement.objects.all().order_by('-achieved_at')
    context = {
        'name' : 'Muhammad Salman Fahri',
        'achievement_list' : achievement_list
    }
    return render(request,'achievement.html',context)