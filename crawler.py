import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_forms(url, session):
    try:
        response = session.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.find_all("form")
    except Exception as e:
        print(f"[-] Error crawling {url}: {e}")
        return []

def get_form_details(form):
    """Extracts action, method, and inputs from a form."""
    details = {}
    details["action"] = form.attrs.get("action", "").lower()
    details["method"] = form.attrs.get("method", "get").lower()
    
    inputs = []
    for input_tag in form.find_all(["input", "textarea"]):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["inputs"] = inputs
    return details
