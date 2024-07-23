# import package
from fastapi import FastAPI, Request, Header, HTTPException
import pandas as pd


# password/api key
API_KEY = "testingapitokenkey1234" #testing api token key 1234
# Create new dataframe
df = pd.DataFrame()

# Populate dataframe
df['UserName'] = ['Undertaker', 'Rey Mysterio', 'Edge']
df['Location'] = ['Texas', 'Mexico', 'Colorado']

# create a FastAPI() object
app = FastAPI()

# make a url + function (endpoint) used by user
# call the variable
# endpoint to retrieve data, get has the parameter of the url
# to retrieve all data, param is /
# http://www.domain.com/...
# endpoint get all data from dataframe
# domain.com/data/texas -> return data with location texas
@app.get("/data/{loc}")
def handlerDf(loc):
    # filter dataframe with param set by user
    result = df.query(f"Location == '{loc}'")
    return result.to_dict(orient="records")

# endpoint secret
@app.get("/secret")


# python function to handle the get request above
# has to be placed close to endpoint, dont leave too much space between the two lines of code


def handlerSecret(api_key: str = Header(None)):
   # check api_key
   if api_key != API_KEY or api_key == None:
       raise HTTPException(detail = "wrong password!", status_code=401)


   return{
       "secret" : "my name is john cena"
   }


# when you add more code in the function restart uvicorn, using CTRL C
# request= name of param, Request = type of data
# request: Request is to see the request in the header
