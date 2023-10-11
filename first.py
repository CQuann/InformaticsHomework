import struct
import wave

inp = wave.open('in.wav', mode='rb')
out = wave.open('result1.wav', mode='wb')
amount_frames = inp.getnframes()
data = struct.unpack("<" + str(amount_frames) + "h", inp.readframes(amount_frames))
updated_data = data[::2]
updated_frames = struct.pack("<" + str(len(updated_data)) + "h", *updated_data)
out.writeframes(updated_frames)
inp.close()
out.close()
