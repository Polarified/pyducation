from zipfile import ZipFile
import os

# Unzip the channel.zip file, extract all the files into a directory.
nothing = '90052'
with ZipFile('channel.zip', 'r') as zip_ref:
    # zip_ref.extractall('./zipdir')
    for i in range(100000):
        with open(f'./zipdir/{nothing}.txt', 'r') as f:
            content = f.read().split()
            print(zip_ref.getinfo(f'{nothing}.txt').comment.decode('utf-8'), end='')
            nothing = content[-1]