import requests

token = "we87fwR4Tf3287w67"
url = "https://gamora.asgard.pp.ua/data/1"

def get_data(url):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.json()

data = get_data(url)
tickets_sold_hour_before_trip = data.get("tickets_sold_hour_before_trip", 17)

print(f"Кількість квитків, куплених за годину до подорожі: {tickets_sold_hour_before_trip}")