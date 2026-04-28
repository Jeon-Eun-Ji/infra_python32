from deep_translator import GoogleTranslator

translator_list = [GoogleTranslator(source="ko", target="en"), "국어 점수를 입력하세요."]
print(translator_list[0].translate(translator_list))


#my_translator = GoogleTranslator(source="ko", target="en")
#result = my_translator.translate("안녕하세요. 저는 전은지입니다.")
#p#rint(result)