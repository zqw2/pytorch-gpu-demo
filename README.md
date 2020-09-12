直接运行code中的train.py，eval暂时无法运行

需要的python版本：3.7
运行需要的扩展包：

本项目主要是为了提供一个快速验证pytorch/cuda/安装完成的demo

=================
GPU版本
=================
pip install -r requirements.txt

=================
CPU版本
=================
pip install -r requirements.txt
pip install torch==1.2.0+cpu torchvision==0.4.0+cpu --default-timeout=1000000 -f https://download.pytorch.org/whl/torch_stable.html

=================
运行
=================
运行python index.py
运行python test-gpu.py