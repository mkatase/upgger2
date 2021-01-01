#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/blogger']

def main():
    tfile = '.conf/token.pickle'
    cfile = '.conf/credentials.json'
    creds = None

    if os.path.exists( tfile ):
        with open( tfile, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                cfile, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open( tfile, 'wb') as token:
            pickle.dump(creds, token)

    service = build('blogger', 'v3', credentials=creds)

    # Call the Blogger API
    users = service.users()

    # Retrieve this user's profile infomation
    thisuser = users.get(userId='self').execute()
    print('This user\'s display name is: %s\n' % thisuser['displayName'])

    blogs = service.blogs()

    # Retrieve the list of Blogs this user has write privileges on
    thisusersblogs = blogs.listByUser(userId='self').execute()
    print(' Blog Id            | Blog Title')
    print('{}+{}'.format('-'*20, '-'*48))
    for blog in thisusersblogs['items']:
        print('{} | {}'.format(blog['id'], blog['name']))

if __name__ == '__main__':
    main()
