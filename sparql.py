# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

from SPARQLWrapper import SPARQLWrapper, JSON

endpoint = "https://query.wikidata.org/sparql"
sample_query = """select distinct ?academicLabel ?deptLabel ?studyAreaLabel ?worksLabel
where {
  VALUES ?employer {wd:Q913861} .
  ?academic wdt:P108 wd:Q913861 ;
    wdt:P106 wd:Q1622272 ;
    wdt:P1416 ?dept ; 
    wdt:P101 ?studyArea ;
  OPTIONAL {?academic wdt:P800 ?works} .
  FILTER (?dept != wd:Q7413726)
  VALUES ?studyArea {wd:Q35069} . 
  service wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  }
order by ?academicLabel
"""


def test_wikidata():

    user_agent = 'PySparqlTest/0.0 (https://linkedin.com/andre_hulet; andrehulet@gmail.com)'
    # adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint, agent=user_agent)
    sparql.setQuery(sample_query)
    sparql.setReturnFormat(JSON)
    the_set = sparql.query().convert()

    for result in the_set["results"]["bindings"]:
        print(result)
