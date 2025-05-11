from bs4 import BeautifulSoup
import requests

def scrape_doctors(specialist):
    url = f"https://pesmed.pl/lekarz-{specialist}-bydgoszcz/"
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    doctors = []

    doctors_card_web = soup.select(".vc_row.wpb_row.vc_inner.vc_row-fluid .vc_col-sm-4")
    for card in doctors_card_web :
        name_property = card.select_one(".wpb_text_column.wpb_content_element h5")
        link_property = card.select_one(".wpb_text_column.wpb_content_element p a")
        img_property = card.select_one(".wpb_wrapper.vc_figure img")
        if name_property is not None:
            name = name_property.text
        else:
            continue

        if link_property is not None:
            link = link_property["href"]

        if img_property is not None:
            img =  img_property["src"]

        doctors.append({"name": name,"link":link, "photo_url": img})

    return doctors

