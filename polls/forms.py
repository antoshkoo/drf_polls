from django.forms import ModelForm

from .models import Poll


class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ('id', 'name', 'date_start', 'date_end', 'description')



