from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'time_to_complete']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome da tarefa'}),
            'time_to_complete': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tempo em minutos'}),
        }
