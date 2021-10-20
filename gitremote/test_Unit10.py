from Unit10 import *


# Creates one text string, searches for president last name in text string.
# Works properly. Fails with random words inserted in pres_list.
@pytest.mark.parametrize("president", pres_list)
def test_ddg1_for_presidents(president):
    textList = ""
    for i in relatedTopics:
        textList += i["Text"]
    assert president in textList


# This test passed but after using additional random words, test still passed.
# Not a good test to use
# @pytest.mark.parametrize("president", pres_list)
# def test_ddg0_for_presidents(president):
#     for i in relatedTopics:
#        assert any(elem in i["Text"] for elem in president)


# url_ddg = "https://api.duckduckgo.com"
# def test_ddg0():
#    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
#    rsp_data = resp.json()
#    ##print(rsp_data["Heading"])
#    assert "DuckDuckGo" in rsp_data["Heading"]



