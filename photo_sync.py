
import os
from pathlib import Path
from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

PHOTO_DIR = Path(os.getenv("STORAGE_DIR", "/app/storage")) / "photos"
SECRET = os.getenv("PHOTO_SYNC_SECRET")


def check_secret(secret: str | None):
    if not SECRET or not secret or secret != SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.get("/photos")
def list_photos(x_sync_secret: str | None = Header(default=None)):
    check_secret(x_sync_secret)
    return [
        p.name for p in PHOTO_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png"}
    ]


@app.get("/photos/{filename}")
def get_photo(
    filename: str,
    x_sync_secret: str | None = Header(default=None),
):
    check_secret(x_sync_secret)

    # Не разрешаем обращаться за пределы папки фотографий.
    if Path(filename).name != filename:
        raise HTTPException(status_code=400, detail="Invalid filename")

    path = PHOTO_DIR / filename
    if not path.is_file():
        raise HTTPException(status_code=404, detail="Not found")

    return FileResponse(path)
