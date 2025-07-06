# -Deep-Learning-Based-Classification-of-Cervical-Cell-Abnormalities-from-Pap-Smear-Images-

1)	Instruction for running the deep leaning algorithm to train models:
●	Download the Dataset:
  i.	Download with the link: https://www.kaggle.com/datasets/prahladmehandiratta/cervical-cancer-largest-dataset-sipakmed
  ii.	Extract to a location in local disk for running Jupyter .
●	Open the folder named “Project”.
●	Find the script named “Algo.ipynb” run it through either colab or jupyter notebook.
●	Make sure to have set the path for datasets and path where to save the models after training.

2)	For running the web application in local hosting:
●	Create a python virtual environment:
  o	In cmd create a virtual environment using “python -m venv papsmear”
  o	Activate the virtual environment using “papsmear\Scripts\activate”.
  o	Extract & Cut the Project folder attached with these docs and paste it inside papsmear.
●	Install required libraries:
  o	In cmd open the project folder, find requirements.txt and run it using cmd “pip install -r requirements.txt”.
●	Download the Dataset:
  o	Download with the link: https://www.kaggle.com/datasets/prahladmehandiratta/cervical-cancer-largest-dataset-sipakmed
  o	Extract the dataset inside papsmear folder.
●	Run the program to start local host
  o	Change the model path according to system inside “app.py”.
  o	Now run app.py from project folder using “python app.py” in cmd .
●	For classification and prediction:
  o	Open the default local host url: http://127.0.0.1:5000
  o	 Click on Test button.
  o	Add the testing image from the selector and press predict button
  o	Output will be displayed.

