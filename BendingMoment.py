'''Variables:
b - breadth 
h - height
l - length
P - load
E - modulus of elasticity

Funtions:
sigmaMax - 
maxBendMoment -
momOfInertia -
reqVol -
'''
def maxBendMoment(P, l):#M_max = maximum bending moment acting on beam
    mBM = (P * l) / 4
    return mBM

def momOfInertia(b, h): #I = for beam section about the neutral axis
    mOI = (b * h**3) / 12
    return mOI

def bendingStress1(h, maxBendMoment, momOfInertia): #Sigma_max1 = maximum normal bending stress acting on beam
    bendStress1 = maxBendMoment * (h/2) / momOfInertia
    return bendStress1

def bendingStress2(P, l, b,h): #Sigma_max2 = maximum normal bending stress acting on beam
    bendStress2 = (6 * P * l) / (b * h**2)
    return bendStress2

def reqVol1(b, h, l): #V_sigma1 = minimum volume reqired for the sufficient strenght of beam
    vol1 = b * h * l
    return vol1

def reqVol2(P, l, h, sigM2):#V_sigma2 = minimum volume reqired for the sufficient strenght of beam
    vol2 = 3 * P * l**2 / 2 * sigM2 * h
    return vol2

def maxDeflection(P, l, E, mOI):#Delta = deflection of beam that must not exceed a permissible value
    maxDef = (P * l**3) / 48 * E * mOI
    return maxDef

def minVol (P, l, E, h, maxDef): #V_delta = minimum volume required to ensure that deflection of the beam under load does not exceed the specified value
    minVol = P * (l**2 / h)**2 / 4 * E * h * maxDef
    return minVol



while True:
    try:
        choice = int(input('''Welcome, choose an option to calculate for:
            1. Maximum bending moment - M_max (Varibales needed: Load [P], Length [l])
            2. Moment of inertia - I (Variables needed: Breadth [b], Height [h])
            3. Bending stress 1 - Sigma_max1 (Variables needed: Height [h], Maximum bending moment [M_max], Moment of inertia [I])
            4. Bending stress 2 - Sigma_max2 (Variables needed: Load [P], Length [l], Breadth [b], Height [h])
            5. Required volume 1 - V_sigma1 (Variables needed: Length [l], Breadth [b], Height [h])
            6. Required volume 2 - V_sigma2 (Variables needed: Load [P], Length [l], Height [h], Bending stress 2 [Sigma_max2])
            7. Maximum deflection - Delta (Variables needed: Load [P], Length [l], Modulus of elasticity [E], Moment of inertia [I])
            8. Minimum volume - V_delta (Variables needed: Load [P], Length [l], Modulus of elasticity [E], Height [h], Maximum deflection [Delta])
              >>>'''))
        
        if choice in [1, 2, 3, 4, 5, 6 , 7 , 8]:
            if choice == 1:
                P = float(input('Enter the load(N): '))
                l = float(input('Enter the length(m): '))
                print(f'The maximum bending moment is {maxBendMoment(P, l)}')
            elif choice == 2:
                b = float(input('Enter the breadth(m): '))
                h = float(input('Enter the height(m): '))
                print(f'The moment of inertia is {momOfInertia(b, h)}')
            elif choice == 3:
                h = float(input('Enter the height(m): '))
                maxBendMoment = float(input('Enter the maximum bending moment: '))
                momOfInertia = float(input('Enter the moment of inertia: '))
                print(f'The bending stress 1 is {bendingStress1(h, maxBendMoment, momOfInertia)}')
            elif choice == 4:
                P = float(input('Enter the load(N): '))
                l = float(input('Enter the length(m): '))
                b = float(input('Enter the breadth(m): '))
                h = float(input('Enter the height(m): '))
                print(f'The bending stress 2 is {bendingStress2(P, l, b, h)}')
            elif choice == 5:
                l = float(input('Enter the length(m): '))
                b = float(input('Enter the breadth(m): '))
                h = float(input('Enter the height(m): '))
                print(f'The required volume 1 is {reqVol1(b, h, l)}')
            elif choice == 6:
                P = float(input('Enter the load(N): '))
                l = float(input('Enter the length(m): '))
                h = float(input('Enter the height(m): '))
                sigM2 = float(input('Enter the bending stress 2: '))
                print(f'The required volume 2 is {reqVol2(P, l, h, sigM2)}')
            elif choice == 7:
                P = float(input('Enter the load(N): '))
                l = float(input('Enter the length(m): '))
                E = float(input('Enter the modulus of elasticity: '))
                mOI = float(input('Enter the moment of inertia: '))
                print(f'The maximum deflection is {maxDeflection(P, l, E, mOI)}')
            elif choice == 8:
                P = float(input('Enter the load(N): '))
                l = float(input('Enter the length(m): '))
                E = float(input('Enter the modulus of elasticity: '))
                h = float(input('Enter the height(m): '))
                maxDef = float(input('Enter the maximum deflection: '))
                print(f'The minimum volume is {minVol(P, l, E, h, maxDef)}')


            #break
        else:
            print('Please enter a number between 1 to 8.')
    except ValueError:
        print('Please enter a valid number.')
        