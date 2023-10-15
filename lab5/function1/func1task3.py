def solve(numheads,numlegs):
    for chicks in range(numheads+1):
        rab = numheads-chicks 
        l=(chicks*2)+(rab*4)
        if l==numlegs:
            return chicks,rab
         


numheads=int(input())
numlegs=int(input()) 
chicks,rab=solve(numheads,numlegs)
print({chicks} ," ", {rab})