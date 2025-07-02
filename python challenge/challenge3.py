name              = input('Enter Your Name:')
salarie_heure     = float(input('Enter hourly wage:'))
number_hour       = float(input('Enter Your Number Hours Worked:'))
try:
    if number_hour > 40:
        hrSup      = number_hour - 40
        additional_salaire = hrSup * 1.5  
        total_salaire   = salarie_heure *(40 + additional_salaire) 
        print('Additional work')
        print("Total", str(total_salaire))
    else:
        total = number_hour * salarie
        print('Regular salary')
        print( "Total", str(total))

except Exception as e:
    print(e)
