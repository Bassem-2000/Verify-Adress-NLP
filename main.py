from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

loaded_model = load_model('model.h5')

with open('tokenizer.pickle', 'rb') as handle:
    loaded_tokenizer = pickle.load(handle)

maxlen = 20

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/predict/")
async def predict_sentiment(request: TextRequest):
    text = request.text
    
    sequence = loaded_tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=maxlen)
    
    prediction = loaded_model.predict(padded_sequence)
    rounded_prediction = int(round(prediction[0][0]))
    if rounded_prediction == 1:
        return {"prediction: القاهرة"}
    if rounded_prediction == 0:
        return {"prediction: ليست القاهرة"}
