import argparse
import os
import subprocess
import sys


APP_NAME = "VoiceTranscriber"
ENTRYPOINT = "app.py"


def run_pyinstaller(mode: str) -> None:
    if mode == "onefile":
        extra = ["--onefile"]
    else:
        extra = ["--onedir"]

    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--windowed",
        "--name",
        APP_NAME,
        *extra,
        ENTRYPOINT,
    ]

    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Сборка исполняемого файла GUI-транскрибатора"
    )
    parser.add_argument(
        "--mode",
        choices=["onefile", "onedir"],
        default="onefile",
        help="onefile = один исполняемый файл, onedir = папка с exe и зависимостями",
    )
    args = parser.parse_args()

    os.makedirs("dist", exist_ok=True)
    run_pyinstaller(args.mode)

    print("\nСборка завершена.")
    if args.mode == "onefile":
        print("Ищите файл в папке dist/ (например, VoiceTranscriber.exe на Windows).")
    else:
        print("Ищите папку dist/VoiceTranscriber/ с исполняемым файлом внутри.")


if __name__ == "__main__":
    main()
