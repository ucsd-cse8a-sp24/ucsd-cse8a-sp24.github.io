from CSE8ACSV import *

tech_diversity_data = get_diversity_data("tech_diversity.csv")


def get_avg_pcnt_category_overall(category):
    total = 0
    for company in tech_diversity_data:
        total += tech_diversity_data[company][category]
    return total / len(tech_diversity_data)
