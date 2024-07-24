import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    men_df = df[df['sex'] == "Male"]
    average_age_men = round(men_df['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    edu_series = df['education']
    edu_bach_series = edu_series[edu_series == 'Bachelors']
    percentage_bachelors = round((edu_bach_series.count() / edu_series.count() * 100), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_series = edu_series[(edu_series == 'Bachelors') | (edu_series == 'Masters') | (edu_series == 'Doctrate')]
    lower_series = edu_series[(edu_series != 'Bachelors') & (edu_series != 'Masters') & (edu_series != 'Doctrate')]
    
    higher_education = round((higher_series.count() / edu_series.count() * 100), 1)
    lower_education = round((lower_series.count() / edu_series.count() * 100), 1)

    # percentage with salary > 50K
    higher_df = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    lower_df = df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]
    
    higher_more_than_50 = higher_df[higher_df['salary'] == '>50K']
    lower_more_than_50 = lower_df[lower_df['salary'] == '>50K']

    higher_education_rich = round((len(higher_more_than_50) / len(higher_df) * 100), 1)
    lower_education_rich = round((len(lower_more_than_50) / len(lower_df) * 100), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers_df = df[df['hours-per-week'] == df['hours-per-week'].min()]

    num_min_workers = num_min_workers_df.count()
    num_min_workers_more_than_50_df = num_min_workers_df[num_min_workers_df['salary'] == '>50K']

    rich_percentage = round((len(num_min_workers_more_than_50_df) / len(num_min_workers_df) * 100), 1)

    # What country has the highest percentage of people that earn >50K?
    workers_earning_more_than_50K = df[df['salary'] == '>50K']

    country_count = df['native-country'].value_counts()
    country_count_more_than_50K = workers_earning_more_than_50K['native-country'].value_counts()

    percentage_earning = round((country_count_more_than_50K / country_count * 100), 1)

    highest_earning_country = percentage_earning.idxmax()
    highest_earning_country_percentage = percentage_earning.max()

    # Identify the most popular occupation for those who earn >50K in India.
    workers_in_india_more_than_50K = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    occupation_count = workers_in_india_more_than_50K['occupation'].value_counts()
    top_IN_occupation = occupation_count.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
