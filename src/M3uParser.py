from urllib.parse import urlparse
from .Epg import Epg

class M3uParser(object):
    def __init__(self, m3u):
        self.lines = m3u.splitlines()
        self.epg = Epg()

    def parse(self):
        for num, line in enumerate(self.lines):
            if line.startswith('#EXTINF:'):
                group = M3uParser.extract_group(self.lines[num + 1])
                if self.is_fr(line):
                    if self.has_epg(line):
                        self.lines[num] = self.add_epg(line.replace(',', f' group-title="{group} FR",', 1))
                    else:
                        self.lines[num] = line.replace(',', f' group-title="{group} FR without EPG",', 1)
                else:
                    self.lines[num] = line.replace(',', f' group-title="{group}",', 1)
        return '\n'.join(self.lines)

    @staticmethod
    def extract_group(url):
        return urlparse(url).path.split('/')[1]

    def is_fr(self, line):
        return line.startswith('#EXTINF:-1,FR')

    def has_epg(self, line):
        channel = line.split(',')[1]
        return channel in self.epg.channels()

    def add_epg(self, line):
        ext_inf = line.split(',')
        tvg = self.epg.find(ext_inf[1])
        tvg_id = tvg['channel_id']
        ext_inf[0] += f' tvg-id="{tvg_id}"'
        ext_inf[1] = tvg_id
        return ','.join(ext_inf)
