def p(*data):
    # import json
    print(data)


def main(base_url=None):
    try:
        import requests, os, sys
        from bs4 import BeautifulSoup
    except Exception as e:
        print("Some Modules are missing...")
    else:
        if base_url is None:
            base_url = 'https://www.bridgeport.edu/'

        def check_extensions(url, extensions=None):
            if extensions is None:
                extensions = ['.gif', '.svg', '.png', '.jpeg', '.jpg', '.webp']

            for e in extensions:
                if e in url:
                    return {'cond': True, 'e': e}
            return {'cond': False}

        headers = {
            'Accept-Encoding': 'gzip, deflate, such',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                          'Safari/537.36 Edg/115.0.1901.203',
            'Accept': '*/*',
            'Referer': 'https://www.wikipedia.org/',
            'Connection': 'keep-alive',
        }

        r = requests.get(url=base_url, headers=headers)
        folder_name = 'bot-images'

        soup = BeautifulSoup(r.text, 'html.parser')
        img_tags = soup.findAll('img')

        for count, i in enumerate(img_tags):
            new_url = base_url + i['src']
            c = check_extensions(new_url)

            if c['cond']:
                try:
                    os.mkdir(folder_name)
                except Exception as e:
                    curr_path = os.getcwd()
                    new_path = os.path.join(curr_path, folder_name)
                    with open(f"{new_path}/{count}{c['e']}", "wb") as f:
                        r = requests.get(url=new_url)
                        f.write(r.content)


if __name__ == '__main__':
    main()
