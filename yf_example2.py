""" yf_example2.py

Example of a function to download stock prices from Yahoo Finance.
"""

import yfinance as yf

def yf_prc_to_csv(tic, pth, start = None, end = None):

    """ Downloads stock prices from Yahoo Finance and saves the
    information in a CSV file

    Parameters
    ----------
    tic : str
        Ticker

    pth : str
        Location of the output CSV file

    start: str, optional
        Download start date string (YYYY-MM-DD)
        If None (the default), start is set to '1900-01-01'

    end: str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
    """

    df = yf.download(tic, start=start, end=end)
    df.to_csv(pth)
print('yf_example2 bottom line')

#print('here is yf_example2')

#tic = 'QAN.AX'
#pth = 'qan_stk_prc.csv'
#yf_prc_to_csv(tic, pth)


#__name__
#print(f"current module __name__: {__name__}")

#import yf_example1
#print(f"imported module __name__:{yf_example1.__name__}")

#Example
if __name__ == "__main__":
    tic = 'QAN.AX'
    pth = 'qan_stk_prc.csv'
    yf_prc_to_csv(tic, pth)
    print('yf_example2 inside if statement')

#original path
#pth= C:\Users\home\toolkit\toolkit\Data

pth = 'C:\\Users\\home\\toolkit\\toolkit\\Data\\test.csv'
print(pth)
pth = r'C:\Users\home\toolkit\toolkit\Data\test.csv'
print(pth)

if __name__ == "__main__":
    tic = 'QAN.AX'
    datadir = r'C:\Users\home\toolkit\toolkit\Data'
    pth = f'{datadir}\\test.csv'
    yf_prc_to_csv(tic, pth)

#portable

if __name__ == "__main__":
    import os
    tic = 'QAN.AX'
    datadir = r'C:\Users\home\toolkit\toolkit\Data'
    pth = os.path.join(datadir, 'qan_stk_prc.csv')
    yf_prc_to_csv(tic, pth)
    print(pth)

#config
if __name__ == "__main__":
    import os
    import toolkit_config as cf
    tic = 'QAN.AX'
    pth = os.path.join(cf.DATADIR, 'test2.csv')
    yf_prc_to_csv(tic, pth)
    print(pth)