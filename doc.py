from fastapi import FastAPI, Body, Path
from pydantic import BaseMode, field 
from typing import Optional, List
from fastapi.responses import HTMLResponse, JSONResponse

# Estamos creando una instancia de la clase FastAPI
app = FastAPI()

# Cambios a la documentacion
app.title = "La super API" 
app.version = "1.0.0"

# Ahora crearemos nuestro primer endpoint 
@app.get("/", tags=['home']) # Aqui se agrega la ruta de inicio
def message():
    return HTMLResponse(content="<h1> Bienvenido a mi API </h1>")
import time
class Movie:
    id: Optional[int] = None
    tit: str = field(min_length=2, max_length=40)
    overview: str = field(min_length=20, max_length=300)
    year: int = field(le=time.localtime().tm_year)
    rating: float = field(ge=0, le=10)
    category: str = field(min_length=5, max_length=12)

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

@app.get("/", tags=['home'])
def message ():
    return HTMLResponse(content="<h1>Hola mundo!!!</h1>")


@app.get("/movies", tags=['movies'], response_model = List[Movie], status_code=200)
def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies)

@app.get("/movies/{id}", tags=['movies'],response_model=Movie,status_code=200)
def get_movie(id:int = Path(ge=1, ie=2000)):
    movie = list(filter(lambda movie : movie['id'] == id, movies))
    if len(movie) >0:
        response = JSONResponse(content==movie, status_code=200)
    else:
        response = JSONResponse(content={"message": "movie not found"})
    return movie

@app.get("/movies/", tags = ['movies'])
def get_movies_by_category(category:str):
    movie = [movie for movie in movies if movie['catgory']==category]
    return movie

@app.post("/movies", tags=['movies'])
def create_movie(id: int = Body(),
                 title: str = Body(),
                 overview: str = Body(),
                 year: str =Body(),
                 rating: float = Body(),
                 category: str = Body()):
    movies.append({
        'id' : id,
        'title' : title,
        'overview' : overview,
        'year' : year,
        'rating' : rating,
        'category' : category
    })
    return movies

@app.put("/movies/{id}", tags=['movies'])
def create_movie(id: int,
                 title: str = Body(),
                 overview: str = Body(),
                 year: str =Body(),
                 rating: float = Body(),
                 category: str = Body()):
    for movie in movies:
        if movie ['id'] == id:
            movie['title'] = title,
            movie['overview'] = overview,
            movie['year'] = year,
            movie['rating'] = rating,
            movie['category' ] = category
    return movies

@app.delete("/movies/{id}", tags=['movies'], response_model=dict)
def delete_movie(id: int) -> dict:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
    return JSONResponse(content={"message": "Movie deleted successfully"})
