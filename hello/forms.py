from django import forms

#フォームをまとめて定義できる。
#これで
class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.CharField(label='age')

#プルダウンの書き方も一応ここに記しておく
class HelloForm2(forms.Form):
    data = [
        ('one', 'item1'),
        ('two', 'item2'),
        ('three', 'item3'),
        ('four', 'item4'),
    ]
    choice = forms.MultipleChoiceField(label='radio', choices=data, widget=forms.Select(attrs={'size':4}))


# forms.CharField -> テキストを入力するフォーム
# forms.IntegerField -> 整数の値を入力するフォーム
