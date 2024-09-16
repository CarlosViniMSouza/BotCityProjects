import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from data_analysis import data_analysis
from report_calc import report_calc

def main():
    try:
        data_analysis()
        report_calc()

    except Exception as ex:
        print(f"Error: {ex}")

    finally:
        print("Encerrado!")

if __name__ == '__main__':
    main()
