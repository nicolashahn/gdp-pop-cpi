import csv
import matplotlib.pyplot as plt


def get_dict_from_csv(filename):
    csvd = {}
    with open(filename) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=",")
        for row in csvreader:
            year = row["Date"]
            val = row["Value"]
            csvd[int(year)] = float(val)
    return csvd


def main():
    # 1947-2020
    gdpd = get_dict_from_csv("GDP.csv")
    # 1913-2020
    cpid = get_dict_from_csv("CPI.csv")
    # 1900-2020
    popd = get_dict_from_csv("population.csv")

    pcpd = {}
    for year, gdp in sorted(gdpd.items()):
        if year - 1 in gdpd:
            cpi = cpid[year]
            pop = popd[year]

            prev_gdp = gdpd[year - 1]
            prev_cpi = cpid[year - 1]
            prev_pop = popd[year - 1]

            per_capita_productivity = (gdp / pop) / cpi
            pcpd[year] = per_capita_productivity
            prev_per_capita_productivity = (prev_gdp / prev_pop) / prev_cpi
            per_capita_productivity_growth = (
                (per_capita_productivity / prev_per_capita_productivity) - 1.0
            )

            gdp_growth_rate = gdp / prev_gdp - 1.0
            pop_growth_rate = pop / prev_pop - 1.0
            gdp_pop_growth_diff = gdp_growth_rate - pop_growth_rate
            print(year, gdp_pop_growth_diff)

    pcp_yrs = list(sorted(pcpd.keys()))
    pcp_vals = [pcpd[k] for k in pcp_yrs]
    plt.plot(pcp_yrs, pcp_vals)
    plt.ylabel('GDP / Population / CPI')
    plt.show()

if __name__ == "__main__":
    main()
