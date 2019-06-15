from .models import profile,blog
from django import forms


class profileform(forms.ModelForm):
    class Meta():
        model = profile
        fields = "__all__"

class blogform(forms.ModelForm):
    class Meta():
        model = blog
        fields = ['blogdata']
