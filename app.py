import falcon
from wsgiref import simple_server
from src.M3uDownload import M3uDownload
from src.M3uParser import M3uParser


class M3uResource(object):
    def on_get(self, req, resp, user_id, user_pwd):
        m3u = M3uDownload(user_id, user_pwd).get()
        if m3u is None:
            raise falcon.HTTPNotFound(description='m3u file not reachable')
        resp.downloadable_as = f'tv_channels_{user_id}.m3u'
        resp.content_type = falcon.MEDIA_TEXT
        resp.body = M3uParser(m3u).parse()


app = falcon.API()
app.add_route('/m3u/{user_id}/{user_pwd}', M3uResource())

if __name__ == '__main__':  # pragma: no cover
    httpd = simple_server.make_server('127.0.0.1', 1785, app)
    httpd.serve_forever()
