from flask import Flask, request, render_template, send_from_directory
import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load your trained model
model_path = "E:\Project\XCP.h5"
try:
    loaded_model = tf.keras.models.load_model(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading the model: {e}")
    loaded_model = None

# Define the class labels (make sure these match your training)
class_labels = ['im_Dyskeratotic', 'im_Koilocytotic', 'im_Metaplastic', 'im_Parabasal', 'im_Superficial-Intermediate']
img_size = (224, 224)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict_image(img_path):
    if loaded_model is None:
        return "Model not loaded.", None
    try:
        img = load_img(img_path, target_size=img_size)
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize the image

        predictions = loaded_model.predict(img_array)
        predicted_class_index = np.argmax(predictions)
        confidence = predictions[0][predicted_class_index]
        predicted_class_label = class_labels[predicted_class_index]
        return predicted_class_label, confidence
    except Exception as e:
        return f"Error processing image: {e}", None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test', methods=['GET', 'POST'])
def test_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            prediction, confidence = predict_image(filepath)
            if confidence is not None:
                return render_template('test.html', prediction=prediction, confidence=f"{confidence:.2f}", image_path=filename)
            else:
                return render_template('test.html', error=prediction, image_path=filename)
        return "Invalid file type"
    return render_template('test.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    # Create the 'uploads' directory if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True, host='0.0.0.0')