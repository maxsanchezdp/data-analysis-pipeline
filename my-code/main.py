from get import get_data
import clean
from filter_fix import filter_fixer
from analyse import analyse_this
from api_enrich import enrich_that
from pdf import make_PDF

import argparse
import warnings
warnings.filterwarnings("ignore")


def main(country,yeari,yearf):
    data=get_data()
    cldata=clean.clean_data(data)
    filfix=filter_fixer(cldata,country,yeari,yearf)
    pop_plot_r,gr_plot_r=analyse_this(filfix)
    nomb, altnomb, capi, regi, langu, cpopul=enrich_that(filfix)
    rpdf=make_PDF(nomb, altnomb, capi, regi, langu, cpopul,pop_plot_r,gr_plot_r)
    return rpdf


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Input a country name and period (two years) to obtain a pdf report with basic info, population and growth rate.')
    parser.add_argument('--fcountry', dest='fcountry', default="spain", type=str, help='Country')
    parser.add_argument('--year0', dest='year0', default=2006, type=int, help='Initial year for report')
    parser.add_argument('--year1', dest='year1', default=2016, type=int, help='End year for report')
    args = parser.parse_args()
    
    if args.fcountry.upper() not in clean.COUNTRIES: print("Not a valid country")    
    elif (args.year0 < 1960) or (args.year1 > 2016): print("No data available for selected years")
    elif args.year0 >= args.year1: print("Year0 must be prior to Year1")
    else: 
        print(f"Generating report for {args.fcountry} from {args.year0} to {args.year1}")
        rutapdf=main(args.fcountry,args.year0,args.year1)
        print(f"Done! You may find your report on the following path: {rutapdf}")

    #print(args.fcountry, args.year0,args.year1) 
    #main()