import struct
import wave


#Если в 25 строке использовать h, как в прошлых задачах, то начинает ругаться, что слишком большие числа, хотя они входят
#в указанный в консоли диапазон значений. При замене на i(выделяется 4 байта на фрейм) все работает, но звук крайне плохой
#Пока не разобрался, как фиксить
def change_volume(param='louder', a=2.0):
    inp = wave.open('../in.wav', mode='rb')
    out = wave.open('result3.wav', mode='wb')
    out.setparams(inp.getparams())
    amount_frames = inp.getnframes()
    data = struct.unpack("<" + str(amount_frames) + "h", inp.readframes(amount_frames))
    updated_data = []
    for i in data:
        if param == 'louder':
            if int(data[i] * a) < 32767:
                updated_data.append(int(data[i] * a))
            else:
                updated_data.append(32766)
        elif param == 'quieter':
            if data[i] // a > -32768:
                updated_data.append(int(data[i] // a))
            else:
                updated_data.append(-32768)
    updated_frames = struct.pack("<" + str(len(updated_data)) + "i", *updated_data)
    out.writeframes(updated_frames)
    inp.close()
    out.close()


change_volume('quieter', 1.3)


