BUSINESS CASE PART


TASK 1

1. Load and merge all files Table_* using pandas package DONE
2. Drop duplicates if any appear in data DONE
3. Show (for example print) number of null values in each column DONE
4. Fill numerical null values with 1337 DONE
5. For each row calculate difference (number of days) between Acctg Date and Date columns DONE
6. For each row calculate difference (number of BUSINESS days) between Acctg Date and Date columns (ignore weekends and UK bank holidays) DONE
7. Convert Amount to PLN using FXrates.csv DONE
8. Create folder results and save separate file for EACH unique Type value, use Type in name of saved file (for example Table_4P4.xlsx) DONE

TASK 2

1. Load file interval_data.xlsx using pandas package DONE
2. Transpose table so that it has columns such as MPAN, Date, Hour (values found in Header row from 00:00 to 23:30), Value (for example 7.18, 7.47 and so on). DONE 
3. Calculate mean, max, min value for each MPAN for each week DONE
4. Save result to separate file for each MPAN number DONE



GENERAL PROGRAMMING PART


TASK 1 DONE

Write Morse code decoder. https://en.wikipedia.org/wiki/Morse_code
decoder('.- -   -.. .- .-- -.   .-.. --- --- -.-   - ---   - .... .   . .- ... -')
Should return "AT DAWN LOOK TO THE EAST". Letters are separated by one whitespace, words by three whitespaces.

TASK 2 DONE

Write a programm which encodes a sentence: for each word which length exceeds 3 letters return that word in backward order. 
For example:

AT DAWN LOOK TO THE EAST  - input

AT NWAD KOOL TO THE TSAE  - result
