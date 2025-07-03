```bash
lmdeploy serve api_server --help
usage: lmdeploy serve api_server [-h] [--server-name SERVER_NAME] [--server-port SERVER_PORT] [--allow-origins ALLOW_ORIGINS [ALLOW_ORIGINS ...]] [--allow-credentials]
                                 [--allow-methods ALLOW_METHODS [ALLOW_METHODS ...]] [--allow-headers ALLOW_HEADERS [ALLOW_HEADERS ...]] [--proxy-url PROXY_URL]
                                 [--max-concurrent-requests MAX_CONCURRENT_REQUESTS] [--backend {pytorch,turbomind}]
                                 [--log-level {CRITICAL,FATAL,ERROR,WARN,WARNING,INFO,DEBUG,NOTSET}] [--api-keys [API_KEYS ...]] [--ssl] [--model-name MODEL_NAME]
                                 [--max-log-len MAX_LOG_LEN] [--disable-fastapi-docs] [--allow-terminate-by-client] [--chat-template CHAT_TEMPLATE]
                                 [--tool-call-parser TOOL_CALL_PARSER] [--reasoning-parser REASONING_PARSER] [--revision REVISION] [--download-dir DOWNLOAD_DIR]
                                 [--adapters [ADAPTERS ...]] [--device {cuda,ascend,maca,camb}] [--eager-mode] [--dtype {auto,float16,bfloat16}] [--tp TP]
                                 [--session-len SESSION_LEN] [--max-batch-size MAX_BATCH_SIZE] [--cache-max-entry-count CACHE_MAX_ENTRY_COUNT]
                                 [--cache-block-seq-len CACHE_BLOCK_SEQ_LEN] [--enable-prefix-caching] [--max-prefill-token-num MAX_PREFILL_TOKEN_NUM] [--quant-policy {0,4,8}]
                                 [--model-format {hf,awq,gptq,fp8}] [--dp DP] [--ep EP] [--enable-microbatch] [--enable-eplb] [--role {Hybrid,Prefill,Decode}]
                                 [--migration-backend {DLSlime,Mooncake}] [--node-rank NODE_RANK] [--nnodes NNODES] [--rope-scaling-factor ROPE_SCALING_FACTOR]
                                 [--num-tokens-per-iter NUM_TOKENS_PER_ITER] [--max-prefill-iters MAX_PREFILL_ITERS] [--communicator {nccl,native}]
                                 [--vision-max-batch-size VISION_MAX_BATCH_SIZE]
                                 model_path

Serve LLMs with restful api using fastapi.

positional arguments:
  model_path            The path of a model. it could be one of the following options: - i) a local directory path of a turbomind model which is converted by `lmdeploy convert`
                        command or download from ii) and iii). - ii) the model_id of a lmdeploy-quantized model hosted inside a model repo on huggingface.co, such as
                        "internlm/internlm-chat-20b-4bit", "lmdeploy/llama2-chat-70b-4bit", etc. - iii) the model_id of a model hosted inside a model repo on huggingface.co, such
                        as "internlm/internlm-chat-7b", "qwen/qwen-7b-chat ", "baichuan-inc/baichuan2-7b-chat" and so on. Type: str

options:
  -h, --help            show this help message and exit
  --server-name SERVER_NAME
                        Host ip for serving. Default: 0.0.0.0. Type: str
  --server-port SERVER_PORT
                        Server port. Default: 23333. Type: int
  --allow-origins ALLOW_ORIGINS [ALLOW_ORIGINS ...]
                        A list of allowed origins for cors. Default: ['*']. Type: str
  --allow-credentials   Whether to allow credentials for cors. Default: False
  --allow-methods ALLOW_METHODS [ALLOW_METHODS ...]
                        A list of allowed http methods for cors. Default: ['*']. Type: str
  --allow-headers ALLOW_HEADERS [ALLOW_HEADERS ...]
                        A list of allowed http headers for cors. Default: ['*']. Type: str
  --proxy-url PROXY_URL
                        The proxy url for api server. Default: None. Type: str
  --max-concurrent-requests MAX_CONCURRENT_REQUESTS
                        This refers to the number of concurrent requests that the server can handle. The server is designed to process the engine’s tasks once the maximum number
                        of concurrent requests is reached, regardless of any additional requests sent by clients concurrently during that time. Default to None. Type: int
  --backend {pytorch,turbomind}
                        Set the inference backend. Default: turbomind. Type: str
  --log-level {CRITICAL,FATAL,ERROR,WARN,WARNING,INFO,DEBUG,NOTSET}
                        Set the log level. Default: ERROR. Type: str
  --api-keys [API_KEYS ...]
                        Optional list of space separated API keys. Default: None. Type: str
  --ssl                 Enable SSL. Requires OS Environment variables 'SSL_KEYFILE' and 'SSL_CERTFILE'. Default: False
  --model-name MODEL_NAME
                        The name of the served model. It can be accessed by the RESTful API `/v1/models`. If it is not specified, `model_path` will be adopted. Default: None.
                        Type: str
  --max-log-len MAX_LOG_LEN
                        Max number of prompt characters or prompt tokens beingprinted in log. Default: Unlimited. Type: int
  --disable-fastapi-docs
                        Disable FastAPI's OpenAPI schema, Swagger UI, and ReDoc endpoint. Default: False
  --allow-terminate-by-client
                        Enable server to be terminated by request from client. Default: False
  --chat-template CHAT_TEMPLATE
                        A JSON file or string that specifies the chat template configuration. Please refer to https://lmdeploy.readthedocs.io/en/latest/advance/chat_template.html
                        for the specification. Default: None. Type: str
  --tool-call-parser TOOL_CALL_PARSER
                        The registered tool parser name dict_keys(['internlm', 'llama3', 'qwen2d5', 'qwen', 'qwen3']). Default to None. Type: str
  --reasoning-parser REASONING_PARSER
                        The registered reasoning parser name from dict_keys(['deepseek-r1', 'qwen-qwq']). Default to None. Type: str
  --revision REVISION   The specific model version to use. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version. Type: str
  --download-dir DOWNLOAD_DIR
                        Directory to download and load the weights, default to the default cache directory of huggingface. Type: str
  --node-rank NODE_RANK
                        The current node rank. Default: 0. Type: int
  --nnodes NNODES       The total node nums. Default: 1. Type: int

PyTorch engine arguments:
  --adapters [ADAPTERS ...]
                        Used to set path(s) of lora adapter(s). One can input key-value pairs in xxx=yyy format for multiple lora adapters. If only have one adapter, one can only
                        input the path of the adapter. Default: None. Type: str
  --device {cuda,ascend,maca,camb}
                        The device type of running. Default: cuda. Type: str
  --eager-mode          Whether to enable eager mode. If True, cuda graph would be disabled. Default: False
  --dtype {auto,float16,bfloat16}
                        data type for model weights and activations. The "auto" option will use FP16 precision for FP32 and FP16 models, and BF16 precision for BF16 models. This
                        option will be ignored if the model is a quantized model. Default: auto. Type: str
  --tp TP               GPU number used in tensor parallelism. Should be 2^n. Default: 1. Type: int
  --session-len SESSION_LEN
                        The max session length of a sequence. Default: None. Type: int
  --max-batch-size MAX_BATCH_SIZE
                        Maximum batch size. If not specified, the engine will automatically set it according to the device. Default: None. Type: int
  --cache-max-entry-count CACHE_MAX_ENTRY_COUNT
                        The percentage of free gpu memory occupied by the k/v cache, excluding weights . Default: 0.8. Type: float
  --cache-block-seq-len CACHE_BLOCK_SEQ_LEN
                        The length of the token sequence in a k/v block. For Turbomind Engine, if the GPU compute capability is >= 8.0, it should be a multiple of 32, otherwise it
                        should be a multiple of 64. For Pytorch Engine, if Lora Adapter is specified, this parameter will be ignored. Default: 64. Type: int
  --enable-prefix-caching
                        Enable cache and match prefix. Default: False
  --max-prefill-token-num MAX_PREFILL_TOKEN_NUM
                        the max number of tokens per iteration during prefill. Default: 8192. Type: int
  --quant-policy {0,4,8}
                        Quantize kv or not. 0: no quant; 4: 4bit kv; 8: 8bit kv. Default: 0. Type: int
  --model-format {hf,awq,gptq,fp8}
                        The format of input model. `hf` means `hf_llama`, `awq` represents the quantized model by AWQ, and `gptq` refers to the quantized model by GPTQ. Default:
                        None. Type: str
  --dp DP               data parallelism. dp_rank is required when pytorch engine is used. Default: 1. Type: int
  --ep EP               expert parallelism. dp is required when pytorch engine is used. Default: 1. Type: int
  --enable-microbatch   enable microbatch for specified model. Default: False
  --enable-eplb         enable eplb for specified model. Default: False
  --role {Hybrid,Prefill,Decode}
                        Hybrid for Non-Disaggregated Engine;Prefill for Disaggregated Prefill Engine;Decode for Disaggregated Decode Engine;. Default: Hybrid. Type: str
  --migration-backend {DLSlime,Mooncake}
                        kvcache migration management backend when PD disaggregation. Default: DLSlime. Type: str

TurboMind engine arguments:
  --dtype {auto,float16,bfloat16}
                        data type for model weights and activations. The "auto" option will use FP16 precision for FP32 and FP16 models, and BF16 precision for BF16 models. This
                        option will be ignored if the model is a quantized model. Default: auto. Type: str
  --tp TP               GPU number used in tensor parallelism. Should be 2^n. Default: 1. Type: int
  --session-len SESSION_LEN
                        The max session length of a sequence. Default: None. Type: int
  --max-batch-size MAX_BATCH_SIZE
                        Maximum batch size. If not specified, the engine will automatically set it according to the device. Default: None. Type: int
  --cache-max-entry-count CACHE_MAX_ENTRY_COUNT
                        The percentage of free gpu memory occupied by the k/v cache, excluding weights . Default: 0.8. Type: float
  --cache-block-seq-len CACHE_BLOCK_SEQ_LEN
                        The length of the token sequence in a k/v block. For Turbomind Engine, if the GPU compute capability is >= 8.0, it should be a multiple of 32, otherwise it
                        should be a multiple of 64. For Pytorch Engine, if Lora Adapter is specified, this parameter will be ignored. Default: 64. Type: int
  --enable-prefix-caching
                        Enable cache and match prefix. Default: False
  --max-prefill-token-num MAX_PREFILL_TOKEN_NUM
                        the max number of tokens per iteration during prefill. Default: 8192. Type: int
  --quant-policy {0,4,8}
                        Quantize kv or not. 0: no quant; 4: 4bit kv; 8: 8bit kv. Default: 0. Type: int
  --model-format {hf,awq,gptq,fp8}
                        The format of input model. `hf` means `hf_llama`, `awq` represents the quantized model by AWQ, and `gptq` refers to the quantized model by GPTQ. Default:
                        None. Type: str
  --rope-scaling-factor ROPE_SCALING_FACTOR
                        Rope scaling factor. Default: 0.0. Type: float
  --num-tokens-per-iter NUM_TOKENS_PER_ITER
                        the number of tokens processed in a forward pass. Default: 0. Type: int
  --max-prefill-iters MAX_PREFILL_ITERS
                        the max number of forward passes in prefill stage. Default: 1. Type: int
  --communicator {nccl,native}
                        Communication backend for multi-GPU inference. Default: nccl. Type: str

Vision model arguments:
  --vision-max-batch-size VISION_MAX_BATCH_SIZE
                        the vision model batch size. Default: 1. Type: int
```
```bash
# basic command
lmdeploy serve api_server internlm/internlm2_5-7b-chat

# mendowload model untuk digunakan secara offline
huggingface-cli download Qwen/Qwen2-VL-2B-Instruct --local-dir /models/qwen --local-dir-use-symlinks False
huggingface-cli download THUDM/cogvlm-chat-hf --local-dir ./cogvlm-chat-hf --local-dir-use-symlinks False
huggingface-cli download lmsys/vicuna-7b-v1.5 special_tokens_map.json tokenizer.model tokenizer_config.json --local-dir ./cogvlm-chat-hf --local-dir-use-symlinks False

# command yg akan kita gunakan
lmdeploy serve api_server --server-port 23333 --model-path /models/qwen  --device cuda

```

command melihat model apa yg tersedia
```bash
curl -X GET http://localhost:9030/model \
	  -H "Content-Type: application/json"
```

expected output
```json
{
  "internvl":"OpenGVLab/InternVL3-8B-AWQ",
  "qween":"Qwen/Qwen2-VL-2B-Instruct",
  "debug":"test/model123"
}
```

ubah model dengan 
```bash
curl -X POST http://localhost:9030/model \
	-H "Content-Type: application/json" \
	-d '{"model": "qween"}'
```
cek status
```bash
curl -X GET http://localhost:9030/status \
	-H "Content-Type: application/json" 
```
expected output
```json
{
  "running":true,
  "pid":33,
  "model":"OpenGVLab/InternVL3-8B-AWQ"
}
```

jika dari dalam docker url nya bisa diubah
```bash
# .env
LMDEPLOY_URL="http://host.docker.internal:9030"
# atau bisa juga dengan 
LMDEPLOY_URL="http://yo.ur.i.p:9030"
```
	
