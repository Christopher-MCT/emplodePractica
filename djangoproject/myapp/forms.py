from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de la tarea", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField(label='Descripción de la Tarea', widget= forms.Textarea(attrs={'class':'textarea'}))
    
class CreateNewProject(forms.Form):
    name=forms.CharField(label='Nombre del proyecto', max_length=200, widget=forms.TextInput(attrs={'class':'input'}))