# Upgger2 - HTML Uploader Vesion 2 for Blogger
command line based HTML uploader for Google Blogger API v3 written by Python.

## Set up JSON file
Please access [this page](https://console.developers.google.com/apis/credentials) and get credentials.json file.

```
$ mkdir .conf
$ cp credentials.json .conf
```

## Getting Blog ID from Bloglists
```
$ ./script/list.py 
This user's display name is: carlos

 Blog Id            | Blog Title
--------------------+------------------------------------------------
1111222233334444555 | Test A Blog
6666777788889999000 | Test B Blog
$
```
For example, if you select "Test A Blog", you must write blog id of "Test A Blog" in upgger.yaml file.

```
$ cat .conf/upgger.yaml
blog_id: '1111222233334444555'
```
Please check ".conf" directory
```
$ ls -a .conf
. .. credentials.json upgger.yaml
```

## Install python module
```
$ pip install google-api-python-client google-auth-oauthlib PyYAML
```
or
```
$ pip install -r requirements.txt
```

## Usage
At the first time, please "authirization" and "allow" on the browser.  
If successful, generated "token.pickle" file.
```
$ ls -a .conf
. .. credentials.json token.pickle upgger.yaml
```

* Basic type (-i option is required)
```
$ python upgger2.py -i hello.html
```
In the above, title is filename(hello.html), label is none,
published date is none, status is LIVE.

* Add to -t or --title option
```
$ python upgger2.py -i hello.html -t hello
```
In the above, title is "hello", label is none,
published date is none, status is LIVE.
```
$ python upgger2.py -i hello.html -t "Hello World"
$ python upgger2.py -i hello.html -t Hello\ World
```
In the above using double quote or backslash, title is "Hello World",
label is none, published date is none, status is LIVE.

* Add to -l or --label option
```
$ python upgger2.py -i hello.html -l abc,def
```
In the above, title is filename, labels are "abc" and "def",
published date is none, status is LIVE.  
Delimitor is comma charactor.

* Add to -p or --pub option
```
$ python upgger2.py -i hello.html -p 20XX-YY-ZZ
```
In the above, title is filename, label is none,
published date is "20XX-YY-ZZ", status is LIVE(no effect).

* Add to -d or --draft option
```
$ python upgger2.py -i hello.html -d
```
In the above, title is filename, label is none,
published date is none, status is DRAFT.
 
## Limitation
*  ~~no upload image file~~
*  ~~no schedule~~
* no permalink

## Development Environment
* OS: Fedora 32 (5.9.15-100) on x86_64
* Python: 3.8.6
* google-api-python-client: 1.12.8
* google-auth-oauthlib: 0.4.2

## Version
* v0.10 2021/01/01 new creation

## License
This source is released under the MIT License, seee LICENSE.txt
