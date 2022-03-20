import json
import requests
from log4py.log4py import logger
from log4py.timeGenerator import timeGenerator
import os
import typer
from typing import Tuple

app = typer.Typer()

__version__ = "1.0.0"

blueberryPath = os.path.join(os.path.expanduser("~"), ".blueberry")

os.makedirs(os.path.join(blueberryPath, "logs"), exist_ok=True)
os.makedirs(os.path.join(blueberryPath, "repos"), exist_ok=True)

logFile = os.path.join(blueberryPath, "logs", timeGenerator("%Y%m%d-%H-%M-%S") + ".log")
log = logger(timeFormat="%H:%M:%S", logFile=logFile)

if os.path.isfile(os.path.join(blueberryPath, "LOCKFILE")):
    log.warn("Blueberry is already running. Cannot invoke 2nd instance.")
    log.warn("If this isn´t the case, delete the file '~/.blueberry/LOCKFILE'")
    log.error("Failed to launch, quitting...")
    exit(1)

if not os.path.isfile(os.path.join(blueberryPath, "repos", "default.json")):
    r = requests.get("")

@app.command()
def update():
    pass

@app.command()
def install(pkgstr: str):
    pkgs = pkgstr.split(",")

if __name__ == '__main__':
    app()