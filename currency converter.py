#simple program to convert usd into pkr
def converter(usd_val):
    pkr_val = usd_val * 280     #280 is the price of the dollar on this day
    print(pkr_val)
    return pkr_val
converter(100)
