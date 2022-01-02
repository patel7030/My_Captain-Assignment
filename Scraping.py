Project 2: web scraper using Beautitutsoups and requests
import requests
from bs4 import BeautifulSoup
import pandas

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
page_nus_MAX = 3   
scraped_info_list = 11

for page_num in range (1,page_num_MAX):
    req requests.get(oyo_url str(page_num)) 
    content req.content

   soup BeautifulSoup(content, "html.parser")

   all hotels = soup.find_all("div". ("class": "hotelCardListing")) 


  for hotel in all hotels:
      hotel dict= () 
      hotel_dict ["name"]= hotel.find("h3", ("class": "listinghotelDescription_hoteName")).text 
      hotel dict["address"]= hotel.find("span", ("itemprop": "streetAddress"}).text 
      hotel_dict I"price"]= hotel.find("span", ("class": "listingPrice_finalPrice")).text
      #try .... except
      try:
          hotel dict["rating") hotel.find("span", ("class": "hotelRating_ratingSummary")).text
      except AttributrError
          pass

      parent_amenities_element = hotel.find("div", {"class": "amenityWrapper})

      amenities list = []
      for amenity in parent_amenities element.find_all("div", ("class": "amenityWrapper___amenity")):
          amenities_list.append(amenity.find("span", {"class": "d-body-sm")).text.strip())

      hotel dict["amenities"]= ', .join(amenities_list[:-1])

      scraped_info_list.append (hotel_dict)

      #printihotel_name, hotel address, hotel_price, hotel_rating, amenities list)
dataFrame pandas.DataFrame (scraped_info_list)
dataFrame.to_csv"Oyo.csv")

