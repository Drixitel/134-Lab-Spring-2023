# all functions used in Oil Drop 
import numpy as np
import pandas as pd

# Constants 

b   = 8.20E-3         # Viscostiy Correction Factor (given)
g   = 9.80            # Gravity (given)
p   = 1.013E5         # Atmospheric Pressure (at room temp? - given in docs)
n_o = 1.824E-5        # Tabulated Viscosity/ Viscocity of air (given)
rho1 = 8.86E2         # Density of oil droplet (given)
rho2 = 0              # To be determined for accuracy   

#Stored List 
Constants = [b, g, p, n_o,rho1 ,rho2]

# Separation of plates (d) 
d   = 7.752E-3      # meters



# Plate Separation 
sigd = 0.0127E-3    # meters
sigx = 0.01E-3      # meters
sigt = 0.1          # fractional seconds




# Functions: 



def radius(v_y0):     
    # Function: Takes (positive) velocity returns radius
    # Components of a 
    # terminal velocity with E = 0 
    
    # convert mm to m 
    v_y0 = v_y0
    
    # alpha 
    alpha = b/(2*p)

    #beta
    beta = (9*v_y0*n_o)/(2*rho1*g)
    
    #radius a 
    a = np.sqrt((alpha**2)+beta) - alpha
   
    return a



def q1(a,v_y0,v_yE,V):
    # Funtion: Takes radius,Velocity E=0 and Velocity E != 0 
    #   Returns charge 
    #velocity: v_y0 E=0 
    #velocity: v_yE E != 0

    # convert mm to m 
    v_y0 = (v_y0)
    v_yE = -(v_yE) 


    #left term (lt) 
    lt = (4/3)*np.pi*rho1*g*(d/V)*(a**3)

    #right term (rt)
    rt = (v_yE - v_y0)/ v_y0

    q1 = lt*rt
    
    return q1


# effective viscosity 

def neff(a): 
    n_effa = n_o/(1 + (b/(p*a)))

    return n_effa




def Droplet_Values(n_drop, n_ionized, csv_name_as_string):
    # Funtion: Choose Droplet, Choose ionization, Call "file.csv"
    # Return a list of paramerters per droplet selected 
    # E.g.: droplet1_ionization2 = [velocities, Voltage]


    # Call the CSV file
    droplet = pd.read_csv(csv_name_as_string)

    # Select the specified droplet by droplet # and Ionization (rows)
    d1 = droplet[droplet['Droplet'].isin([n_drop]) & droplet['Ionized'].isin([n_ionized])]

    # Select the specified parameters (Velocities and Volts) (columns)
    d1 = d1[["Vf1","Vr1","Vf2","Vr2","Vf3","Vr3","vf av","vr av","Volts V","varVf1", "varVr1","varVf2","varVr2","varVf3","varVr3"]]

    # Convert to array, already is a float
    d1 = d1.to_numpy()

    # Assign a list 
    d1_values = []

    # use a for loop to unpack the 0th element into our desired list

    for value in d1[0]:
        d1_values.append(value)

    return d1_values




def CreateDropsDatabase(csv_file_name_as_string): # "filename.csv"
    # Function: Takes "file.csv" Returns list of lists for our drops
    # dependent on the function Droplet_Values()
    # E.g.: Drops = [d1[velocities,Voltage],...dn[velocities,Voltage]]

    # define list
    drops = []

    # define counter, starts at 1 (our table has droplets starting at 1)
    droplet_number = 1 

    # define while loop such it breaks if we define droplet_number = None
    while droplet_number is not None: 
        # set ionization counter to 0 (our table has ionizations starting at 0)

        ionization_number = 0

        # define a while loop -same condition
        while ionization_number is not None: 
            # preform: "handling an exception(error)" aka running code to check for error  
            # we know we will get an index error meaning we are at the end of our spreadsheet or ionizations
            # The Try-Except block
            #       will try to pull a drops paramaters if it works we incriment through the ionizations 
            #       skipping the except block. 
            #       if an Index error occurs it will check if it broke due to ionization value or droplet value

            try:
                d = Droplet_Values(droplet_number, ionization_number, csv_file_name_as_string)
                # prints used to check if something breaks
                # print(f"{droplet_number}, {ionization_number}")
                # print(d)

                # add to list 
                drops.append(d)
                # check next ionization add 1
                ionization_number += 1
            except IndexError:
                # prints to see breaks
                # print(f"{droplet_number}, {ionization_number}")

                # Check if droplet_number or ionization_number gave error
                # important: this means drops.append and the incriment on ionization did not occur
                if ionization_number == 0: 
                    # if false (ionizations broke) this means all ionizations for this droplet were found
                    #   continue to else 
                    # if true (droplet broke) this means we have no more droplets
                    #   since ionization is still set to 0 this condition is True, Call None and break
                    #   Note: Calling droplet_number =None will break whole loop and return list of lists 
                    droplet_number = None
                    break
                else:
                    # break this check-block by calling None and continue to next droplet
                    ionization_number = None
        
        # occurs after ionization = None (else block)
        if droplet_number is not None:
            droplet_number += 1
    return drops 




def Radii_Charge_NotAveragedVel(drops_list_of_lists): 
    # droplet = to loop through
    # drops a list of lists previously created

    # function takes list to loop through
    # returns two lists one for radius and one for charge 
    list_of_radius_values = []
    list_of_charge_values =[]


    for droplet in drops_list_of_lists: 
        # n = index value of 1droplets parameters
        # n = 0  
        # print(droplet)
        for i in range(3): 
            idx = i * 2

            # if n > 4: 
            #     break
            # else: 
            if droplet[idx] ==0 or droplet[idx+1] ==0: 
                list_of_radius_values.append(0)
                list_of_charge_values.append(0)
                print("no value vf.vr")
                continue
            else:
                # print(n)
                # print('new drop vf.vr')
                # print(droplet[n])
                # print(droplet[n+1])

                ri = radius(droplet[idx])
                list_of_radius_values.append(ri)

                #calculate charge 
                qi = q1(ri,droplet[idx],droplet[idx+1],droplet[8])
                list_of_charge_values.append(qi)
                # n += 2
    return list_of_radius_values, list_of_charge_values


def Radii_Charge_VelAVERAGED(drops_list_of_lists):
    #   Pulls the velocity that is already averaged 
    #   Returns two lists 
    list_of_radius_values_velAV = []
    list_of_charge_values_velAV =[]

    for droplet in drops_list_of_lists: 
    #Droplet should have 8 indecies we want index 6 & 7
    #index 6 = vel E=0
    #index 7 = vel E!=0

        #Cal Radius and save
        ri_velav = radius(droplet[6])
        list_of_radius_values_velAV.append(ri_velav)

        #Cal Charge and save 
        qi_velav = q1(ri_velav, droplet[6], droplet[7], droplet[8])
        list_of_charge_values_velAV.append(qi_velav)
    return list_of_radius_values_velAV, list_of_charge_values_velAV
            