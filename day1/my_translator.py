from deep_translator import GoogleTranslator

my_translator = GoogleTranslator(source="ko", target="en")

result = my_translator.translate("안녕하세요. 저는 전은지입니다.")
print(result)