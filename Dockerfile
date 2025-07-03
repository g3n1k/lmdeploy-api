
FROM openmmlab/lmdeploy
ENV CUDA_VERSION_SHORT=cu123

# support for InternVL & qween
RUN python3 -m pip install timm \
    git+https://github.com/huggingface/transformers.git \
    https://github.com/Dao-AILab/flash-attention/releases/download/v2.6.3/flash_attn-2.6.3+${CUDA_VERSION_SHORT}torch2.3cxx11abiFALSE-cp310-cp310-linux_x86_64.whl \
    qwen_vl_utils

RUN apt-get update && \
    apt-get install -y ncdu curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
