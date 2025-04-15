#!/bin/bash
# Setup script for SAMPart3D on Linux
set -e

sudo apt-get update
sudo apt-get install -y libglib2.0-0 curl git python3-pip python3-venv

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip packaging setuptools wheel ninja

pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu121

pip install spconv-cu121 \
    Pillow opencv-python transformers einops scikit-learn tensorboard tensorboardx \
    yapf addict scipy timm open3d trimesh torch-scatter

curl -o /usr/local/bin/pget -L "https://github.com/replicate/pget/releases/latest/download/pget_$(uname -s)_$(uname -m)"
sudo chmod +x /usr/local/bin/pget

if [ ! -d "SAMPart3D" ]; then
    git clone https://github.com/V-Sekai-fire/SAMPart3D.git SAMPart3D
fi

cd SAMPart3D/libs/pointops
TORCH_CUDA_ARCH_LIST="7.5;8.0;8.6" python setup.py install
cd ../../../

TCNN_CUDA_ARCHITECTURES=86 pip install ninja git+https://github.com/NVlabs/tiny-cuda-nn/#subdirectory=bindings/torch

pip install --extra-index-url=https://pypi.nvidia.com cudf-cu11==24.6.* cuml-cu11==24.6.*

echo "Setup complete. Activate your virtual environment with: source venv/bin/activate"
