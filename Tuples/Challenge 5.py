dictionaire = { "Amine": 15.5, "Yassine": 19.0, "Reda": 14.2}

dictionaire_trie = dict(sorted(dictionaire.items(), key=lambda item:item[1]))
print(dictionaire_trie)