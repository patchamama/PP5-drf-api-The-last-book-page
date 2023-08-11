# **_The last book page - Django REST Framework API_**

# Objective

The reason for this API is to provide all the information required for querying and updating data from the front-end "The last book page". To do this using the (MVC) pattern, this application manages the model and controller that serve the data required by the front-end (the View managed with React). To meet its objectives, exhaustive tests are carried out to validate the correct manipulation of data and limited and secure access to the data, depending on the pre-established permissions in the application, taking care of security.

# User Experience (UX)

### User Stories

In total 19 User Stories have been created and executed in 7 Epics (Milestones). In the commit history you can see how the tasks were executed as the development of the application progressed.

# Agile Methodology

# Entity Relationship Diagram

# Database

# Models

### Comment

| **Database Value** | **Field Type** | **Field Argument**               |
| ------------------ | -------------- | -------------------------------- |
| owner              | ForeignKey     | `User, on_delete=models.CASCADE` |
| book               | ForeignKey     | `Book, on_delete=models.CASCADE` |
| comment            | TextField      |                                  |
| created_on         | DateTimeField  | `auto_now_add=True`              |
| updated_on         | DateTimeField  | `auto_now=True`                  |

### Book

| **Database Value** | **Field Type** | **Field Argument**                                                                      |
| ------------------ | -------------- | --------------------------------------------------------------------------------------- |
| title              | Char           | `max_length=150, unique=False`                                                          |
| auth               | Char           | `max_length=150, unique=False`                                                          |
| pub_date           | DateTime       | `blank=True, null=True`                                                                 |
| publisher          | Char           | `max_length=100, unique=False, blank=True`                                              |
| pages_no           | Integer        | `default=0`                                                                             |
| isbn               | Char           | `max_length=13, unique=False, blank=True`                                               |
| lang_orig          | Char           | `max_length=50, choices=LANGUAGES, blank=True`                                          |
| lang               | Char           | `max_length=50, choices=LANGUAGES, blank=True`                                          |
| translators        | Char           | `max_length=200, unique=False, blank=True`                                              |
| genre              | Text           | `blank=True`                                                                            |
| synopsis           | Text           | `blank=True`                                                                            |
| cover              | Image          | `upload_to='images/', default='../No_image_available.svg_t2xrtz.png'`                   |
| created_by         | ForeignKey     | `User, on_delete=models.SET_NULL, related_name="book_createdby", blank=True, null=True` |
| updated_by         | ForeignKey     | `User, on_delete=models.SET_NULL, related_name="book_updatedby", blank=True, null=True` |
| created_on         | DateTime       | `auto_now_add=True`                                                                     |
| updated_on         | DateTime       | `auto_now=True`                                                                         |

### Bookmark

| **Database Value** | ** Type**  | ** Argument**                                                |
| ------------------ | ---------- | ------------------------------------------------------------ |
| owner              | ForeignKey | `User, on_delete=models.CASCADE`                             |
| book               | ForeignKey | `Book, on_delete=models.CASCADE`                             |
| status             | Char       | `max_length=25, choices=STATUS_TYPE, default='Want to read'` |
| created_on         | DateTime   | `auto_now_add=True`                                          |

### Follower

| **Database Value** | ** Type**  | ** Argument**                                              |
| ------------------ | ---------- | ---------------------------------------------------------- |
| owner              | ForeignKey | `User, related_name='following', on_delete=models.CASCADE` |
| followed           | ForeignKey | `User, related_name='followed', on_delete=models.CASCADE`  |
| created_on         | DateTime   | `auto_now_add=True`                                        |

### Like

| **Database Value** | ** Type**  | ** Argument**                                             |
| ------------------ | ---------- | --------------------------------------------------------- |
| owner              | ForeignKey | `User, on_delete=models.CASCADE`                          |
| comment            | ForeignKey | `Comment, related_name='likes', on_delete=models.CASCADE` |
| created_on         | DateTime   | `auto_now_add=True`                                       |

### Profile

| **Database Value** | ** Type** | ** Argument**                                                  |
| ------------------ | --------- | -------------------------------------------------------------- | ----------- |
| owner              | OneToOne  | `User, on_delete=models.CASCADE`                               |
| name               | Char      | `max_length=200, blank=True`                                   |
| date_of_birth      | Date      | `blank=True, null=True`                                        |
| language           | Char      | `max_length=50, choices=LANGUAGES, blank=True`                 |
| image              | Image     | `upload_to='images/', default='../default_profile_hk81a7.jpg'` |
| created_on         | DateTime  | `auto_now_add=True`                                            |
| updated_on         | DateTime  | `auto_now=True`                                                | ### Comment |

| **Database Value** | ** Type** | ** Argument**                    |
| ------------------ | --------- | -------------------------------- |
| owner              | FK        | `User, on_delete=models.CASCADE` |
| book               | FK        | `Book, on_delete=models.CASCADE` |
| comment            | Text      |                                  |
| created_on         | DateTime  | `auto_now_add=True`              |
| updated_on         | DateTime  | `auto_now=True`                  |

### Book

| **Database Value** | ** Type** | ** Argument**                                                                           |
| ------------------ | --------- | --------------------------------------------------------------------------------------- |
| title              | Char      | `max_length=150, unique=False`                                                          |
| auth               | Char      | `max_length=150, unique=False`                                                          |
| pub_date           | DateTime  | `blank=True, null=True`                                                                 |
| publisher          | Char      | `max_length=100, unique=False, blank=True`                                              |
| pages_no           | Integer   | `default=0`                                                                             |
| isbn               | Char      | `max_length=13, unique=False, blank=True`                                               |
| lang_orig          | Char      | `max_length=50, choices=LANGUAGES, blank=True`                                          |
| lang               | Char      | `max_length=50, choices=LANGUAGES, blank=True`                                          |
| translators        | Char      | `max_length=200, unique=False, blank=True`                                              |
| genre              | Text      | `blank=True`                                                                            |
| synopsis           | Text      | `blank=True`                                                                            |
| cover              | Image     | `upload_to='images/', default='../No_image_available.svg_t2xrtz.png'`                   |
| created_by         | FK        | `User, on_delete=models.SET_NULL, related_name="book_createdby", blank=True, null=True` |
| updated_by         | FK        | `User, on_delete=models.SET_NULL, related_name="book_updatedby", blank=True, null=True` |
| created_on         | DateTime  | `auto_now_add=True`                                                                     |
| updated_on         | DateTime  | `auto_now=True`                                                                         |

### Bookmark

| **Database Value** | ** Type** | ** Argument**                                                |
| ------------------ | --------- | ------------------------------------------------------------ |
| owner              | FK        | `User, on_delete=models.CASCADE`                             |
| book               | FK        | `Book, on_delete=models.CASCADE`                             |
| status             | Char      | `max_length=25, choices=STATUS_TYPE, default='Want to read'` |
| created_on         | DateTime  | `auto_now_add=True`                                          |

### Follower

| **Database Value** | ** Type** | ** Argument**                                              |
| ------------------ | --------- | ---------------------------------------------------------- |
| owner              | FK        | `User, related_name='following', on_delete=models.CASCADE` |
| followed           | FK        | `User, related_name='followed', on_delete=models.CASCADE`  |
| created_on         | DateTime  | `auto_now_add=True`                                        |

### Like

| **Database Value** | ** Type** | ** Argument**                                             |
| ------------------ | --------- | --------------------------------------------------------- |
| owner              | FK        | `User, on_delete=models.CASCADE`                          |
| comment            | FK        | `Comment, related_name='likes', on_delete=models.CASCADE` |
| created_on         | DateTime  | `auto_now_add=True`                                       |

### Profile

| **Database Value** | ** Type** | ** Argument**                                                  |
| ------------------ | --------- | -------------------------------------------------------------- |
| owner              | OneToOne  | `User, on_delete=models.CASCADE`                               |
| name               | Char      | `max_length=200, blank=True`                                   |
| date_of_birth      | Date      | `blank=True, null=True`                                        |
| language           | Char      | `max_length=50, choices=LANGUAGES, blank=True`                 |
| image              | Image     | `upload_to='images/', default='../default_profile_hk81a7.jpg'` |
| created_on         | DateTime  | `auto_now_add=True`                                            |
| updated_on         | DateTime  | `auto_now=True`                                                |

# Testing

### Python

#### PEP8 Validation

## Manual Testing

## Security Fixed

During the updates in git I did not check the updates to be discarded in the .gitignore file, which resulted in the env.py file being published with the cloudinary, postgres (ElephantSQL) and secret-key keys. This determined to regenerate the keys again and update them in env.py and the configuration variables in heroku.

## Bugs Fixed

- In the app comments/serializers.py don't render the image cover of the book with the line:

```
book_cover = serializers.ReadOnlyField(source='book.cover.image.url')
```

after a lot of tests/debugs and the checking of the documentation was resolve with the line:

```
book_cover = serializers.ImageField(source='book.cover', read_only=True)
```

## Bugs Unresolved

# Technologies Used

## Languages

## Libraries and Frameworks

## Other Tools

# Development

## Installing Django and libraries

### Install Django

```
pip3 install 'django<4'
```

_The Long Term Support (LTS 3.2.x) version (in my case 3.2.20) will installed and is the most advisable for production as it is kept up to date with security patches._

### Create Project

```
django-admin startproject drf_api_lastpage .
```

_A new directory called your `'drf_api_lastpage'` and a `manage.py` file will be created within your project folder._

### Install Cloudinary Storage to connect Django with Cloudinary

```
pip install django-cloudinary-storage==0.3.0
```

### Install Pillow (to Image Processing)

```
pip install Pillow==8.2.0
```

### Install apps of the project

```
python3 manage.py startapp profiles
python3 manage.py startapp books
python3 manage.py startapp comments
python3 manage.py startapp likes
python3 manage.py startapp bookmarks
python3 manage.py startapp followers
```

### Add Installed Apps in settings `drf_api_lastpage/settings.py`

```
INSTALLED_APPS = [
    (...)
    **'cloudinary_storage',**
    'django.contrib.staticfiles',
    **'cloudinary',**

    'profiles',
    'books',
    'comments',
    'likes',
    'bookmarks',
    'followers'
]
```

_Note: Cloudinary storage must go before django.contrib.staticfiles, as shown._
_Note: Text in **bold** is newly added code_

### Add the following lines in `drf_api_lastpage/settings.py`

- Import os

```
from pathlib import Path
import os
```

- Add statement to import env.py if it exists - _below import os_

```
if os.path.exists('env.py'):
    import env
```

- Set CLOUDINARY_STORAGE variable equals to the CLOUDINARY_URL variable and place directly below imports

```
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
```

- Define Media Storage URL and place directly below

```
MEDIA_URL = '/media/'
```

- Define Default File Storage to Cloudinary and place directly below

```
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

### Create an `env.py` file within the top level directory with the follow content:

```
import os
os.environ['CLOUDINARY_URL'] = 'cloudinary://**<cloudinary_key>**'
```

_Note: Ensure `env.py` is listed in the .gitignore file so it does not get pushed to GitHub._
_Note: URL value copied from [Cloudinary Account Desktop](https://console.cloudinary.com/console/). Make sure to only paste the correct part of the URL_

###

# Deployment

# Credits

- Django Documentation: https://docs.djangoproject.com/en/4.2/ref/models/fields/
- Images of profiles: https://www.pexels.com/
- To generate secret-keys: https://djecrety.ir/

# Acknowledgments
