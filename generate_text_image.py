import requests

UNSPLASH_ACCESS_KEY = '4nAfsYR31NZCgTw1oSr0EzXRVgG9BkhyP5MFSrtwCxk'

def generate_random_city():
    url = "https://random-city-api.vercel.app/api/random-city"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['city']:
            return data['city']
        else:
            return None

def get_cover_image(keyword):
    url = f"https://api.unsplash.com/search/photos"
    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
    params = {"query": keyword, "per_page": 1}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]['urls']['regular']
        else:
            return "No images found for the given keyword."
    else:
        return f"Error: {response.status_code} - {response.text}"


keyword = generate_random_city()
if keyword:
    image_url = get_cover_image(keyword)
    print(f"Cover Image URL for city {keyword}: {image_url}")
else:
    print("Invalid City Name")

