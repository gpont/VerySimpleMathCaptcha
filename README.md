# Very Simple Math Captcha

| Authors | Version |
| :---: | :---: |
| Evgeny Guzhikhin <gpont97@gmail.com> | 0.1 |

Very Simple Math Captcha is the easiest way to add mathematical captcha verification to your forms.
It asks you a simple math question (eg `1 + 2 =`) and validates the form if your response is correct and you can be certain that the users are humans. 

## Using with other apps

Add the following in your `views.py`:

```python
from verysimplemathcaptcha import VerySimpleMathCaptcha
        
def some_page(request):
	CaptchaObject = VerySimpleMathCaptcha()
	if form.is_valid() and CaptchaObject.isValid(request.POST['captcha_id'], request.POST['captcha_answer']):
		pass
```

Now the contact form will block robots who cant do math.

## Settings

Set the behavior of the math captcha interaction in your ``settings.py``

```
VERYSIMPLEMATHCAPTCHA_USING_PIL = True`
```

String containing mathematical operators to use. Default is only add (`+`) and subtract (`-`).
Available operators are: add (`+`), subtract (`-`), multiply (`*`) and divide (`/`)

```
MATH_CAPTCHA_QUESTION = 'Are you human?'
```

Question that appears on forms as a label for math questions. By default it is `'Are you human?'`

## ToDo
- [ ] PIL
- [ ] PIL tests
- [ ] Django forms
- [ ] Publishing
