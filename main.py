from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from rembg import remove
import io

app = FastAPI()

@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    input_bytes = await file.read()
    output_bytes = remove(input_bytes)
    return StreamingResponse(io.BytesIO(output_bytes), media_type="image/png")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # ← ここでPORT環境変数を見る
    uvicorn.run("main:app", host="0.0.0.0", port=port)