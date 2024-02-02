import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr


class UsersBase(BaseModel):
    email: EmailStr
    phone: int
    fam: str
    name: str
    otc: Optional[str] = None
    
    class Config:
        orm_mode = True


class CoordsBase(BaseModel):
    latitude: str
    longitude: str
    height: str

    class Config:
        orm_mode = True


class LevelBase(BaseModel):
    winter: Optional[str] = None
    summer: Optional[str] = None
    autumn: Optional[str] = None
    spring: Optional[str] = None

    class Config:
        orm_mode = True


class FotoRaw(BaseModel):
    data: Optional[bytes] = None
    title: Optional[str] = None

    class Config:
        orm_mode = True


# поля, отправленные в теле запроса (JSON)
class AddedRaw(BaseModel):
    beauty_title: str
    title: str
    other_titles: Optional[str] = None
    connect: Optional[str]
    add_time: str
    user: UsersBase
    coords: CoordsBase
    level: LevelBase
    images: List[FotoRaw]


class AddedBase(BaseModel):
    add_time: datetime.datetime
    beauty_title: str
    title: str
    other_titles: Optional[str]
    connect: Optional[str]
    user_id: int
    coords_id: int
    level_id: int
    status: Optional[str] = None

    class Config:
        orm_mode = True


class FotoBase(BaseModel):
    date_added: datetime.datetime
    img: Optional[bytes] = None
    title: Optional[str] = None

    class Config:
        orm_mode = True


class ImagesBase(BaseModel):
    pereval_id: int
    foto_id: int
