# django_tutorial

Steps on building an saas boilerplate consisting of the following functions:
- Login, logout, register
- Update user profile
- Update password
  - Check if user is authenticated
  - Get the current user
  - Check if it's POST
  - Pass the form variable into the backend into forms.py
  - Check if the form is valid
  - Save the form, log the user in, return somewhere
  - If it's a GET, show the form
  - If user is not logged in, show an error
- Password reset for when you forget your password
- Dashboard (login required)
- Landing page
- Subscription/payment
