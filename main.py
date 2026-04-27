def currency_converter():
    print("--- Algeria to Europe Money Converter ---")
    
    exchange_rate = 150 
    
    dzd_amount = float(input("Enter amount in DZD (Algerian Dinar): "))
    
    eur_amount = dzd_amount / exchange_rate
    
    print(f"\nYour {dzd_amount} DZD is approximately: {eur_amount:.2f} EUR")
    
    if eur_amount < 10:
        print("Tip: This is a small daily expense in Europe.")
    else:
        print("Tip: This amount covers a good meal or a train ticket in Europe.")

currency_converter()
