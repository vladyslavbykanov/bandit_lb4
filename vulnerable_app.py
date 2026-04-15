import hashlib
import os
import pickle
import subprocess
import tempfile


PASSWORD = "admin123"


def unsafe_eval(user_input: str) -> object:
    return eval(user_input)


def unsafe_pickle(data: bytes) -> object:
    return pickle.loads(data)


def unsafe_command(user_input: str) -> None:
    os.system("ping -c 1 " + user_input)


def unsafe_subprocess(user_input: str) -> None:
    subprocess.Popen("ls " + user_input, shell=True)


def weak_hash(data: str) -> str:
    return hashlib.md5(data.encode()).hexdigest()


def insecure_tempfile() -> str:
    name = tempfile.mktemp()
    return name
