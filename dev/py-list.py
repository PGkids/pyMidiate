# -*- coding: utf-8 -*-

#from midiate import Midiate
import midiate

midiate = midiate.Midiate()
midiate.start_process()

inputs = midiate.enum_input()
outputs = midiate.enum_output()

print('MIDI入力:')
for name in inputs: print(name)
print('\n')
print('MIDI出力:')
for name in outputs: print(name)

midiate.stop_process()