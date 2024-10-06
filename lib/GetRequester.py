import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        search_term='daniel'
        search_term_formatted=search_term.replace('','+')
        fields=["name", "occupation"]
        fields_formatted=",".join(fields)
        limit=1
        
        URL=f"https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json?name={search_term_formatted}&occupation={fields_formatted}&limit={limit}"
        
        response = requests.get(URL)
        return response.content

    def load_json(self):
        search_term="daniel"
        search_term_formatted=search_term.replace("","+")
        fields=['name','occupation']
        fields_formatted=','.join(fields)
        limit=1
        
        URL=f"https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json?name={search_term_formatted}&occupation={fields_formatted}&limit={limit}"
        print (URL)
        response=requests.get(URL)
        
        return response.json()
        