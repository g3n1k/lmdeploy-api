from fastapi import FastAPI, Request, HTTPException, Header
import subprocess
import os
import signal
import threading
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
model_process = None
current_model_path = None
pid_file = "lmdeploy.pid"

# Token rahasia dari .env
SECRET_TOKEN = os.getenv("ACCESS_TOKEN", "supersecrettoken123")

def stream_output(process):
    for line in iter(process.stdout.readline, b''):
        print(f"[lmdeploy] {line.decode().rstrip()}")

@app.on_event("startup")
async def startup_event():
    global model_process, current_model_path
    model_path = "OpenGVLab/InternVL3-8B-AWQ"
    current_model_path = model_path

    model_process = subprocess.Popen(
        ["lmdeploy", "serve", "api_server", model_path, "--device", "cuda", "--server-port", "23333"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    threading.Thread(target=stream_output, args=(model_process,), daemon=True).start()
    print(f"[startup] lmdeploy started with model: {model_path}")

@app.post('/model')
async def switch_model(request: Request):
    global model_process, current_model_path

    data = await request.json()
    key = "MODEL_" + data.get("model")
    model_path = os.getenv(key)

    print(f"[switch_model] Looking for key: {key}")
    print(f"[switch_model] model_path = {model_path}")

    if not model_path:
        raise HTTPException(status_code=400, detail="Model not found in .env")

    # kill old process if running
    if model_process and model_process.poll() is None:
        print(f"[switch_model] Terminating old model: {current_model_path}")
        os.kill(model_process.pid, signal.SIGTERM)
        model_process.wait()

    # start new process
    model_process = subprocess.Popen(
        ["lmdeploy", "serve", "api_server", model_path, "--device", "cuda", "--server-port", "23333"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    current_model_path = model_path
    threading.Thread(target=stream_output, args=(model_process,), daemon=True).start()

    with open(pid_file, "w") as f:
        f.write(str(model_process.pid))

    print(f"[switch_model] Switched to model {model_path}")

    return {"message": f"Switched to model {model_path}", "pid": model_process.pid}

@app.get("/status")
async def status():
    return {
        "running": model_process.poll() is None if model_process else False,
        "pid": model_process.pid if model_process else None,
        "model": current_model_path
    }

@app.get("/model")
async def available_models():
    return {
        k[6:]: v for k, v in os.environ.items() if k.startswith("MODEL_")
    }
