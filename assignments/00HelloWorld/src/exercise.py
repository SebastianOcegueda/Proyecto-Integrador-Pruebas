import pandas as pd

def main():
    #escribe tu código abajo de esta línea
    datasheet=pd.read_csv("DataSheet.csv")
    print(datasheet)


if __name__=='__main__':
    main()
