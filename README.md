# Python-TLS-Client File Uploader
An alternative method to *upload files* for [Python-TLS-Client](https://pypi.org/project/tls-client/) through [**POST**](https://en.wikipedia.org/wiki/POST_(HTTP)) request in **python**
# Introduction
I developed this because I ~~encountered repeated exceptions while attempting to upload files using tls_client~~ want to explore something fresh.
> [!WARNING]
> This program needs to load all data into a variable before sending it to the server, which can consume lots of the computer's memory.

> [!NOTE]
> All of the syntax is based on *Python-TLS-Client*. The only difference is that you will now only be **sending files**.
# Dependencies
Only [Python-TLS-Client](https://pypi.org/project/tls-client/) :)
# Examples
Here is the simplest use
```python
import fileuploader, tls_client

FILE_PATH = "path/to/your/file"
FILE_CONTENT_TYPE = "content/type"
FILE_ORIGINAL_NAME = "file"
UPLOADED_FILE_NAME = "file"

UPLOAD_TARGET = "https://upload.server.com/"

# Create a new File object
file = fileuploader.File(FILE_PATH, content_type=FILE_CONTENT_TYPE, name=FILE_ORIGINAL_NAME)

# Create a new tls_client session
sess = tls_client.Session(client_identifier='chrome112')

# Create the FileUploader object
uploader = fileuploader.FileUploader(sess)

# Add the file
uploader.addFile(UPLOADED_FILE_NAME, file)

# Do just like normal tls_client.Session.post method except now you are not modifying the request's body
res = uploader.upload(UPLOAD_TARGET, headers={'some': 'headers'})

# Print the result
print(res.content)
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
#### extract()
> Get the needed file data to upload

Returns a tuple: `(file_name, file, content_type)`

------
## FileUploader
> A class for performing file uploads via POST request
### Methods
#### \_\_init__()
| Parameter | Value | Explanation |
| -- | -- | -- |
| sess | **tls_client.Session** | Python-TLS-Client session to be used |

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
------
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

> [!CAUTION]
> Some arguments like `files`, `data`, and `json` are blocked due to conflicts but maybe not all. Please keep the request body empty unless you know how to work with it

# License
See [License](./LICENSE)
# The last word
I’m *still learning the ropes*, and my code definitely has room for improvement. I sincerely value any contributions or feedback. If you have any questions, feel free to open an issue. And... sorry for my poor English 😅
