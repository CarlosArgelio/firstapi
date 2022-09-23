from pydoc import describe
from fastapi import FastAPI
from fastapi import Body, Path
from data import Form


app = FastAPI()

@app.get('/helloWorld')
def home():
    return {"Hello": "World"}


@app.post('/create/')
def change_user(form: Form = Body(...)):
    return form

@app.get('/read/')
def read_user(form: Form = Body(...)):
    return form

@app.put('/update/{id_user}')
def update(
    id_user: int = Path(
        ...,
        title = "user_id",
        description = "Add the 'id' of the user to modify"
    ),
    form: Form = Body(...)
):
    return update

@app.delete('/delete/{id_user}')
def delete(
    id_user: int = Path(
        ...,
        title = "user_id",
        description = "Add the 'id' of the user to delete"
    ) 
):
    return delete