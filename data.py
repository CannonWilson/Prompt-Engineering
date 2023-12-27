# Note: all figures in millions. All figures are estimates.

# Source: https://www.statista.com/statistics/241488/population-of-the-us-by-sex-and-age/
# Maps age range as a string to US pop
AGE_DICT_US = {
    '0-4': 18.82,
    '5-9': 20.3,
    '10-14': 21.45,
    '15-19': 21.56,
    '20-24': 21.52,
    '25-29': 22.39,
    '30-34': 23.1,
    '35-39': 22.3,
    '40-44': 21.1,
    '45-49': 19.79,
    '50-54': 20.91,
    '55-59': 21.57,
    '60-64': 21.23,
    '65-69': 18.4,
    '70-74': 15.27,
    '75-79': 9.9,
    '80-84': 6.31,
    '85-90': 5.98,
}

# Source: https://ourworldindata.org/grapher/population-by-broad-age-group
# Maps age range as a string to global pop
AGE_DICT_GLOBAL = {
    '0-4': 671.48,
    '5-14': 1340,
    '15-24': 1220,
    '25-64': 3910,
    '65-90': 761.27
}

# Comparing two histograms, may need to normalize
# Chi-squared distance
# KL-divergence

AGE_DICT_UNIFORM = {
    '0-4': 1,
    '5-9': 1,
    '10-14': 1,
    '15-19': 1,
    '20-24': 1,
    '25-29': 1,
    '30-34': 1,
    '35-39': 1,
    '40-44': 1,
    '45-49': 1,
    '50-54': 1,
    '55-59': 1,
    '60-64': 1,
    '65-69': 1,
    '70-74': 1,
    '75-79': 1,
    '80-84': 1,
    '85-90': 1,
}

# Source: https://www.statista.com/statistics/241495/us-population-by-sex/
# Maps sex as a string to US pop
SEX_DICT_US = {
    'male': 164.38,
    'female': 167.51
}

# Source: https://statisticstimes.com/demographics/world-sex-ratio.php
# Data from: https://population.un.org/wpp/Download/Standard/Population/
# Maps sex as a string to global pop
SEX_DICT_GLOBAL = {
    'male': 3970,
    'female': 3905  
}

SEX_DICT_UNIFORM = {
    'male': 1,
    'female': 1
}

# Source: https://www.npr.org/2021/08/13/1014710483/2020-census-data-us-race-ethnicity-diversity
# Maps race as a string to US pop
RACE_DICT_US = {
    'white': 191.698,
    'hispanic': 62.08,
    'black': 39.94,
    'asian': 19.619,
    'multiracial': 13.549,
    'american indian': 2.252,
    'pacific islander': 0.622
}

# Source: https://infogram.com/race-of-the-world-population-1go502yg18k62jd
# Maps race as a string to global pop
RACE_DICT_GLOBAL = {
    'white': 1.2,
    'black': 1,
    'asian': 2.1,
    'indian/middle eastern': 1.657,
    'native american': 0.25,
    'hispanic': 0.7
}

RACE_DICT_UNIFORM = {
    'white': 1,
    'black': 1,
    'asian': 1,
    'indian/middle eastern': 1,
    'native american': 1
}