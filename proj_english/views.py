"""
Файл, в котором находятся функции для генерации
страниц сайта (views).
"""
from random import randint
from django.shortcuts import render, redirect
from .csv_work import get_csv_count, get_from_csv, write_word, delete_word


def index(request):
    """Функция, которая выводит главную страницу"""
    tests_count = get_csv_count("tests")
    theory_count = get_csv_count("theory")
    words_count = get_csv_count("words")
    context = {
        "tests_count": tests_count,
        "theory_count": theory_count,
        "words_count": words_count
    }
    return render(request, "index.html", context=context)


def words_learn(request):
    """Функция, которая выводит страницу с изучением слов"""
    word_id = request.GET.get('word_id', 0)
    word_id = int(word_id)
    if not word_id:
        words_count = get_csv_count("words")
        word_id = randint(1, words_count)
        return redirect(f'/words-learn?word_id={word_id}')

    show_translation = bool(request.GET.get('translation', None))

    word = get_from_csv("words")[word_id-1]
    context = {
        "word": word,
        "show_translation": show_translation
    }
    return render(request, "words_learn.html", context=context)


def words_list(request):
    """Функция, которая выводит список слов"""
    words = get_from_csv("words")
    return render(request, "words_list.html", context={"words": words})


def words_add(request):
    """Функция, которая выводит форму для добавления слова"""
    return render(request, "words_add.html")


def words_delete(request):
    """Функция, с помощью которой удаляется слово из CSV файла"""
    if request.method == "POST":
        word_id = request.GET.get("id")
        word_id = int(word_id) - 1
        delete_word(word_id)
        return redirect('/words-list')
    return render(request, "words_delete.html")


def words_send(request):
    """Функция, обрабатывающая запрос на добавление слова в CSV файл"""
    if request.method == "POST":
        word = request.POST.get("word").strip(" ")
        translation = request.POST.get("translation").strip(" ")
        comment = request.POST.get("comment", "-").strip(" ")
        context = {}
        if len(word) == 0:
            context["success"] = False
            context["comment"] = "Слово не должно быть пустым"
        elif len(translation) == 0:
            context["success"] = False
            context["comment"] = "Перевод не должен быть пустым"
        else:
            context["success"] = True
            context["comment"] = "Новое слово добавлено"
            write_word(word, translation, comment)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "words_request.html", context)
    return words_add(request)


def theory_list(request):
    """Функция, выводящая список уроков"""
    theory = get_from_csv("theory")
    return render(request, "theory_list.html", context={"theory": theory})


def theory_details(request):
    """Функция, выводящая текст урока"""
    theory_id = request.GET.get("id")
    theory_id = int(theory_id) - 1
    theory = get_from_csv("theory")[theory_id]
    return render(request, "theory_details.html", context={"theory": theory})


def tests_list(request):
    """Функция, выводящая список упражнений для тренировки"""
    tests = get_from_csv("tests")
    return render(request, "tests_list.html", context={"tests": tests})


def tests_details(request):
    """
    Функция, выводящая текст упражнения и форму для проверки ответа.
    Так же проверяет, является ли ответ правильным,
    если он был отправлен.
    """
    test_id = request.GET.get("id")
    test_id = int(test_id) - 1
    test = get_from_csv("tests")[test_id]

    user_answer = ""
    answer_right = False
    if request.method == "POST":
        user_answer = request.POST.get('answer')
        if user_answer == test[3]:
            answer_right = True

    context = {
        "test": test,
        "user_answer": user_answer,
        "answer_right": answer_right
    }

    return render(request, "tests_details.html", context=context)
