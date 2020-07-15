import requests


url = 'https://cdn.dlcordapp.com/attachments/486699197131915266/710452259770728448/cute_koishi.png'
user_agent = 'Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)'
headers = {'User-Agent': user_agent}

r = requests.get(url, headers=headers, allow_redirects=False)

with open('C:\\cute_koishi.png', 'wb') as f:
    f.write(r.content)

print('Done!')
