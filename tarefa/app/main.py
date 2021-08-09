import pickle
from fastapi import FastAPI
import numpy as np

app = FastAPI()

model = pickle.load(open('app/model/Titanic.pkl','rb'))

@app.get('/model')
def get ():
    return

@app.post('/model/')
def titanic(Sex:int, Age: float, Lifeboat: int, Pclass: int):
    
    teste = np.array([[Sex,Age,Lifeboat,Pclass]])

    classe = model.predict(teste)[0]

    if(classe==1):
        return {"survived": classe,
	            "status": "int",
                "message": "Sobreviveu"
        }
    else:
        return {"survived": classe,
	            "status": "int",
                "message": "Não Sobreviveu"
                }











