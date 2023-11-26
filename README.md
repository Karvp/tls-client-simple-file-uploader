# tls_client File Uploader
An alternative method to *upload files* for tls_client through [**POST**](https://en.wikipedia.org/wiki/POST_(HTTP)) request in [**python**](https://www.python.org/)
# Introduction
I developed this because I ~~encountered repeated exceptions while attempting to upload files using tls_client~~ want to explore something fresh.
> I am a newbie.
# Dependencies
Only [tls_client](https://pypi.org/project/tls-client/) :)
# Examples
```python
import fileuploader, tls_client

UPLOAD_FILE_PATH = "path/to/your/file"
UPLOAD_FILE_CONTENT_TYPE = "content/type"
UPLOAD_FILE_ORIGINAL_NAME = "file"
UPLOADED_FILE_NAME = "file"

UPLOAD_TARGET = "https://upload.server.com/"

# Create a new tls_client session
sess = tls_client.Session(client_identifier='chrome112')

# Create the FileUploader object
uploader = fileuploader.FileUploader(sess)

# Add a file
uploader.addFile(UPLOADED_FILE_NAME, fileuploader.File(UPLOAD_FILE_PATH, content_type=UPLOAD_FILE_CONTENT_TYPE, name=UPLOAD_FILE_NAME))

# Do just like normal tls_client.post method
res = uploader.upload(UPLOAD_TARGET, headers={'some': 'headers'})

# Print the result
dump(res.json())
```
# Documentation
## File
> A class for easier use of files when uploading
### Methods
#### \_\_init__()
| Parameter | Value | Default | Explanation |
| -- | -- | -- | -- |
| file | **[BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO)** or **str** | *(non-optional)* | A BytesIO object or the path to the file |
| content_type | **str** | None | The [media type](https://en.wikipedia.org/wiki/Media_type) of the file |
| name | **str** | None | The file's original name when uploading |

**Example**
+ With file's path
```python
fileuploader.File("C:/path/to/original_image.jpg", content_type='image/jpg')
```
+ With BytesIO
```python
buff = BytesIO(bytes(open("C:/path/to/original_image.jpg", 'rb'))
fileuploader.File(buff, content_type='image/jpg', name='original_image.jpg')
```
------
#### extract
> Get the needed file data to upload

Returns a tuple: `(file_name, file, content_type)`

------
## FileUploader
> A class for performing file uploads via POST request
### Methods
#### \_\_init__()
| Parameter | Value | Explanation |
| -- | -- | -- |
| sess | **tls_client.Session** | tls_client session to be used |

**Example**
```python
session = tls_client.Session(client_identifier='chrome112')
uploader = fileuploader.FileUploader(session)
```
------
#### addFile()
> Adds a file to upload

| Parameter | Value |
| -- | -- |
| name | **str** |
| file | **fileuploader.File** |

**Example**
```python
file = fileuploader.File("C:/path/to/original_image.jpg", content_type='image/jpg')
uploader.addFile("file_to_upload", file)
```
#### upload()
> Uploads file to url

| Parameter | Value | Explanation |
| -- | -- | -- |
| url | **str** | The destination URL |
| *Others* |  | The same as using `tls_client.Session.post` |

**Example**
```python
uploader.upload("https://target.server.com/target/path")
```
# The last word
I’m *still learning the ropes*, and my code definitely has room for improvement. I sincerely value any contributions or feedback. If you have any questions, feel free to open an issue.
