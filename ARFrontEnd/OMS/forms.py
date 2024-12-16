from django import forms
# from .models import Strategy

# class StrategyForm(forms.ModelForm):
#     class Meta:
#         model = Strategy
#         fields = [
#             'id', 'user_id', 'client_id', 'name', 'active', 'portfolio'
#         ]
        
#         widgets = {
#             'id': forms.HiddenInput(),
#             'user_id': forms.NumberInput(attrs={'class': 'form-control'}),
#             'client_id': forms.TextInput(attrs={'class': 'form-control'}),
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#             'portfolio': forms.TextInput(attrs={'class': 'form-control'}),
#         }

#     created_at = forms.DateTimeField(
#         widget=forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
#         required=False
#     )
    
#     updated_at = forms.DateTimeField(
#         widget=forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
#         required=False
#     )