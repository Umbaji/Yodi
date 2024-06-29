from tensorflow.keras.models import load_model
AUTOTUNE = tf.data.AUTOTUNE
# Replace 'model.h5' with the path to your .h5 file

class Yodi():
  def __init__(self,file_path, version = "1", local = True, plot_specs = True ):
      self.FPATH = str(file_path)
      commands = np.array(tf.io.gfile.listdir(str(data_dir)))
      self.audio_binary = tf.io.read_file(self.FPATH)
      self.commands = commands[commands != 'README.md']
      print('Commands:', commands)
      self.pspectrogram = plot_specs 

  def get_spectrogram(self,waveform):
    # Zero-padding for an audio waveform with less than 16,000 samples.
    input_len = 16000
    waveform = waveform[:input_len]
    zero_padding = tf.zeros(
        [16000] - tf.shape(waveform),
        dtype=tf.float32)
    # Cast the waveform tensors' dtype to float32.
    waveform = tf.cast(waveform, dtype=tf.float32)
    # Concatenate the waveform with `zero_padding`, which ensures all audio
    # clips are of the same length.
    equal_length = tf.concat([waveform, zero_padding], 0)
    # Convert the waveform to a spectrogram via a STFT.
    spectrogram = tf.signal.stft(
        equal_length, frame_length=255, frame_step=128)
    # Obtain the magnitude of the STFT.
    spectrogram = tf.abs(spectrogram)
    # Add a `channels` dimension, so that the spectrogram can be used
    # as image-like input data with convolution layers (which expect
    # shape (`batch_size`, `height`, `width`, `channels`).
    spectrogram = spectrogram[..., tf.newaxis]
    return spectrogram

  def _decode_audio(self):
    # Decode WAV-encoded audio files to `float32` tensors, normalized
    # to the [-1.0, 1.0] range. Return `float32` audio and a sample rate.
    audio, _ = tf.audio.decode_wav(contents=self.audio_binary)
    # Since all the data is single channel (mono), drop the `channels`
    # axis from the array.
    mono_signal = tf.reduce_mean(audio, axis=-1, keepdims=True)
    return tf.squeeze(mono_signal, axis=-1)

  def get_label(self):
    constant = tf.constant(self.FPATH)
    parts = tf.strings.split(
        input=self.FPATH,
        sep=os.path.sep)
    # Note: You'll use indexing here instead of tuple unpacking to enable this
    # to work in a TensorFlow graph.
    return parts[-2]

  def get_spectrogram_and_label_id(self,audio, label):
    spectrogram = self.get_spectrogram(audio)
    label_id = tf.argmax(label == self.commands)
    return spectrogram, label_id

  def preprocess_data(self):
    files_ds = tf.data.Dataset.from_tensor_slices([str(self.FPATH)])
    output_ds = files_ds.map(
      map_func=self.get_waveform_and_label,
      num_parallel_calls=AUTOTUNE)
    output_ds = output_ds.map(
      map_func=self.get_spectrogram_and_label_id,
      num_parallel_calls=AUTOTUNE)
    return output_ds

  def get_waveform_and_label(self,file_path):
    label = self.get_label()
    waveform = self._decode_audio()
    return waveform, label

  def _load_(local=True, URL=""):
    if local:
        try:
            model = load_model('YodiV1.2-4.keras')
        except FileNotFoundError:
            print("Error: 'YodiV1.2-4.keras' not found. Trying to load from JSON.")
            try:
                json_file = open('YodiV1.2-4.json', 'r')
                loaded_model_json = json_file.read()
                json_file.close()
                model = model_from_json(loaded_model_json)
                model.load_weights("YodiV1.2-4_weights.h5")
            except FileNotFoundError:
                print("Error: 'YodiV1.2-4.json' or 'YodiV1.2-4_weights.h5' not found.")
                try:
                    # Fallback to a default model or raise an exception
                    model =  load_model('YodiV1.2-4.h5')
                except:
                    print("Error: Could not load any model.")
                    return None
            except OSError as e:
                print(f"Error loading model from JSON: {e}")
                return None
        except OSError as e:
            print(f"Error loading model from .keras: {e}")
            return None
    else:
        # Handle loading from URL
        pass  # Implement URL loading logic here

    return model

  def predict_from_path(self):
    model = self._load_(local=True)
    test_ds = self.preprocess_data()
    
    prediction = ""
    for spectrogram, label in test_ds.batch(1):
      prediction = model(spectrogram)
      if self.pspectrogram == True:
	      plt.bar(self.commands, tf.nn.softmax(prediction[0]))
	      plt.title(f'Predictions for "{self.commands[label[0]]}"')
	      plt.show()
      else :
      	y_pred = int(np.argmax(prediction, axis=1))
      	prediction_ = label[y_pred]

    return prediction_
