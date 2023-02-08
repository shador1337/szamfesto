import random

generaltszamok=[]

for x in range(24):
    x=random.randrange(1,270)
    x=generaltszamok.append(x)

print('A szedőlapon megjelenő legnerált számok a program sorrendje szerint: ',generaltszamok)

sorrend=[]

for ep1s in range(16):
    sorrend.append(ep1s)
for ep2s in range(91,106):
    sorrend.append(ep2s)
for ep3s in range(181,196):
    sorrend.append(ep3s)
for kp1s in range(16,29):
    sorrend.append(kp1s)
for kp2s in range(106,119):
    sorrend.append(kp2s)
for kp3s in range(196,209):
    sorrend.append(kp3s)
for hp1s in range(29,42):
    sorrend.append(hp1s)
for hp2s in range(119,132):
    sorrend.append(hp2s)
for hp3s in range(209,222):
    sorrend.append(hp3s)
for np1s in range(42,61):
    sorrend.append(np1s)
for np2s in range(132,151):
    sorrend.append(np2s)
for np3s in range(222,241):
    sorrend.append(np3s)
for op1s in range(61,76):
    sorrend.append(op1s)
for op2s in range(151,166):
    sorrend.append(op2s)
for op3s in range(241,256):
    sorrend.append(op3s)
for hap1s in range(76,91):
    sorrend.append(hap1s)
for hap2s in range(166,181):
    sorrend.append(hap2s)
for hap3s in range(256,271):
    sorrend.append(hap3s)

sorrendberakottszamok=sorted(generaltszamok, key=lambda x: sorrend.index(x))

print('A számunkra ideális sorrendberakott számok sorrendje: ',sorrendberakottszamok)
