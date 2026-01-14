from fastapi import FastAPI, Query

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/filter")
async def filter_values(
    min_val: int = Query(0, alias="min", ge=0),
    max_val: int = Query(100, alias="max", le=100)
):
    return {"min": min_val, "max": max_val}
# END
