import requests, os, sys


VK_USER_ID = 151227453
script_dir = os.path.dirname(sys.argv[0])
def read_file(file_path, file_name):
    with open(os.path.join(file_path, file_name), encoding='utf-8') as f:
        token_vk = f.read().strip()
    return token_vk
  
class VK_photo_save:
    
    def __init__(self):
        self.params = {
            'access_token': read_file(script_dir, 'vk_token.txt'),
            'owner_id': VK_USER_ID,
            'album_id': 'profile',
            'rev': 0,
            'extended': 1,
            'photo_sizes': 1,
            'v': '5.131'
        }

        
    def get_data(self):
        req = requests.get('https://api.vk.com/method/photos.get', self.params).json()
        res = req['response']['items']
        return res
        

    def get_max_size(self, data):
        max_value = 0
        for i in range(0, len(data)):
            if max_value < (data[i]['sizes'][i]['width'] + data[i-1]['sizes'][i]['height']):
                max_value = data[i]['sizes'][i]['width'] + data[i]['sizes'][i]['height']
        return max_value
        
    def data_dict(self, data, max_value):
        for i in range(0, len(data)):
            photo_size = data[i]['sizes'][i]['width'] + data[i]['sizes'][i]['height']
            if photo_size == max_value:
                res = requests.get(data[i]['sizes'][i]['url'])
                print(res)
                likes = data[i]['likes']['count']
                comments = data[i]['comments']['count']
                try:
                    with open(f'images/{str(likes)}', 'xb') as f:
                        f.write(res.content)
                        print('Success')
                except FileExistsError:
                    with open(f'images/{str(comments)}', 'xb') as f:
                        f.write(res.content)
                        print('Success')