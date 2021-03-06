from urllib.parse import urlparse

from .Epg import Epg


class M3uParser(object):
    _LIVE = 'live'

    def __init__(self, m3u):
        self.lines = m3u.splitlines()
        self.epg = Epg()

    def parse(self):
        for num, line in enumerate(self.lines):
            if line.startswith('#EXTINF:'):
                group = M3uParser.extract_group(self.lines[num + 1])
                if group == M3uParser._LIVE and self.has_epg(line):
                    self.lines[num] = self.add_epg(line.replace(',', f' group-title="{M3uParser._LIVE} FR",', 1))
                elif group == M3uParser._LIVE:
                    self.lines[num] = line.replace(',', f' group-title="{M3uParser._LIVE}",', 1)
                elif self.is_fr(line):
                    self.lines[num] = line.replace(',', f' group-title="{group} FR",', 1)
                else:
                    self.lines[num] = line.replace(',', f' group-title="{group}",', 1)   
        return '\n'.join(self.lines)

    @staticmethod
    def extract_group(url):
        parts = urlparse(url).path.split('/')
        if len(parts) == 5:
            return parts[1]
        elif len(parts) == 4:
            return M3uParser._LIVE
        else:
            return 'empty'

    def is_fr(self, line):
        return line.startswith('#EXTINF:-1,FR') or line.startswith('#EXTINF:-1,|FR|')

    def has_epg(self, line):
        channel = line.split(',')[1]
        return channel in self.epg.channels()

    def add_epg(self, line):
        ext_inf = line.split(',')
        tvg = self.epg.find(ext_inf[1])
        tvg_id = tvg['channel_id']
        tvg_logo = tvg['channel_logo']
        tvg_name = tvg['channel_name']
        ext_inf[0] += f' tvg-id="{tvg_id}" tvg-logo="{tvg_logo}"'
        ext_inf[1] = tvg_name
        return ','.join(ext_inf)
