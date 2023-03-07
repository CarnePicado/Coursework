from vk_project import *
from ya_project import *

if __name__ == '__main__':
    test = VK_photo_save()
    data_1 = test.get_data()
    max_value_1 = test.get_max_size(data_1)
    test.data_dict(data_1, max_value_1)
    test = YaDisk_upload
    test.run('/home/carnepicado/Desktop/NetologyHW/Work_with_json/FinalProject/images')