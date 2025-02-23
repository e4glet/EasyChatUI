# 测试当前运行环境是否支持GPU
# env_check.py
import torch
import psutil

def print_environment_info():
    """打印关键环境信息"""
    # PyTorch 配置
    print(f"[Framework] PyTorch {torch.__version__}")
    print(f"  CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"  CUDA version: {torch.version.cuda}")
        print(f"  GPU: {torch.cuda.get_device_name(0)}")
    
    # 系统资源
    mem = psutil.virtual_memory()
    print(f"[System] Physical Memory: {mem.total / 1024**3:.1f}GB")
    


if __name__ == "__main__":
    print_environment_info()