import requests


class M3uDownload(object):
    def __init__(self, user_id, user_pwd):
        self.url = f'http://tvservice.pro:80/get.php?username={user_id}&password={user_pwd}&type=m3u&output=ts'

    def get(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            return r.text
        else:
            return None
