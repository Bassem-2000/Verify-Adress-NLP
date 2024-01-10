from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import concurrent.futures

# Load the model
loaded_model = load_model('my_model.h5')

# Load the tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    loaded_tokenizer = pickle.load(handle)

# Maximum sequence length used during training

maxlen = 20

app = FastAPI()

class TextRequest(BaseModel):
    text: str

def predict(text):
    # Preprocess the text
    sequence = loaded_tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=maxlen)
    
    # Make prediction using the loaded model
    prediction = loaded_model.predict(padded_sequence)
    # Assuming the output is a probability, you might want to return a rounded value (0 or 1)
    rounded_prediction = int(round(prediction[0][0]))
    
    return rounded_prediction

@app.post("/predict/")
async def predict_sentiment(request: TextRequest):
    text = request.text
    
    # Use ThreadPoolExecutor to parallelize predictions
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = executor.submit(predict, text)
        prediction = result.result()
        
    if rounded_prediction == 1:
        return {"prediction: القاهرة"}
    if rounded_prediction == 0:
        return {"prediction: ليست القاهرة"}
