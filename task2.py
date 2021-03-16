# не сходится с тестовыми данными, проверить ещё раз

import wikipediaapi
def getStatForCat(category):
    d = {chr(a): 0 for a in range(ord('А'), ord('А') + 32)}
    wiki_wiki = wikipediaapi.Wikipedia('ru')
    page_py = wiki_wiki.page(category)
    tmpdict = []
    for s in page_py.categorymembers:
      tmp = s.split()[-1]
      if tmp[0] in d and tmp not in tmpdict:
        tmpdict.append(tmp)
        d[tmp[0]] += 1
    return d

print(getStatForCat('Категория:Животные по алфавиту'))