#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  v0.10 2021/01/01 new creation (Improved upgger.py)

  uploader for blogger

  Usage:
    $ python upgger2.py -i hoge.html
  When this is the case, title is filename, label is none,
  published date is none, status is LIVE.

    $ python upgger2.py -t moge -i hoge.html
  When this is the case, title is "moge", label is none,
  published date is none,  status is LIVE.

    $ python upgger2.py -t "hoge hoge" -i hoge.html
    or
    $ python upgger2.py -t hoge\ hoge -i hoge.html
  When this is the case, title is "hoge hoge", label is none,
  published date is none, status is LIVE.

    $ python upgger2.py -l aaa -i hoge.html
  When this is the case, title is filename, label is "aaa",
  published date is none, status is LIVE.

    $ python upgger2.py -l aaa,bbb -i hoge.html
  When this is the case, title is filename, labels are "aaa" and "bbb",
  published date is none, status is LIVE.

    $ python upgger2.py -i hoge.html -p 20XX-YY-ZZ
  When this is the case, title is filename, labels is none,
  published date is "20XX-YY-ZZ", status is none.

    $ python upgger2.py -i hoge.html -d
  When this is the case, title is filename, label is none,
  status is DRAFT.

"""

__author__  = 'mkatase (michimoto.katase@gmail.com'
__version__ = '0.10'

from sys import *
from string import *
from argparse import ArgumentParser
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import datetime
import os
import yaml

class Upgger:
    def __init__(self, opts):
        self.ifile = opts.file
        self.label = opts.label
        self.title = opts.title
        self.pdate = opts.pub
        self.draft = opts.draft

    def checkfile(self):
        if os.path.isfile(self.ifile):
            with open(self.ifile) as fp:
                self.content = fp.read()
                if self.title is None:
                    n = self.ifile.rfind('/')
                    self.title = self.ifile[n+1:]
        else:
            print('Input File Not Found...')
            exit()

    def checkdir(self):
        s_dir = os.path.abspath( os.path.dirname( __file__ ) )
        self.c_dir = os.path.join( s_dir, ".conf" )

        if not os.path.exists( self.c_dir ):
            os.mkdir( self.c_dir )

    def checkstorage(self):
        flags = ['--auth_host_name','localhost']
        #flags = None
        scopes = ['https://www.googleapis.com/auth/blogger']
        pfile  = os.path.join( self.c_dir , 'token.pickle' )
        cfile  = os.path.join( self.c_dir , '/credentials.json' )

        creds = None

        if os.path.exists( pfile ):
            with open( pfile, 'rb' ) as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh( Request() )
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    cfile, scopes )
                creds = flow.run_local_server( port=0 )
            with open( pfile, 'wb' ) as token:
                pickle.dump( creds, token )

        return creds

    def createbody(self):
        body = {}

        body['title']   = self.title
        body['content'] = self.content

        if self.pdate:
            d = datetime.datetime.strptime(self.pdate,'%Y-%m-%d')
            e = datetime.datetime(d.year, d.month, d.day)
            body['published'] = e.isoformat()

        if self.label is not None: 
            body['labels'] = self.label.split(',')

        return body

    def getyaml(self):
        b_path = os.path.join( self.c_dir, 'upgger.yaml' )
        with open(b_path) as fp:
            data = yaml.load(fp, Loader=yaml.FullLoader)
        self.b_id = data['blog_id']

    def uploadfile(self, cr):
        service = build('blogger', 'v3', credentials=cr)
        blogs   = service.blogs()
        posts   = service.posts()

        self.getyaml()
        insert = posts.insert(blogId=self.b_id, isDraft=self.draft,
                              body=self.createbody())
        insert.execute()

    def start(self):
        self.checkfile()
        self.checkdir()
        self.uploadfile( self.checkstorage() )

if __name__ == '__main__':

    U = '{} [-t|--title] <Title> [-l|--label] <Labels> '.format(__file__)
    U = U + '[-i|--in] <Input HTML> [-d|--draft]'
    p = ArgumentParser(usage=U)

    p.add_argument("-i", "--in", dest="file",
        help="Input HTML file")
    p.add_argument("-t", "--title", dest="title",
        help="Input Title (default is Input HTML filename")
    p.add_argument("-l", "--label", dest="label", default=None,
        help="Input Labels (comma separated)")
    p.add_argument("-p", "--pub", dest="pub",
        help="Input Published Date String (ex. 2050-01-01)")
    p.add_argument("-d", "--draft", dest="draft", default=None,
        action="store_true", help="Input Status flag")
    p.add_argument('--version', action='version', version=__version__)
 
    args = p.parse_args()

    if len(argv) == 1:
        p.print_help()
        exit()

    if args.file is None:
        print('Input HTML file ([-i|--in] <HTML file>)')
        exit()

    Upgger(args).start()

# end of Upgger script
