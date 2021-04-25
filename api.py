import shutil
from fastapi import APIRouter, UploadFile, File, Form
from schemas import UploadVideo
from models import Video, User


video_router = APIRouter()


@video_router.post('/')
async def create_video(title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)):
    info = UploadVideo(title=title, description=description)
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    user = await User.objects.first()
    return await Video.objects.create(user_id=user, file=file.filename, **info.dict())


@video_router.get("/video/{video_pk}", response_model=Video)
async def get_video(video_pk: int):
    return await Video.objects.select_related('user_id').get(pk=video_pk)


@video_router.post('/user', response_model=User)
async def create_user(user: User):
    await user.save()
    return user


@video_router.get("/user/{user_id}", response_model=User)
async def get_user(user_pk: int):
    return await User.objects.get(pk=user_pk)
