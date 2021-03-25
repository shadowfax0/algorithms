# algorithms
Selected Algorithms

1. business_day.py
    - Recursive function that returns the last business day based off of the current date. 
    - We define a business day as M-F and not a holiday. 
    - Explained:
        if today is Monday, 4 January 2021
        the functon will get the prior day and check if it falls on a weekend or is a holiday
        the 2nd and 3rd of Jan fell on the weekend in 2021, so these days are ignored
        function arrives on Friday, 1 Jan. This is not the weekend but is a holiday, so this day is also ignored
        Thursday, 31 Dec 2020 is returned as the last business day 
        
