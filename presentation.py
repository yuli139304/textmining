
# coding: utf-8
wordMap = {
           "president": u"president|presidente",
           "dilma": u"Dilma",
           "temer": u"Temer",
           "oglobo": u"O Globo",
           "folha": u"Folha de SP",
           "bbc": u"BBC Brasil",
           "dw": u"DW Brasil",
           "carta": u"Carta Capital",
           "brasil": u"Brasil",
           "mulher": u"woman|mulher",
           "comissao": u"comission|comissão",
           "dia": u"day|dia",
           "nao": u"no|não",
           "impeach": u"impeachment",
           "processo": u"process|processo",
           "senado": u"Senate|Senado",
           "governo": u"government|governo",
           "trump": u"Trump",
           "desfil": u"parade|desfile",
           "rio": u"Rio",
           "reproducao": u"reproduction|reprodução",
           "amarela": u"yellow|amarela",
           "morr": u"die|morrer",
           "febr": u"fever|febre",
           "preve": u"foresee|prever",
           "chuck": u"Chuck",
           "cronologia": u"cronology|cronologia",
           "votacao": u"vote|votação",
           "mandato": u"mandate|mandato",
           "concluiram": u"concluded|concluíram",
           "mal": u"bad|mal",
           "carn": u"meat|carne",
           "luxo": u"luxury|luxo",
           "palacio": u"palace|palácio",
           "presidenci": u"presidency|presidência",
           "destituida": u"destituted|destituída",
           "escandalo": u"scandal|escândalo",
           "reproducao": u"reproduction|reprodução",
           "fraca": u"weak|fraca",
           "faz": u"to do|fazer",
           "cidadania": u"citizenship|cidadania",
           "mora": u"to live|morar",
           "humano": u"human|humano",
           "aprend": u"to learn|aprender",
           "parda": u"brown|parda",
           "catadora": u"picker|catadora",
           "perderam": u"lost|perderam",
           "camara": u"chamber|camara",
           }

def showWord(w):
  if w in wordMap:
    return wordMap[w].encode('utf-8')
  if isinstance(w, str):
    return w.encode('utf-8')
  return w

