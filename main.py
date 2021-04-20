import shutil
from typing import List
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post('/')
async def root(file: UploadFile = File(...)):
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {'file_name': file.filename}


@app.post('/img')
async def root(files: List[UploadFile] = File(...)):
    for img_file in files:
        with open(f'{img_file.filename}', 'wb') as buffer:
            shutil.copyfileobj(img_file.file, buffer)
    return {'status': 'Good'}
