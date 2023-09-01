from django import forms


class AdvertisementForm(forms.Form):
    # заданием поле для названия
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    # задаем поле для описания
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
    # задаем поле для цены
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
    # задаем поле для торга
    auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    # задаем поле для изображения
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))