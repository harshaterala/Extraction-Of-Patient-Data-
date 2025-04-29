from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
from utils import parse_lab_report_text

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = FastAPI()

@app.post("/get-lab-tests")
async def get_lab_tests(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file)
        text = pytesseract.image_to_string(image, config='--psm 4')  


        lab_data = parse_lab_report_text(text)

        return JSONResponse(content={"is_success": True, "data": lab_data})
    except Exception as e:
        return JSONResponse(content={"is_success": False, "error": str(e)}, status_code=500)
