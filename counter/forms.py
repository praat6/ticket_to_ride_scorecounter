from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div


class CreateGameForm(forms.Form):
    red = forms.CharField(max_length=100, required=False, label='Name')
    blue = forms.CharField(max_length=100, required=False, label='Name')
    green = forms.CharField(max_length=100, required=False, label='Name')
    yellow = forms.CharField(max_length=100, required=False, label='Name')
    black = forms.CharField(max_length=100, required=False, label='Name')

    def is_valid(self):
        n_players = 0
        for name, field in self.fields.items():
            value = field.widget.value_from_datadict(self.data, self.files, self.add_prefix(name))
            if value:
                n_players += 1

        if n_players < 2:
            return False
        else:
            return super().is_valid()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(Column('red', css_class='p-3 mb-2 bg-red text-white')),
            Row(Column('blue', css_class='p-3 mb-2 bg-blue text-white')),
            Row(Column('green', css_class='p-3 mb-2 bg-green text-white')),
            Row(Column('yellow', css_class='p-3 mb-2 bg-yellow text-white')),
            Row(Column('black', css_class='p-3 mb-2 bg-black text-white')),
            Div(Submit('submit', 'START!'), css_class='col text-center')
        )
