print("Welcome! Please type the correlating number: \n 1 Current Ratio \n 2 PE Ratio \n 3 M/B Ratio")

x = int(input())

if x == 1:
    print("Current ratio determines liquidity of an account. \n Total Assets:")
    a = float(input())
    print("Total Liabilities:") 
    l = float(input())
    cr = a/l

    print("Current Ratio:", cr, "alternatively:", cr*100, "%")
    if cr >= 1.0:
         print("Can cover short term liabilities")
    else: print("Short term liabilites cannot be fully covered")
    
else: 
        if x== 2: 
            print("PE Ratio is a value indicator of a business. \n Share Price:")
            a = float(input())
            print("Earnings Per Share:") 
            l = float(input())
            cr = a/l
            print("Current Ratio:", cr)
            if cr >= 25:
                print("Possibly overvalued stock.")
            else: 
                if cr <= 20: 
                       print("Possibly undervalued stock.")
                else: 
                       print("Possibly accurate value")
        else: 
            if x == 3:
                print("Market to Book Ratio is a value indicator of a business. \n Market Capitalization:")
                a = float(input())
                print("Book Value:") 
                l = float(input())
                cr = a/l
                print("Market to Book Ratio:", cr)
                if cr >= 1:
                    print("Possibly overvalued stock.")
                else: 
                    if cr <= 1: 
                       print("Possibly undervalued stock.")
                    else: 
                       print("Possibly accurate value")
input("Press Enter to Exit.")