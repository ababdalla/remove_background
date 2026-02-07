import io
import os

import numpy as np
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from PIL import Image
from rembg import remove

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    output = remove(image)
    if isinstance(output, np.ndarray):
        output = Image.fromarray(output)

    buffer = io.BytesIO()
    output.save(buffer, format="PNG")  # pyright: ignore[reportAttributeAccessIssue]
    buffer.seek(0)

    return Response(content=buffer.getvalue(), media_type="image/png")


app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("backend.api.main:app", host="0.0.0.0", port=port)
