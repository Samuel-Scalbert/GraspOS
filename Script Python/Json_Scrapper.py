import json


def scrapper_title_json(file_name):
    with open('data_HAL/' + file_name, 'r', encoding='utf-8') as file:
        # Load the JSON data
        data = json.load(file)

        response = data["response"]
        docs = response["docs"]
        list_conferenceTitle_s = []

        for conf in docs:
            conferencetitle_s = conf["conferenceTitle_s"]
            list_conferenceTitle_s.append(conferencetitle_s)
        return list_conferenceTitle_s
