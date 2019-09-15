"""
    practise for pandas
"""
import pandas as pd
from pandas import Series

PATH = '../data/athlete_events.csv'


class Assignment1:
    """
    The dataset has the following features:
        ID - Unique number for each athlete
        Name - Athlete's name
        Sex - M or F
        Age - Integer
        Height - In centimeters
        Weight - In kilograms
        Team - Team name
        NOC - National Olympic Committee 3-letter code
        Games - Year and season
        Year - Integer
        Season - Summer or Winter
        City - Host city
        Sport - Sport
        Event - Event
        Medal - Gold, Silver, Bronze, or NA

    """

    def __init__(self):
        self.data = pd.read_csv(PATH)

    def question_one(self):
        """
        How old were the youngest male and female participants of the 1992 Olympics?
        """
        year_filter_condition = self.data['Year'] == 1992
        male_filter_condition = self.data['Sex'] == 'M'
        female_filter_condition = self.data['Sex'] == 'F'

        youngest_male = self.data.where(year_filter_condition & male_filter_condition)['Age'].min()
        youngest_female = self.data.where(year_filter_condition & female_filter_condition)['Age'].min()

        print('Question 1 Answer')
        print('Youngest male ', youngest_male)
        print('Youngest female ', youngest_female)

        # Answer = 11 and 12

    def question_two(self):
        """
        2. What was the percentage of male basketball players among all the male participants of the 2012 Olympics?
        Round the answer to the first decimal.

        Hint: here and further if needed drop duplicated sportsmen to count only unique ones.
        """

        # print(self.data['Sport'].head())

        year_filter_condition = self.data['Year'] == 2012
        male_filter_condition = self.data['Sex'] == 'M'
        game_filter_condition = self.data['Sport'] == 'Basketball'

        total_male_players = self.data.where(year_filter_condition
                                             & male_filter_condition)['ID'].drop_duplicates()

        total_male_basketball = self.data.where(year_filter_condition
                                                & male_filter_condition
                                                & game_filter_condition)['ID'].drop_duplicates()

        percentage = round(len(total_male_basketball) / len(total_male_players) * 100, 1)

        print('Question 2 Answer')
        print('Total male basketball players', len(total_male_basketball))
        print('Total male players', len(total_male_players))

        print('Percentage', percentage)

        # Answer = 2.5

    def question_three(self):
        """
        3. What are the mean and standard deviation of height for female tennis players who participated in the 2000
        Olympics? Round the answer to the first decimal.
        """

        female_filter_condition = self.data['Sex'] == 'F'
        year_filter_condition = self.data['Year'] == 2000
        sport_filter_condition = self.data['Sport'] == 'Tennis'

        tennis_data: Series = self.data.where(female_filter_condition
                                              & year_filter_condition
                                              & sport_filter_condition) \
            .dropna(subset=['Height']) \
            .drop_duplicates(subset='ID', keep='first')['Height']

        mean = round(tennis_data.mean(), 1)
        std_dev = round(tennis_data.std(), 1)

        print('Question 3 Answer')
        print('Mean', mean)
        print('Standard Deviation', std_dev)

        # Answer 171.8 and 6.5

    def question_four(self):
        """
        4. Find a sportsman who participated in the 2006 Olympics, with the highest weight among other participants of
        the same Olympics. What sport did he or she do?
        """

        year_filter_condition = self.data['Year'] == 2006

        sorted_data: Series = self.data \
            .where(year_filter_condition) \
            .sort_values(by=['Weight'], ascending=False)

        print('Question 4 Answer')
        print('Sport is ', sorted_data['Sport'].values[0])

        # Skeleton

    def question_five(self):
        """
            5. How many times did John Aalberg participate in the Olympics held in different years?
        """

        name_filter_condition = self.data['Name'] == 'John Aalberg'

        john_data = self.data.where(name_filter_condition).drop_duplicates(subset='Year').dropna(subset=['Name'])

        freq = len(john_data)

        print('Question 5 Answer')
        print('Number of times John Aalberg participated ', freq)

    def question_six(self):
        """
        6. How many gold medals in tennis did sportspeople from the Switzerland team win at the 2008 Olympics?
        Count every medal from every sportsperson.
        """

        country_filter_condition = self.data['Team'] == 'Switzerland'
        medal_filter_condition = self.data['Medal'] == 'Gold'
        sport_filter_condition = self.data['Sport'] == 'Tennis'
        year_filter_condition = self.data['Year'] == 2008

        switzerland_gold_data = self.data.where(country_filter_condition
                                                & medal_filter_condition
                                                & year_filter_condition
                                                & sport_filter_condition
                                                ).dropna(subset=['Medal'])

        print('Question 6 Answer')
        print('Number of gold medals in tennis from switzerland in 2008 ', len(switzerland_gold_data))

        # Answer = 2

    def question_seven(self):
        """
         Is it true that Spain won fewer medals than Italy at the 2016 Olympics? Do not consider NaN values in Medal
         column.
        """

        spain_filter_condition = self.data['Team'] == 'Spain'
        italy_filter_condition = self.data['Team'] == 'Italy'

        year_filter_condition = self.data['Year'] == 2016

        spain_medals_data = self.data.where(spain_filter_condition & year_filter_condition).dropna(subset=['Medal'])
        italy_medals_data = self.data.where(italy_filter_condition & year_filter_condition).dropna(subset=['Medal'])

        spain_medals = len(spain_medals_data)
        italy_medals = len(italy_medals_data)

        print('Spain : ', spain_medals)
        print('Italy : ', italy_medals)

        if spain_medals > italy_medals:
            print('Yes')
        else:
            print('No')

        # Answer : No


if __name__ == '__main__':
    assignment = Assignment1()
    assignment.question_seven()
