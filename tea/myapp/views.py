from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from .models import Tea
from .alg import match
import telebot


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


def handle_uploaded_file(f):
    with open('myapp/csv.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def time_and_place(request):
    if request.method == 'GET':
        return render(request, 'time_and_place.html')
    else:
        try:
            global time, place
            time = request.POST['time'].split(',')
            place = request.POST['place'].split(',')
            user = match()
            print(time, place)
            if len(time) * len(place) < len(user):
                messages.info(request, 'Мало мест и времени. Добавьте чуть больше мест или времени')
                HttpResponseRedirect('/test')
            else:
                d = {'table': [(place[i % len(place)], time[i // len(place)], user[i][0], user[i][1]) for i in
                               range(len(user))]}
                return render(request, 'tea.html', d)
        except:
            names = request.POST['names'].split(',')
            times = request.POST['times'].split(',')
            places = request.POST['places'].split(',')
            names = [(names[i * 2], names[i * 2 + 1]) for i in range(len(names) // 2)]
            ans = []
            for i in range(len(times)):
                t = Tea()
                t.user_1 = names[i][0]
                t.user_2 = names[i][1]
                t.place = places[i]
                t.time = times[i]
                ans.append((t.user_1, t.user_2, t.place, t.time))
                t.save()
            telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}
            bot = telebot.TeleBot(token="1008644876:AAHdPfzbXGiq5WpX9IJyKVxoGnK4wYXRZ0w")
            for i in ans:
                bot.send_message(542658693, '{}, вместе с {}, в {}, в {}'.format(*i))
            return redirect('/test')


def test(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        print(request.POST['login'])
        print(request.POST['password'])
        return redirect('/')


def index(request):
    if request.method == 'GET':
        return render(request, 'test.html')
    else:
        if request.FILES:
            handle_uploaded_file(request.FILES['file'])
            return redirect('/time_and_place')
        else:
            messages.info(request, 'Вставьте файл.')
            return HttpResponseRedirect('/test')


def tea(request):
    if request.method == 'GET':
        global time, place
        print('test')
        user = match()
        if len(time) * len(place) < user:
            messages.info(request, 'Мало мест и времени. Добавьте чуть больше мест или времени')
            HttpResponseRedirect('/test')
        else:
            d = {'table': [(time[len(place) // i], place[len(place) % i], user[i][0], user[i][1]) for i in
                           range(len(user))]}
            return render(request, 'tea.html', d)
    else:
        names = request.POST['names'].split(',')
        times = request.POST['times'].split(',')
        places = request.POST['places'].split(',')
        names = [(names[i * 2], names[i * 2 + 1]) for i in range(len(names) // 2)]
        ans = []
        for i in range(len(times)):
            t = Tea()
            t.user_1 = names[i][0]
            t.user_2 = names[i][1]
            t.place = places[i]
            t.time = times[i]
            ans.append((t.user_1, t.user_2, t.place, t.time))
            t.save()
        telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}
        bot = telebot.TeleBot(token="1008644876:AAHdPfzbXGiq5WpX9IJyKVxoGnK4wYXRZ0w")
        for i in ans:
            bot.send_message(542658693, '{}, вместе с {}, в {}, в {}'.format(*i))
        return redirect('/')
