# py module for implementing SPARQLWrapper with UNLV requirements
#
import re
from SPARQLWrapper import SPARQLWrapper, XML, JSON

wd_endpoint = "https://query.wikidata.org/sparql"
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


def get_wd_query(query):
    # retrieves a list matrix of the UNLV base query.
    user_agent = 'PySparqlTest/0.0 (https://linkedin.com/andre_hulet; andrehulet@gmail.com)'
    sparql = SPARQLWrapper(wd_endpoint, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    the_set = sparql.query().convert()
    return the_set


def load_base(json_dict):
    # preps the LOAD_BASE query results for use in Django
    clean_result = []
    for r in json_dict["results"]["bindings"]:
        # base query includes topic (Q code), topic label, category label (typeof)
        topic = r.get("topic", {}).get("value")
        topic_split = re.split(r'\/', topic)
        topic_key = topic_split.pop()
        topic_label = r.get("topicLabel", {}).get("value")
        categLabel = r.get("categoryLabel", {}).get("value")
        clean_result_row = [topic_key, topic_label, categLabel]
        clean_result.append(clean_result_row)

    return clean_result


def load_item_detail(json_dict):
    clean_result = []
    for r in json_dict["results"]["bindings"]:
        # base query includes item (Q code) label, the property, English language prop value
        item = r.get("itemLabel", {}).get("value")
        prop = r.get("property", {}).get("value")
        prop_code = re.split(r'\/', prop).pop()
        val = r.get("oLabel_en", {}).get("value")
        clean_result_row = [item, prop_code, val]
        clean_result.append(clean_result_row)

    return clean_result


def query_item_detail(qvalue):
    # provides query of properties for a given wikidata Q code
    qry_begin = """select ?itemLabel ?property ?oLabel_en 
where {
  VALUES ?item {wd:"""

    qry_end = """} .
  ?item ?property ?oraw .
  ?oraw rdfs:label ?oLabel_en . FILTER (lang(?oLabel_en)='en')
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }  
   }"""
    return qry_begin + qvalue + qry_end
