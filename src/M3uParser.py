from urllib.parse import urlparse


class M3uParser(object):
    def __init__(self, m3u):
        self.lines = m3u.splitlines()

    def parse(self):
        parsed_lines = []
        for num, line in enumerate(self.lines):
            if line == '#EXTM3U':
                parsed_lines.append(line)
            elif line.startswith('#EXTINF:'):
                group = M3uParser.extract_group(self.lines[num + 1])
                if group != 'live' or M3uParser.is_fr(line):
                    new_line = line.replace(',', f' group-title="{group}",', 1).replace('FR - ', '', 1).replace('FR- ',
                                                                                                                '', 1)
                    parsed_lines.append(new_line)
                    parsed_lines.append(self.lines[num + 1])
        return '\n'.join(parsed_lines)

    @staticmethod
    def extract_group(url):
        return urlparse(url).path.split('/')[1]

    @staticmethod
    def is_fr(ext_inf):
        return ext_inf.startswith('#EXTINF:-1,FR') or ext_inf.startswith('#EXTINF:-1,(-FR')
