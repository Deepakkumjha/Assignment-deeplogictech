import http.client  
import json  

def fetch_latest_stories():
    connection = http.client.HTTPSConnection("time.com")  
    connection.request("GET", "/")  
    response = connection.getresponse()  
    html_content = response.read().decode('utf-8')  
    start_index = html_content.find('Latest Stories')  
    stories_html = html_content[start_index:start_index + 3000]  
    stories = []  
    find_index = 0  
    while len(stories) < 6:  
        link_s = stories_html.find('<a href="', find_index)+len("<a href=")+1
        link_e = stories_html.find('"', link_s)  
        link = 'https://time.com' + stories_html[link_s:link_e]  
        title_s = stories_html.find('<h3', link_e)+len("<h3 class=\"latest-stories__item-headline>")+1  
        title_e = stories_html.find('<', title_s)  
        title_with_html = stories_html[title_s:title_e].strip()  
        stories.append({"title": title_with_html, "link": link})
        find_index = title_e  
    return stories  


latest_stories = fetch_latest_stories()
print(json.dumps(latest_stories,indent=1))
