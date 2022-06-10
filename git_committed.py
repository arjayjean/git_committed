#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import os
from pathlib import Path
subprocess.run('clear')

print('Is this project initiated? Y / N\n')

commited = False

while commited != True:
    initiated = input().upper() 

    if initiated == 'Y': 
        subprocess.run('clear')
        msg = input('Enter your message: ')
        commit = [
            ['git', 'add', '.'],
            ['git', 'commit', '-m', f'{msg}'],
            ['git', 'push'],
            'clear',
            ['git', 'status']
        ]

        final_git = [subprocess.run(command) for command in commit]
        commited = True


    elif initiated == 'N':
        directory = ''
        for path in os.scandir():
            filePath = Path(path)
            if filePath.suffix == '.py':
                directory = filePath.stem
            elif filePath.suffix == '.html':
                directory = filePath.stem        

        initiation = [
        ['git', 'add', '.'],
        ['git', 'commit', '-m', '"Initial ' 'commit"'],
        ['git', 'remote', 'add', 'origin', f'https://github.com/USERNAME/{directory}.git'],
        ['git', 'branch', '-M', 'main'],
        ['git', 'push', '-u', 'origin', 'main'],
        'clear',
        ['git', 'status']
        ]

        final_git = [subprocess.call(command) for command in initiation]
        commited = True

    elif initiated != 'Y' or 'N':
        subprocess.run('clear')
        print('Incorrect value! Please select Y or N\n')