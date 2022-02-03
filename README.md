# Python Minimalistic Google Translate API
Just a very simple python file to add to your project (requires Selenium) to use Google Translate.

# Usage:
```py
t = Translator()
print(t.translate('Hello World', Translator.AUTO, Translator.FRENCH)) # Bonjour le monde
print(t.detect_language('מה המצב?')) # Hebrew
