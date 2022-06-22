import re


class Tokenizer:
    @staticmethod
    def tokenize(sentence):
        loweredSentence = Tokenizer.lower_sentence(sentence)
        wordList = list(filter(None, re.split('[^a-zA-Z0-9ığüşöç]', loweredSentence)))
        return wordList

    @staticmethod
    def lower_sentence(sentence):
        lower_map = {
            ord(u'I'): u'ı',
            ord(u'İ'): u'i',
        }

        loweredSentence = sentence.translate(lower_map).lower()
        return loweredSentence