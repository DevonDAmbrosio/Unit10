from Unit10 import *

#url_ddg = "https://api.duckduckgo.com"
#def test_ddg0():
#    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
#    rsp_data = resp.json()
#    ##print(rsp_data["Heading"])
#    assert "DuckDuckGo" in rsp_data["Heading"]


@pytest.mark.parametrize("president", pres_list)
def test_ddg0_for_presidents(president):
    for i in relatedTopics:
        assert any(elem in i["Text"] for elem in president)
