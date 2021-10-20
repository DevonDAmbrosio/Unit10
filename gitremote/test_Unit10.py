from Unit10 import *

url_ddg = "https://api.duckduckgo.com"
def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    ##print(rsp_data["Heading"])
    assert "DuckDuckGo" in rsp_data["Heading"]