# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/
import re
from SPARQLWrapper import SPARQLWrapper, XML, JSON

endpoint = "https://query.wikidata.org/sparql"
LOAD_BASE = """select ?topic ?topicLabel ?categoryLabel
where {
  {
   ?topic wdt:P485 wd:Q96156694 .
    ?topic wdt:P31 ?category .
  }  
UNION 
  {
    ?topic wdt:P485 wd:Q73644758 .
    ?topic wdt:P31 ?category .
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }  
}
ORDER BY ?categoryLabel
"""

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
    sparql.setQuery(LOAD_BASE)
    sparql.setReturnFormat(JSON)
    the_set = sparql.query().convert()
    clean_result = {}
    for r in the_set["results"]["bindings"]:
        topic = r.get("topic", {}).get("value")
        topic_split = re.split(r'\/', topic)
        topic_key = topic_split.pop()
        topic_label = r.get("topicLabel", {}).get("value")
        categLabel = r.get("categoryLabel", {}).get("value")

        print(topic_key + " |", topic_label + " |", categLabel)
