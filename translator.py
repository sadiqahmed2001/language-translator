from googletrans import Translator

user_input=input("enter the your text:- ")

print("original text:-",user_input)

lang_convert=input("enter the language which you want to convert:- ")
print(f"you are selected {lang_convert} language to convert your  language..thank you..!!!!")


if lang_convert.lower()=="arabic":
    translator=Translator()
    translation=translator.translate(user_input,dest="ar")
    print(f"Translated text:- {translation.text} --->", translation)
elif lang_convert.lower()=="german":
    translator=Translator()
    translation=translator.translate(user_input,dest="de")
    print(f"Translated text:-  {translation.text} ---> ", translation)
elif lang_convert.lower()=="french":
    translator=Translator()
    translation=translator.translate(user_input,dest="fr")
    print(f"Translated text:-  {translation.text} ---> ", translation)
elif lang_convert.lower()=="chinese":
    translator=Translator()
    translation=translator.translate(user_input, dest="zh-CN")
    print(f"Translated text:-  {translation.text} ---> ", translation)
elif lang_convert.lower()=="czech":
    translator=Translator()
    translation=translator.translate(user_input,dest="cs")
    print(f"Translated text:-  {translation.text} ---> ", translation)
elif lang_convert.lower()=="hindi":
    translator=Translator()
    translation=translator.translate(user_input,dest="hi")
    print(f"Translated text:-  {translation.text} ---> ", translation)
elif lang_convert.lower()=="japanese":
    translator=Translator()
    translation=translator.translate(user_input,dest="ja")
    print(f"Translated text:-  {translation.text} ---> ", translation)
elif lang_convert.lower()=="korean":
    translator=Translator()
    translation=translator.translate(user_input,dest="ko")
    print(f"Translated text:-  {translation.text} ---> ", translation)
elif lang_convert.lower()=="luxembourgish":
    translator=Translator()
    translation=translator.translate(user_input,dest="lb")
    print(f"Translated text:-  {translation.text} ---> ", translation)
elif lang_convert.lower()=="macedonian":
    translator=Translator()
    translation=translator.translate(user_input,dest="mk")
    print(f"Translated text:-  {translation.text} ---> ", translation)
elif lang_convert.lower()=="marathi":
    translator=Translator()
    translation=translator.translate(user_input,dest="mr")
    print(f"Translated text:-  {translation.text} ---> ", translation)
elif lang_convert.lower()=="telugu":
    translator=Translator()
    translation=translator.translate(user_input,dest="te")
    print(f"Translated text:-  {translation.text} ---> ", translation)
elif lang_convert.lower()=="kannada":
    translator=Translator()
    translation=translator.translate(user_input,dest="kn")
    print(f"Translated text:- {translation.text} ---> ", translation)
elif lang_convert.lower()=="bengali":
    translator=Translator()
    translation=translator.translate(user_input,dest="bn")
    print(f"Translated text:- {translation.text} ---> ", translation)
elif lang_convert.lower()=="bhojpuri":
    translator=Translator()
    translation=translator.translate(user_input,dest="bho")
    print(f"Translated text:- {translation.text} ---> ", translation)
elif lang_convert.lower()=="russian":
    translator=Translator()
    translation=translator.translate(user_input,dest="ru")
    print(f"Translated text:- {translation.text} ---> ", translation)
elif lang_convert.lower()=="tamil":
    translator=Translator()
    translation=translator.translate(user_input,dest="ta")
    print(f"Translated text:- {translation.text} ---> ", translation)
elif lang_convert.lower()=="turkish":
    translator=Translator()
    translation=translator.translate(user_input,dest="tr")
    print(f"Translated text:- {translation.text} ---> ", translation)
elif lang_convert.lower()=="urdu":
    translator=Translator()
    translation=translator.translate(user_input,dest="ur")
    print(f"Translated text:- {translation.text} ---> ", translation)  
else:
    print("please write correct language")


