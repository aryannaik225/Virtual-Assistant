import webbrowser
from youtube_search import YoutubeSearch

def play():
    query = "Songs"

    results = YoutubeSearch(query, max_results=1).to_dict()
    for result in results:
        url = f"https://youtube.com{result['url_suffix']}"
        title = result['title']
        print(f"{title}: {url}")
        webbrowser.open(url)