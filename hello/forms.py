from django import forms

#フォームをまとめて定義できる。
#これで
class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.CharField(label='age')

    # forms.CharField -> テキストを入力するフォーム
    # forms.IntegerField -> 整数の値を入力するフォーム
