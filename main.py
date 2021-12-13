from fastapi import FastAPI
from fastapi.responses import JSONResponse
from scripts import parse
import uvicorn

app = FastAPI(title='HousingParser')


@app.get('/relocation/data')
def parse_specialities():
    try:
        return JSONResponse({'content': parse()})
    except ValueError as e:
        return JSONResponse(status_code=500)


if __name__ == '__main__':
    uvicorn.run(app, port=os.environ.get('PORT', 8090), host='localhost')
