from django.shortcuts import render

from app1.models import Worcker


def index_page(request):
    """
worcker_to_cange = Worcker.objects.get(id=5)    доступ к объекту БД по id запись в переменную
    print(worcker_to_cange)                     печать переменной в теминале
    """

    """
    worcker_to_cange.second_name = 'Задира'     изменения 
    worcker_to_cange.save()
    """

    """
    all_worckers = Worcker.objects.all()                        получение списка всех строк из БД QuerySet
    print(all_worckers)                                         печать переменной в теминале
    """

    """
    worckers_filtered = Worcker.objects.filter(salary=60000)    получение отфильтрованных значений из БД
    print(worckers_filtered)                                    печать переменной в теминале
    """

    """
    all_worckers = Worcker.objects.all()                                                получение значения полей
    for i in all_worckers:
        print(i.second_name, i.name}, i.salary, i.id})
        print(f'Фамилия:{i.second_name}, Имя:{i.name}, зарплата:{i.salary}, ID:{i.id}')
    """

    """
    Worcker.objects.get(id=5).delete                            удаление по id
    """
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')
