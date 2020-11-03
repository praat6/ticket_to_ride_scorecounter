from django import forms


class PlayerField(forms.CharField):
    def __init__(self, css_class, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.css_class = css_class


class CreateGameForm(forms.Form):
    red = PlayerField(max_length=100, required=False, css_class='p-3 mb-2 bg-red text-white')
    blue = PlayerField(max_length=100,  required=False, css_class='p-3 mb-2 bg-blue text-white')
    green = PlayerField(max_length=100,  required=False, css_class='p-3 mb-2 bg-green text-white')
    yellow = PlayerField(max_length=100,  required=False, css_class='p-3 mb-2 bg-yellow text-white')
    black = PlayerField(max_length=100, required=False, css_class='p-3 mb-2 bg-black text-white')

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
