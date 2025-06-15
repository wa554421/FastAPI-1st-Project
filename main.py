from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from bson import ObjectId
from fastapi.responses import RedirectResponse
from db import collection

app = FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")
template = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
async def waleed(request: Request):
    notes = list(collection.find())
    for note in notes:
        note["_id"] = str(note["_id"]) 
    return (template.TemplateResponse('index.html',{"request": request,"notes": notes}))

@app.get("/about",response_class=HTMLResponse)
async def about(request: Request):
    return (template.TemplateResponse('about.html',{"request": request}))


@app.post("/submit",response_class=HTMLResponse)
async def form_read(request: Request , name: str = Form(...) , msg: str = Form(...)):
    collection.insert_one({
        "name":name,
        "msg":msg
    })
    return template.TemplateResponse('submit.html',{
        "request":request,
        "name":name,
        "msg": msg
    })

@app.post("/",response_class=HTMLResponse)
async def delete_form(request: Request,note_id: str = Form(...) ):
    collection.delete_one({"_id": ObjectId(note_id)})
    return RedirectResponse("/",status_code=303)
    



# 🔸 Context Passing to a Template Engine
# Framework	Template Engine	Context passed using
# Django	Django Templates	return render(request, "template.html", context)
# FastAPI	Jinja2 (usually)	TemplateResponse("template.html", context)

# So this technique is:

# 🧠 Name:
# Template Context Rendering using Django Template Language (DTL) or Jinja2.

# ✅ You're passing a Python dictionary (called context) to the HTML template.