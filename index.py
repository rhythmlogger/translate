from googletrans import Translator  # pip install googletrans==3.1.0a0
translator = Translator(service_urls=['translate.googleapis.com'])
result = translator.translate('어서오세요', dest='en')
print(result)
print(result.text)
