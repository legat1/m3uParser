import os
from src.M3uParser import M3uParser


class MockData:
    @staticmethod
    def get():
        m3u_file = os.path.join(os.path.dirname(__file__), 'list.m3u')
        with open(m3u_file, 'r') as data:
            return data.read()


def test_parse():
    parser = M3uParser(MockData.get())
    res = parser.parse()
    lines = res.splitlines()
    first_line = lines[1]
    assert lines[0] == '#EXTM3U'
    assert 'group-title="live"' in first_line
    assert 'TF1' in first_line
    assert len(lines) == 11733
