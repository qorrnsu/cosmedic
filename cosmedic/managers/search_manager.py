import re
from bs4 import BeautifulSoup

def scrape_search_results(page_content: str) -> list:
    soup = BeautifulSoup(page_content, 'html.parser')

    a_tag_list = soup.find_all('a', href=re.compile('/eng/cosmetic_'))
    del a_tag_list[0::2]

    results = arrange_data(a_tag_list)

    return results

def arrange_data(a_tag_list: list) -> list:
    results = []

    for blob in a_tag_list:
        url = blob['href']
        name = blob.string

        if name and url:
            results.append({
                'name': name.strip(),
                'url': url.strip('/eng/')
            })

    return results