from PyQt5 import QtWidgets, QtGui, uic
import time
import threading
import pyaudio
import wave

class Recorder(object):
    '''A recorder class for recording audio to a MP3 file.
    Records in mono by default.
    '''
    def __init__(self, channels=1, rate=44100, frames_per_buffer=1024):
        self.channels = channels
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer

    def open(self, fname, mode='wb'):
        return RecordingFile(fname, mode, self.channels, self.rate, self.frames_per_buffer)


class RecordingFile(object):
    def __init__(self, fname, mode, channels,rate, frames_per_buffer):
        self.fname = fname
        self.mode = mode
        self.channels = channels
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer
        self._pa = pyaudio.PyAudio()
        self.wavefile = self._prepare_file(self.fname, self.mode)
        self._stream = None

    def __enter__(self):
        return self

    def __exit__(self, exception, value, traceback):
        self.close()

    def record(self, duration):
        # Use a stream with no callback function in blocking mode
        self._stream = self._pa.open(format=pyaudio.paInt16,
                                        channels=self.channels,
                                        rate=self.rate,
                                        input=True,
                                        frames_per_buffer=self.frames_per_buffer)
        for _ in range(int(self.rate / self.frames_per_buffer * duration)):
            audio = self._stream.read(self.frames_per_buffer)
            self.wavefile.writeframes(audio)
        return None

    def start_recording(self):
        # Use a stream with a callback in non-blocking mode
        self._stream = self._pa.open(format=pyaudio.paInt16,
                                        channels=self.channels,
                                        rate=self.rate,
                                        input=True,
                                        frames_per_buffer=self.frames_per_buffer,
                                        stream_callback=self.get_callback())
        self._stream.start_stream()
        return self

    def stop_recording(self):
        self._stream.stop_stream()
        return self

    def get_callback(self):
        def callback(in_data, frame_count, time_info, status):
            self.wavefile.writeframes(in_data)
            return in_data, pyaudio.paContinue
        return callback

    def close(self):
        self._stream.close()
        self._pa.terminate()
        self.wavefile.close()

    def _prepare_file(self, fname, mode='wb'):
        wavefile = wave.open(fname, mode)
        wavefile.setnchannels(self.channels)
        wavefile.setsampwidth(self._pa.get_sample_size(pyaudio.paInt16))
        wavefile.setframerate(self.rate)
        return wavefile


class Recording(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.shutdownFlag = threading.Event()
        self.rec = Recorder(channels=2)

    def generateFileName(self):
        return 'recording ' + str(time.time()) + '.mp3'

    def run(self):
        with self.rec.open(self.generateFileName(), 'wb') as self.recfile2:
            self.recfile2.start_recording()
            while not self.stopped():
                pass

    def stop(self):
        self.shutdownFlag.set()
        self.recfile2.stop_recording()

    def stopped(self):
        return self.shutdownFlag.is_set()


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = uic.loadUi("gui.ui")
        self.connectButtonsToFunctions()

    def printInTextBox(self,message):
        self.ui.displayText.setText(message)

    def connectButtonsToFunctions(self):
        try:
            self.ui.startButton.clicked.connect(self.startButtonClicked)
            self.ui.stopButton.clicked.connect(self.stopButtonClicked)
        except AttributeError as e:
            print("Either the object does not exist or it's connection function does not exist")
        except Exception as e:
            print(e)

    def startButtonClicked(self):
        print("startButtonClicked")
        self.recordingThread = Recording()
        self.recordingThread.start()

    def stopButtonClicked(self):
        print("stopButtonClicked")
        self.recordingThread.stop()