from django import forms

from pybo.models import Question, Answer, Comment



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content', 'photo']
        labels = {
            'subject': '제목',
            'content': '내용',
            'photo' : '사진',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }



class QuestionFormWithPhoto(forms.ModelForm):
    photo = forms.ImageField(required=False)  # Add the photo field

    class Meta:
        model = Question
        fields = ['subject', 'content', 'photo']  # Include the photo field in the fields list
        labels = {
            'subject': '제목',
            'content': '내용',
            'photo' : '사진',
        }
