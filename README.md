# Транскрибатор голоса (GUI)

Небольшое desktop-приложение на Python с тёмным интерфейсом:
- большая кнопка **СТАРТ / СТОП** для записи;
- распознавание речи с микрофона (русский язык);
- сохранение результата в **TXT**, **DOCX** и **PDF**.

## Запуск из исходников

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

## Сборка в исполняемый файл

Поддерживаются **оба варианта**, которые вы просили:
1. **Один обычный исполняемый файл** (`--mode onefile`)
2. **Папка с исполняемым файлом и вспомогательными файлами** (`--mode onedir`)

### Windows (PowerShell / CMD)

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python build.py --mode onefile
# или
python build.py --mode onedir
```

Результат:
- `dist/VoiceTranscriber.exe` (для `onefile`),
- или `dist/VoiceTranscriber/` с `VoiceTranscriber.exe` внутри (для `onedir`).

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python build.py --mode onefile
# или
python build.py --mode onedir
```

Результат будет в папке `dist/`.

## Зависимости

- `SpeechRecognition` — распознавание речи
- `PyAudio` — доступ к микрофону
- `python-docx` — экспорт в DOCX
- `reportlab` — экспорт в PDF
- `pyinstaller` — сборка исполняемого файла

## Примечания

- Для распознавания используется `recognize_google`, нужен интернет.
- Если `PyAudio` не ставится, установите системные аудио-библиотеки (например, `portaudio`).
