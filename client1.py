from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient('127.0.0.1', 65432)
t = threading.Thread(target=sender.start_stream, args=("send",))
t.start()

while input('') != 'STOP':
    continue

sender.stop_stream()