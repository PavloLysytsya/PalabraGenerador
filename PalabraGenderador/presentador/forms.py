from django import forms

from .models import Vocabulary


class VocabularyForm(forms.ModelForm):

    class Meta:
        model = Vocabulary
        fields = ('word', 'spanish_word', 'native_language')
