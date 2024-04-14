from django import forms

class AddReview(forms.Form):
    reviewText = forms.CharField(label="Your review:", max_length= 500)
    reviewRating = forms.IntegerField(label="Your rating:", min_value=0, max_value=10)