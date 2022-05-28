LoginRequiredMixin:

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication

## In admin console
1. Create a group with only a name
2. Create a regular user 
3. Add the user to your group
4. Add to urls.py in project folder

```Python
#urls.py

from django.urls import include

#To paths
path('accounts/', include('django.contrib.auth.urls')),
```

5. Navigate to: http://127.0.0.1:8000/accounts/login/
6. Grab the html template name
7. mkdir /project/templates/registration/
8. Open settings.py

```Python
#settings.py

import os

#int TEMPLATES:
       'DIRS': [os.path.join(BASE_DIR, 'templates')],

```

9. Create /project/templates/registration/login.html
10. After a basic test, use the provided template

```Python
#login.html

{% extends "booksofmine/base.html" %}

{% block content %}

  {% if form.errors %}
    <p>Your username and password didn't match. Please try again.</p>
  {% endif %}

  {% if next %}
    {% if user.is_authenticated %}
      <p>Your account doesn't have access to this page. To proceed,
      please login with an account that has access.</p>
    {% else %}
      <p>Please login to see this page.</p>
    {% endif %}
  {% endif %}

  <form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    <table>
      <tr>
        <td>{{ form.username.label_tag }}</td>
        <td>{{ form.username }}</td>
      </tr>
      <tr>
        <td>{{ form.password.label_tag }}</td>
        <td>{{ form.password }}</td>
      </tr>
    </table>
    <input type="submit" value="login" />
    <input type="hidden" name="next" value="{{ next }}" />
  </form>

  {# Assumes you setup the password_reset view in your URLconf #}
  <p><a href="{% url 'password_reset' %}">Lost password?</a></p>

{% endblock %}
```

11. setting.py (set login redirect)

```Python
#settings.py

LOGIN_REDIRECT_URL = '/books'
```

12. Create /project/templates/registration/logged_out.html
13. Copy & paste

```Python
#logged_out.html

{% extends "booksofmine/base.html" %}

{% block content %}
  <p>Logged out!</p>
  <a href="{% url 'login'%}">Click here to login again.</a>
{% endblock %}
```

14. Add pwd reset form /project/templates/registration/password_reset_form.html

```Python
#password_reset_form.html

{% extends "booksofmine/base.html" %}

{% block content %}
  <form action="" method="post">
  {% csrf_token %}
  {% if form.email.errors %}
    {{ form.email.errors }}
  {% endif %}
      <p>{{ form.email }}</p>
    <input type="submit" class="btn btn-default btn-lg" value="Reset password">
  </form>
{% endblock %}
```

15. Create pwd reset done html /project/templates/registration/password_reset_done.html

```Python
#password_reset_done.html

{% extends "booksofmine/base.html" %}

{% block content %}
  <p>We've emailed you instructions for setting your password. If they haven't arrived in a few minutes, check your spam folder.</p>
{% endblock %}
```

16. Create pwd reset email /project/templates/registration/password_reset_email.html

```Python
#password_reset_email.html

Someone asked for password reset for email {{ email }}. Follow the link below:
{{ protocol}}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}
```

17. PWD reset confirm /project/templates/registration/password_reset_confirm.html

```Python
#password_reset_confirm.html

{% extends "booksofmine/base.html" %}

{% block content %}
    {% if validlink %}
        <p>Please enter (and confirm) your new password.</p>
        <form action="" method="post">
        {% csrf_token %}
            <table>
                <tr>
                    <td>{{ form.new_password1.errors }}
                        <label for="id_new_password1">New password:</label></td>
                    <td>{{ form.new_password1 }}</td>
                </tr>
                <tr>
                    <td>{{ form.new_password2.errors }}
                        <label for="id_new_password2">Confirm password:</label></td>
                    <td>{{ form.new_password2 }}</td>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="Change my password" /></td>
                </tr>
            </table>
        </form>
    {% else %}
        <h1>Password reset failed</h1>
        <p>The password reset link was invalid, possibly because it has already been used. Please request a new password reset.</p>
    {% endif %}
{% endblock %}
```

18. pwd reset complete /project/templates/registration/password_reset_complete.html

```Python
#password_reset_complete.html

{% extends "booksofmine/base.html" %}

{% block content %}
  <h1>The password has been changed!</h1>
  <p><a href="{% url 'login' %}">log in again?</a></p>
{% endblock %}
```

19. Restrict views CUD in views.py

```Python
#views.py

class MyView(LoginRequiredMixin, View):
	login_url='/login'
	redirect_field_name = 'redirect_to'
```

