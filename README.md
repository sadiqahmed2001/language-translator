# language-translator
It takes input from the user, translates it into the desired language using Google Translate, and prints out the translated text

First, we write the function translate_text, which accepts two parameters: user_input (the text to be translated) and dest_lang (the destination language code). Within the function, we build a Translator object from Googletrans to translate the input text to the desired destination language. Finally, we will return the translated content.

We prompt the user to enter the text they want to translate using input ("Enter the text you want to translate: "). This input is saved in the variable user_input.
We publish the original content by calling print("Original text:", user_input).

We construct a dictionary named supported_languages, where the keys are the lowercase names of languages and the values are the language codes that Google Translate supports.


We prompt the user to enter the language they want to translate the content using input ("Enter the language into which you want to translate:"). To make the comparison case insensitive, we change the input to lowercase with the. lower() function.
We use the in keyword to determine whether the entered language is in the supported_languages dictionary. If that's the case, we run the translate_text method with the user input and the dictionary's language codes. Finally, we publish the translated content.

Suppose the input language is not in the supported_languages dictionary. In that case, we display a message alerting the user that the language is not supported and offer other languages by iterating over the supported_languages dictionary's keys and writing them in uppercase.
Overall, the code allows the user to enter text and a destination language, which is subsequently translated to the requested language using the Google Translate API and printed. If the entered language is not supported, the system notifies the user and provides other languages.
