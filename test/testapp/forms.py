from django import forms
from .models import (
    Clients,
    Equipment,
    Modes,
)


class DurationsForm(forms.Form):
    client = forms.ModelChoiceField(
        empty_label='Все',
        queryset=Clients.objects.all(),
        label='Клиент',
        blank=True,
        required=False,
    )
    equipment = forms.ModelChoiceField(
        empty_label='Все',
        queryset=Equipment.objects.all(),
        label='Оборудование',
        blank=True,
        required=False,
    )
    mode = forms.ModelChoiceField(
        empty_label='Все',
        queryset=Modes.objects.all(),
        label='Режим',
        blank=True,
        required=False,
    )
    minutes = forms.IntegerField(
        label='Продолжительность',
        min_value=0,
        widget=forms.NumberInput,
        required=False,
    )
    start = forms.DateField(
        label='Дата начала',
        widget=forms.SelectDateWidget(years=range(2015, 2025)),
        required=False,
    )
    stop = forms.DateField(
        label='Дата окончания',
        widget=forms.SelectDateWidget(years=range(2015, 2025)),
        required=False,
    )
    hour_start = forms.IntegerField(
        label='Время начала, номер часа',
        widget=forms.NumberInput,
        required=False,
        min_value=0,
        max_value=23,
    )
    hour_stop = forms.IntegerField(
        label='Время окончания, номер часа',
        widget=forms.NumberInput,
        required=False,
        min_value=0,
        max_value=23,
    )



