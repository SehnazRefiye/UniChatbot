import json
from tokenizer import Tokenizer
# from pyswip import Prolog
"""
prolog = Prolog()
prolog.consult("morphological_analyzer.pl")
"""
# bu kısımda json dosyası içindeki keywordsler bize lazım
# ayrıca kullanıcının girdiği soru da lazım
# kullanıcının girdiği soruyu alıp tokonize etmemiz gerekli
# bir sınıf oluşturuyoruz, adı değişebilir
class ChatBot:
    # ilk önce constructor oluşturuyoruz
    def __init__(self):
        # deneme.json dosyasını açtık
        self.data = open("deneme.json", encoding="utf-8")
        # json formatındaki veriyi 
        # pythonın anlayabileceği şekilde bir dict yapısı haline getirdik
        self.data = json.load(self.data)
        self.create_corpus()

    def create_corpus(self):
        # aynı olan keywordsler tekrar eklenmesin diye set() i kullandık
        self.corpus = set()
        
        # json dosyaının içinde olan keywordsler bize lazım
        # kullanıcının girdiği sorunun içinde bu keywordsleri arayacağız
        for pair in self.data:
            for keys in pair["keywords"]:
                for key in keys:
                    # bütün keywordsler artık tek bir listede
                    # aynı olan keywordsler listeye tekrar alınmıyor
                    self.corpus.add(key)

    def chatbot_question(self, quesiton):
        self.answer = "" 
        self.answer_key_length = -1
        
        # kullanıcıdan alınan soru burada tokenize ediliyor
        quesiton_words = Tokenizer.tokenize(quesiton)
        
        
        # sorunun içinde geçen anahtar kelimeler için boş bir array açtık
        quesiton_keywords = []
        for word in quesiton_words:
            for key in self.corpus:
                if key in word:
                    # kullanıcının sorduğu sorunun içinde geçen 
                    # ve oluşturduğumuz keywords havuzuyla eşleşen 
                    # kelimeleri array e ekledik
                    quesiton_keywords.append(key)
                """    
                elif key == self.prolog.analyzer(word):
                    quesiton_keywords.append(key)
                """
        
        # oluşturduğumuz array in içinde eleman olup olmadığını kontrol ettik
        if len(quesiton_keywords) > 0:
            # kullanıcının sorduğu sorunun içinde o soruya ait bütün keywordsler
            # geçmek zorunda değil
            # bu yüzden aşağıdaki koşul(if) kodu yazıldı
            for pair in self.data:
                for keys in pair["keywords"]:
                    if set(quesiton_keywords) >= set(keys):
                        # array in içi boş değil ve kullanıcının sorduğu soru ile
                        # keywords listesinde eşleşme varsa 
                        # eşleşen keywordslerin olduğu cevabı döndür
                        if self.answer_key_length == -1 or len(set(keys)) > self.answer_key_length:
                            self.answer = pair["answer"]
                            self.answer_key_length = len(set(keys))
        # eğer array in içi boşsa bu yazıyı console a bastır
        if self.answer != "":
            return self.answer
        else: 
            return "Maalesef bu soruya cevap veremiyorum!!!"
