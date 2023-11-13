import requests
from PIL import Image
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array
import mlflow
import os

os.environ['MLFLOW_TRACKING_USERNAME'] = 'user'
os.environ['MLFLOW_TRACKING_PASSWORD'] = 'K1aLXzz0QW'

# Configuration de MLflow
mlflow.set_tracking_uri('http://20.67.145.120:80')
mlflow.set_experiment("image_classification_experiment")



# Télécharge une image depuis Internet
def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        return img
    else:
        return None

# Prédit le contenu de l'image
def predict_image(model, img):
    img_resized = img.resize((224, 224))
    img_array = img_to_array(img_resized)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)
    return decode_predictions(predictions, top=1)[0][0]

# URL de l'image
image_url = 'https://www.manutan.fr/fstrz/r/s/www.manutan.fr/img/S/GRP/ST/AIG18043952.jpg?frz-v=96'  # Remplacez avec l'URL de l'image que vous souhaitez analyser

# Enregistrement du processus avec MLflow
with mlflow.start_run():
    # Télécharge et analyse l'image
    img = download_image(image_url)
    if img is not None:
        model = MobileNetV2(weights='imagenet')
        prediction = predict_image(model, img)
        
        # Log information
        mlflow.log_param("image_url", image_url)
        mlflow.log_metric("prediction_confidence", float(prediction[2]))

        # Log l'image
        img.save("predicted_image.jpg")
        mlflow.log_artifact("predicted_image.jpg")
        
        # Log an instance of the trained model for later use
        mlflow.tensorflow.log_model(model, artifact_path="object-detection")

        # Affiche l'image et la prédiction
        plt.imshow(img)
        plt.axis('off')
        plt.title(f"Prédiction: {prediction[1]} (Confiance: {prediction[2]*100:.2f}%)")
        plt.show()
    else:
        print("L'image n'a pas pu être téléchargée.")
