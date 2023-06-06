# Speech Processing and Synthesis of Voice Cloning with Emotion Transfer :

## Different Features that can be extracted from Speech in Python(not limited by this list, but these features should be sufficient):

> Mel Frequency Cepstral Coefficients (MFCCs): These coefficients capture important spectral information about speech signals. They are computed by taking the short-term Fourier transform of a windowed signal, filtering out high frequency components, and quantizing the resulting power spectrum into a set of mel bands.

> Pitch values: Speech contains both amplitude and pitch variations. Pitch values represent the estimated fundamental frequency of the speech signal, which can be used to estimate the speaker's mood or level of excitement.

> Spectral envelope: The spectral envelope represents the intensity pattern present in the speech signal over time. Features related to the shape of the spectral envelope, such as spectral centroid, rolloff measures, and bandwidth, provide additional insight into the nature of the sound.

> LSF (Lambert-Shaped Filterbank) parameters: LSF parameters provide perceptually meaningful representations of the acoustic properties of speech sounds based on a representation similar to that of human auditory processing.

> Voice quality analysis features: These include measurements of voice roughness, hoarseness, breathiness, and other factors that affect the quality of speech production.

> Acoustic energy: Acoustic energy reflects the overall loudness or strength of the audio signal.

> Zero crossing rate: Zero crossing rate indicates how quickly the sign of the waveform changes polarity. A high zero crossing rate corresponds to a more complex waveform.

> Spectrogram: A spectrogram is a graphical representation of the temporal and spectral content of a signal. In the context of speech recognition, spectrograms may reveal patterns in syllables, words, and phrases, allowing them to serve as useful features in machine learning models.

> Phoneme durations: Phoneme durations indicate the length of time spent pronouncing specific phonemes within a word or sentence. 

## Mel Frequency Ceptral Coefficients:

> If a cepstral coefficient has a positive value, the majority of the spectral energy is concentrated in the low-frequency regions. On the other hand, if a cepstral coefficient has a negative value, it represents that most of the spectral energy is concentrated at high frequencies.

> [MFCC Simplified explanation](https://medium.com/@tanveer9812/mfccs-made-easy-7ef383006040)



