import os, sys, yadisk
from datetime import datetime

script_dir = os.path.dirname(sys.argv[0])
def read_file(file_path, file_name):
    with open(os.path.join(file_path, file_name), encoding='utf-8') as f:
        token_ya = f.read().strip()
    return token_ya

y = yadisk.YaDisk(token=read_file(script_dir, 'ya_token.txt'))

class YaDisk_upload():

    def run(path):
        date = datetime.strftime(datetime.now(), "%d.%m.%Y.-%H.%M.%S")
        y.mkdir(f'/test/{date}')

        for address, dirs, files in os.walk(path):
            for dir in dirs:
                y.mkdir(f'/test/{date}/{dir}')
                print('The folder {dir} has been created')
            for file in files:
                y.upload(f'{address}/{file}', f'/test/{date}/{file}')