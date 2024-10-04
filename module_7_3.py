class WordsFinder:
    delimeters = (',', '.', '=', '!', '?', ';', ':', ' - ')
    def __init__(self, *files: str):
        self.file_names: tuple = files
    def get_all_words(self):
        all_words = {}
        for f in self.file_names:
            with open(f, encoding='utf-8') as file:
                file_words = []
                for s in file:
                    sl = s.lower()
                    for ch in self.delimeters:
                        sl = sl.replace(ch, '')
                    file_words.extend(sl.split())
                all_words[f] = file_words
        return all_words

    def find(self, word):
        word_first_instance = {}
        for f in self.file_names:
            with open(f, encoding='utf-8') as file:
                all_words = self.get_all_words()
                for fn, w in all_words.items():
                    for i in range(len(w)):
                        if word.lower() == w[i].lower():
                            word_first_instance[fn] = i
                            break
        return word_first_instance

    def count(self, word):
        word_count = {}
        for f in self.file_names:
            with open(f, encoding='utf-8') as file:
                all_words = self.get_all_words()
                count = 0
                for fn, w in all_words.items():
                    for i in range(len(w)):
                        if word.lower() == w[i].lower():
                            count += 1
                if count > 0:
                    word_count[fn] = count
        return word_count

finder2 = WordsFinder('test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего