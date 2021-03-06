# -*- coding: utf-8 -*-
import midiate
import devel

mid = midiate.Midiator();
mid.start_process()
indev,outdev = devel.open_both_io(mid);
mid.send(outdev, 'C010')
mid.send(outdev, 'B07A00')
mid.send(outdev, 'B07800')

note_count = 0
def thru(dev, msg, raw):
    global note_count
    st = raw[0]
    if st&0xF0 in {0x90,0x80}:
        if st&0xF0==0x90 and raw[2]>0:
            note_count += 1
        else: note_count -= 1
        if note_count <= 1: mod_level = 0
        elif note_count <= 4: mod_level = (note_count-1) * 32
        else: mod_level = 127        
        ch = raw[0]&0xF    
        mid.send(outdev, msg)
        mid.send(outdev, b'B%X%02X%02X'%(ch,1,mod_level))
        devel.status(f'同時発音数 {note_count}音、\n変調レベル = {mod_level}')
    else: mid.send(outdev, msg)
    print('受信: ', dev, msg)
    
mid.callback(None,'******', thru)
mid.listen(indev);

devel.wait(title='automatic modulator',
           text='自動でモジュレーションを掛けるよ！\n'
           '単音では掛からないよ。\n和音の構成音数が増えるに連れて深く掛かるよ！')

mid.stop_process()
