import os

import torch
import torchvision

os.environ['CUDA_VISIBLE_DEVICES'] = '0' # #设置当前使用的GPU设备仅为0号设备  设备名称为'/gpu:0'。可以指定使用的环境，是GPU还是CPU。

print(torchvision.__version__) #获取torchvision版本
print(torch.__version__) # 获取torch版本

torch.cuda.set_device(0) # 设定使用指定GPU：0号GPU
print(torch.cuda.is_available()) # 是否有已经配置好可以使用的GPU (若True则有)
print(torch.cuda.device_count())  # 可用GPU块数
print(torch.cuda.get_device_capability()) #获取所使用的GPU的计算力
print(torch.cuda.get_device_name()) #获取该GPU的名称
print(torch.cuda.get_device_properties(0)) #获取指定GPU的常见属性，必须指定GPU，否则报错


