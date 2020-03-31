from bs4 import BeautifulSoup

def scrape_item_tables(page_content: str) -> list:
    soup = BeautifulSoup(page_content, 'html.parser')

    tr_tag_list = soup.find_all('tr', {'class':'tr-i'})

    data = []

    for tr_tag in tr_tag_list:
        ingredient = tr_tag.findChild('span', {'class': 'colors'}).string

        function = tr_tag.findChild('td', {'class': 'small-85 text-vampire align-middle'}).string\
            .strip()\
            .replace(" ", "")\
            .replace("\n", " ")

        safety_list = tr_tag.findChildren('span', {'title': 'Safety'})
        safety = []
        for span in safety_list:
            safety.append(span.string)

        data.append({
            'ingredient': ingredient,
            'function': function,
            'safety': safety
        })

    return data
