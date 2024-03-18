In forms.py,
```
from django.contrib.auth.forms import SetPasswordForm

class UpdateUserPassword(SetPasswordForm): 
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(UpdateUserPassword, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
```

In views.py,
```
def update_password(request):
    # If user is authenticated, get the current user
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id) # Gives you the currently logged in user
        if request.method == 'POST':
            form = UpdateUserPassword(current_user, request.POST)
            # If form is valid, save the form
            if form.is_valid():
                form.save()
                login(request, current_user)
                messages.success(request, "Your profile has been updated successfully!")
                return redirect('dashboard')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
        else:
            form = UpdateUserPassword(current_user)
            return render(request, 'core/update_password.html', {'form': form})
    # Else, return an error message
    else:
        messages.success(request, 'You must be logged in to access the page')
        return redirect('index')
```
