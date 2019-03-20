# Charecter Frequency in String

def freq(str):
    unique_Char = set(str)
    for i in unique_Char:
        print(i,": ", str.count(i))
        
if __name__ == "__main__":
    str = "abcdacd"
    freq(str)

    