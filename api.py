import shutil
from typing import List
from fastapi import APIRouter, UploadFile, File, Form, Request
from fastapi.responses import JSONResponse
from schemas import UploadVideo, GetVideo, User, Message
from models import Video


video_router = APIRouter()


@video_router.post('/')
async def root(title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)):
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    info = UploadVideo(name=title, description=description)
    return {'file_name': file.filename, 'info': info}


@video_router.post('/img', status_code=201)
async def root(files: List[UploadFile] = File(...)):
    for img_file in files:
        with open(f'{img_file.filename}', 'wb') as buffer:
            shutil.copyfileobj(img_file.file, buffer)
    return {'status': 'Good'}


@video_router.get('/video', response_model=GetVideo, responses={404: {"model": Message}})
async def get_video():
    video = UploadVideo(**{'name': 'Test', 'description': 'Description'})
    user = User(**{'id': 5, 'name': 'Test'})
    # return GetVideo(user=user, video=video)
    return JSONResponse(status_code=404, content={'message': 'Item not found'})


@video_router.post('/video', response_model=Video)
async def create_video(video: Video):
    await video.save()
    return video
