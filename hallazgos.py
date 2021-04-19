import stanza
import spacy
from negspacy.negation import Negex

nlp_ = spacy.load("es_core_news_md")



nlp = stanza.Pipeline(lang='es')

review  = """Parénquima mamario denso, heterogéneo y pseudonodular, lo que disminuye la sensibilidad del método.
En la unión de los cuadrantes inferiores, tercio posterior de la mama derecha, se visualiza nódulo isodenso, de bordes aceptablemente definidos, de 6mm., reducido de tamaño entre controles.
No hay lesiones espiculadas, distorsiones ni microcalcificaciones agrupadas de sospecha, solo puntiformes aisladas."""

doc_review = nlp(review)

# doc_review.sentences[0].print_dependencies()

for sent in doc_review.sentences:
    for dep in sent.dependencies:       
        if dep[1] == 'amod' :
            print(dep[0].text,dep[2].text)


for sent in doc_review.sentences:
    for dep in sent.dependencies:       
        if dep[1] == 'root' :
            print(dep[2].text)  


doc_review_ = nlp_(review)
for e in doc_review_.ents:
    print(e)