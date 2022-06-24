from django.forms import ModelForm
from .models import Article ,Comment , Gallery

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
    
    
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'
    
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'





        