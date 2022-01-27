
from django import forms
from . models import User

class StudentRegistration(forms.ModelForm):
    # this is high priority 
    # name=forms.CharField(max_length=10,min_length=5,required=True)
    class Meta:
        model=User
        fields=['name','email','password']
        labels={'name':'Enter Name','email':'Enter Email','password':'Pass'}
        # help_texts={'name':'enter your name here','email':'enter your email here'}
        # error_messages={
        #     'name':{'required':'name is necessary'},
        #     'password':{'required':'password is manadatory'},
        #     }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'write your name'}),
          
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'write your email'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),

            }




