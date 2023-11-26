import tls_client, random, string
from io import BytesIO
from os.path import basename

__all__ = ['File', 'FileUploader']

def randSeq(length: int, chars: str, encode: str = 'ascii'):
    return bytes().join(random.choice(chars).encode(encode) for _ in range(length))

class File:
    def __init__(self, file: str|BytesIO, *, content_type: str = None, name: str = None):
        self.name = name
        self.content_type = content_type
        if type(file) == str:
            self.file = open(file, 'rb')
            if name == None or len(name) == 0:
                self.name = basename(self.file.name)
        elif isinstance(file, BytesIO):
            self.file = file
            self.name = name
        else:
            raise TypeError("'file' object must be string or BytesIO")
    def extract(self):
        return self.name, self.file, self.content_type

class FileUploader:
    def __init__(self, sess: tls_client.Session):
        self.sess = sess
        
        self.__new_boundary()
        self.body = b''
    def __new_boundary(self):
        self.boundary = b"----WebKitFormBoundary" + randSeq(16, string.ascii_lowercase + string.ascii_uppercase + string.digits)
    def __generate_file_header(self, name: str, filename: str = None, content_type: str = None):
        header = b'Content-Disposition: form-data; name="' + name.encode() + b'"; '
        if filename != None:
            header += b'filename="' + filename.encode() + b'"; '
        if content_type != None:
            header += b'\r\nContent-Type: ' + content_type.encode()
        return header
    def addFile(self, name: str, file: File):
        filename, fp, mime = file.extract()

        self.body = b'--' + self.boundary + b'\r\n'
        self.body += self.__generate_file_header(name, filename, mime)
        self.body += b'\r\n\r\n'
        self.body += fp.read()
        self.body += b'\r\n--' + self.boundary + b'--\r\n'
    def upload(self, url: str, *, files = None, data = None, json = None, **kwargs):
        self.sess.headers['Content-Type'] = 'multipart/form-data; boundary=' + self.boundary.decode()
        return self.sess.post(url, data=self.body, **kwargs)
