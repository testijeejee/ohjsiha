from django.utils import timezone

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Note

class RegisterationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        ]

    def save(self, commit=True):
        user = super(RegisterationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class ModifyNoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ['notetitle', 'notes']

        labels = {
            "notetitle": "Otsikko",
            "notes": "Muistiinpano",
        }

    def save(self, commit=True):
        note = super(ModifyNoteForm, self).save(commit=False)

        note.pub_date = timezone.now()
        note.notetitle = self.cleaned_data['notetitle']
        note.notes = self.cleaned_data['notes']

        if commit:
            note.save()



class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ['notetitle', 'notes']
        labels = {
            "notetitle": "Otsikko",
            "notes": "Muistiinpano",
        }


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(NoteForm, self).__init__(*args, **kwargs)

    def save(self, commit = True):
        note = super(NoteForm, self).save(commit=False)

        note.pub_date = timezone.now()
        note.notetitle = self.cleaned_data['notetitle']
        note.notes = self.cleaned_data['notes']
        note.user = self.user

        if commit:
            note.save()

        return note
