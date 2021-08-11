import pickle
from fastapi import FastAPI
import pandas as pd

app = FastAPI()
@app.post('/model')
## Coloque seu codigo na função abaixo
def titanic(Sex:int, Age:float, Lifeboat:int, Pclass:int):
    #with open('./model/Titanic.pkl', 'rb') as fid: 
        #titanic = pickle.load(fid)
    
    titanic = pickle.load(open('app/model/Titanic.pkl','rb'))
   
    df = pd.DataFrame([[Age, Lifeboat, Pclass, Sex]], columns =['Age', 'Lifeboat', 'Pclass', 'Sex'])

    y = titanic.predict(df)

    response = {
                "survived": bool(y[0]),
                "status": 200,  
                "message": "SUCCESS",    
               }
    return response

@app.get('/model')
def get():
    return {'hello':'test'}











