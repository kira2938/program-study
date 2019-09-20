from django import forms
from .models import AreaData

class StForm(forms.Form):
    station = forms.ModelChoiceField(queryset=AreaData.objects.all(), widget=forms.RadioSelect(), empty_label=None)
    


class CreateForm(forms.ModelForm):
    class Meta:
        model = AreaData
        fields = '__all__'
        labels = {
                'area_list': 'エリア',
                'list_jpen': 'エリア(英語）',
                'list_id': 'リストid',
                }
        widgets = {
                'area_list': forms.TextInput(attrs={'placeholder': '例)大崎'}),
                'list_jpen': forms.TextInput(attrs={'placeholder': '例)osaki'}),
                }
    
