# Yodi

This is the official repository for YodiV1, the speech recognition model for 10 words, in Ewè. The Yodi package is also useful for rapid inference on speech data, especially on the mini_speech datasets.

## Yodi, Your Speech Recognition Model

Welcome to the Yodi Model! This model is designed to perform inference on audio files, providing a prediction of the audio command. Visit our Hugging Face page or contact contact@umbaji.org to access your model now !

## Requirements

This project requires Python 3.6 or later. To install all the necessary packages run:

```bash
pip install -r requirements.txt
```

## Project Contents
This project contains the following files:
- yodi.py: The main Python script where the model is defined and used for prediction.

## How to Run
Clone the repo (if installing via git): 
```bash
git clone https://github.com/Umbaji/Yodi.git
```
Navigate to the cloned directory.

Run the script in the terminal: 
```bash
python Yodi.py
```
## Usage
First, make sure you load your audio into the appropriate test folder.

The Yodi class in yodi.py is initialized with the following parameters:

- file_path: The path to the audio file for prediction.
- version: The version of the model to use (default is “1”).
- local: Whether to load the model locally or from a URL (default is True).
- plot_specs: Whether to plot the inference results (default is False).
After initializing a Yodi object, call the predict_from_path() method to get the prediction for the audio command.

You can also use it to train our model via the umni_speech dataset avaible on our github page :https://github.com/Umbaji/umni_speech


Example

## Example
```python
from pathlib import Path

if __name__ =="__main__":
    
DATASET_PATH = '~/umini_speech/test_set/'
data_dir = pathlib.Path(DATASET_PATH)

if not data_dir.exists():
        print("Dowload the test_set folder from the repo: https://github.com/Umbaji/Yodi.git")
        pass
        
yodi_instance = Yodi(file,version = "1", local = True,plot_specs = "True")
yodi_instance.predict_from_path()

```

If Yodi misses the prediction on your input that means that it has not enough data !

Contribute to leverage afircan language model by adding your input audio to our umini_speech dataset here :
https://github.com/Umbaji/umni_speech

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
