from django import forms
from .models import Folder,File

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parent']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        parent_locked = kwargs.pop('parent_locked', False)
        super().__init__(*args, **kwargs)
        if parent_locked:
            self.fields['parent'].widget = forms.HiddenInput()


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file','folder']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            
        }

    def __init__(self, *args, **kwargs):
        folder_locked = kwargs.pop('folder_locked', False)
        super().__init__(*args, **kwargs)
        if folder_locked:
            self.fields['folder'].widget = forms.HiddenInput()

    def clean_file(self):
        uploaded_file = self.cleaned_data.get('file')
        if uploaded_file:
            file_size = uploaded_file.size
            min_size = 1 * 1024  # 10MB in bytes
            max_size = 50 * 1024 * 1024  # 50MB in bytes

            if file_size < min_size:
                raise forms.ValidationError("حجم فایل نباید کمتر از ۱ مگابایت باشد.")
            if file_size > max_size:
                raise forms.ValidationError("حجم فایل نباید بیشتر از ۵۰ مگابایت باشد.")

        return uploaded_file

            