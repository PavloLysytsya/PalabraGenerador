from django.shortcuts import render
from .forms import VocabularyForm
import pandas as pd
import sqlite3
import os


def home(request):
    return render(request, 'presentador/base.html')


def presentation(request):
    dbpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db.sqlite3')
    conn = sqlite3.connect(dbpath)
    sql = """
        select *
from top2000nouns n
left join top2000nouns_phrases p
on n.id = p.vocabulary_id
    """
    df = pd.read_sql(sql, con=conn)
    spanishwords = list(df['spanish'])
    englishwords = list(df['english'])
    #data = {1: 'text0', 2: 'text1'}
    sounds = {1: '/static/mp3/sound0.mp3', 2: '/static/mp3/sound1.mp3'}
    return render(request, 'presentador/presentation.html', {
        'spanishwords': spanishwords,
        'englishwords': englishwords,
        'sounds': sounds
        })


def post_new(request):
    form = VocabularyForm()
    return render(request, 'presentador/post_edit.html', {'form': form})