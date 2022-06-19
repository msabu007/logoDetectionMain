import uvicorn
from fastapi import FastAPI, File, UploadFile
import uuid

from components import prediction, read_img

app = FastAPI()

#api 
@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):

   
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()

    image = read_img(contents)
    predictions = prediction(image)
    return predictions


if __name__ == "__main__":
    uvicorn.run(app, debug=True)
