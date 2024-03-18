In views.py, add
```
def update_user(request):
    # If user is authenticated, get the current user
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id) # Gives you the currently logged in user
        user_form = UpdateUserForm(request.POST or None, instance=current_user) # The profile for the current user is pre-filled
        # If form is valid, save the form
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "Your profile has been updated successfully!")
        return render(request, 'core/update_user.html', {'user_form': user_form})
    # Else, return an error message
    else:
        messages.success(request, 'You must be logged in to access the page')
        return redirect('index')
```

In forms.py
```
class UpdateUserForm(UserChangeForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    
    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
```

Be sure to update urls.py
