from django import forms


class PostAdminForm(forms.ModelForm):
    """
    1.required：是否可以为空。required=True 不可以为空，required=False 可以为空
    2.widget=forms.Textarea()  生成Textarea标签。widget默认生成input标签
    """
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)