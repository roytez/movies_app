from django.forms import ModelForm


class AppBaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppBaseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
