from urllib.parse import urlparse


class M3uParser(object):
    def __init__(self, m3u):
        self.lines = m3u.splitlines()

    def parse(self):
        for num, line in enumerate(self.lines):
            if line.startswith('#EXTINF:'):
                group = M3uParser.extract_group(self.lines[num + 1])
                if M3uParser.is_fr(line):
                    self.lines[num] = line.replace(',', f' group-title="{group} FR",', 1).replace('FR - ', '', 1).replace('FR- ',
                                                                                                                '', 1)
                else:
                    self.lines[num] = line.replace(',', f' group-title="{group}",', 1)
        return '\n'.join(self.lines)

    @staticmethod
    def extract_group(url):
        return urlparse(url).path.split('/')[1]

    @staticmethod
    def is_fr(ext_inf):
        return ext_inf.startswith('#EXTINF:-1,FR') or ext_inf.startswith('#EXTINF:-1,(-FR')
