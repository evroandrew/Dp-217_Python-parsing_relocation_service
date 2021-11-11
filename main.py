from fastapi import FastAPI
from fastapi.responses import JSONResponse
from scripts import parse

app = FastAPI(title="HostelParser")


@app.get("/relocation/data")
def parse_specialities():
    try:
        return JSONResponse({'content': parse()})
    except ValueError as e:
        return JSONResponse(status_code=500)
