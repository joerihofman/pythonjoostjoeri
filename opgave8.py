T = int(input('Temperatuur:'))    #temp
B = int(input('Beaufort:'))    #beaufort

G = 13+0.62*T-14*B**0.24+0.47*T*B**0.24
print(G)