from enum import Enum
from typing import TypedDict

class MimeTypes(Enum):
    JSON = "application/json"
    CHOICE = "text/x.enum"

class WorkType(Enum):
    SLIDES = 'slides'
    CODE = 'code'
    SHEET = 'sheet'
    DOC = 'doc'
    IMG = 'img'
    OTHER = 'other'

class Resources(TypedDict):
    name:str
    type: str
    url: str


class Code(TypedDict):
    file_name: str
    content: str

class CodeProj(TypedDict):
    explanation: str
    files: list[Code]


class workTask(TypedDict):
    workType: WorkType
    Task: str


class Slide(TypedDict):
    title: str
    content: str
    image: list[str]

class Doc(TypedDict):
    title: str
    introduction: str
    development: str
    conclusion: str
    references: str

class Task(TypedDict):
    title: str
    author: str
    register: str
    date: str
    subject:str
    desc: str
    professor: str
    cat:str
    resources: list[Resources]
    work: CodeProj | Slide | Doc

class ArtStyles(Enum):
    NO_STYLE ='(No style)'
    CINEMATIC ='Cinematic'
    PHOTOGRAPHIC ='Photographic'
    ANIME ='Anime'
    MANGA ='Manga'
    DIGITAL_ART ='Digital Art'
    PIXEL_ART ='Pixel art'
    FANTASY_ART ='Fantasy art'
    NEOPUNK ='Neonpunk'

class Art(TypedDict):
    subject_general: list[str]
    subject_lighting:list[str]
    background_general:list[str]
    background_lighting:list[str]
    theme: list[str]
    vibe:list[str]
    style: ArtStyles


class JSON_SCHEMAS(Enum):
    SLIDES = "slides"
    DOC = "doc"
    # CODE = "code"
    TASK = "task"
    ART = "art"
    CODE_PROJ = "code"

schema_types = {
    JSON_SCHEMAS.SLIDES: list[Slide],  # Mapping the SLIDES enum to list[Slide]
    JSON_SCHEMAS.DOC: Doc,             # Mapping the DOC enum to Doc
    # JSON_SCHEMAS.CODE: Code,           # Mapping the CODE enum to Code
    JSON_SCHEMAS.TASK: list[workTask], # Mapping the TASK enum to list[WorkTask]
    JSON_SCHEMAS.ART: Art, # Mapping the TASK enum to list[WorkTask]
    JSON_SCHEMAS.CODE_PROJ: CodeProj
}

schema_mapping = {
    "slides": JSON_SCHEMAS.SLIDES,
    "doc": JSON_SCHEMAS.DOC,
    "code": JSON_SCHEMAS.CODE_PROJ,
    "task": JSON_SCHEMAS.TASK,
    "art": JSON_SCHEMAS.ART,
}
