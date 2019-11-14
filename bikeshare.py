import time

import pandas as pd

import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',

'new york city': 'new_york_city.csv',

'washington': 'washington.csv' }

def get_filters():



    city = ('chicago', 'new_york_city', 'washington')

    month = ('all', 'january', 'febuary', 'march', 'april', 'may', 'june')

    day = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

    print('Hello! Let\'s explore some US bikeshare data!')

# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    print('Which city would you like to explore: chicago, new_york_city, or washington')

    while True:

        try:

         city in CITY_DATA

         city = input('Enter name of a city: ').lower()

         print('Great! we are checking data for', city)
         break
        
        except KeyError:

         print('Sorry, Invalid City entered, new york city and washington')
         True

# get user input for month (all, january, february, ... , june)

print('\nWhich month would you like to explore')

month = input('Enter month of the year: ').lower()

while True:

    print('\nGreat! we are checking data for', month)

    break

else:

    print('Sorry, please enter all or months; january to june')

quit()

# get user input for day of week (all, monday, tuesday, ... sunday)

print('\nWhich day of the week would you like to explore')

day = input('\nEnter day of the week: ').lower()

print('-'*40)

return city, month, day

def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':

        months = ['january', 'febuary', 'march', 'april', 'may', 'june']

        month = months.index(month) + 1

    if day != 'all':

        df = df[df['day_of_week'] == day.title()]

return df

def time_stats(df):


    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()

# display the most common month

    common_month = df['month'].mode()[0]

    print('Most common month: ', common_month)

# display the most common day of week

    common_day = df['day_of_week'].mode()[0]

    print('Most common day of week: ', common_day)

# display the most common start hour

    common_start_hour = df['hour'].mode()[0]

    print('Most common start hour: ', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def station_stats(df):


    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()

# display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]

    print('Most Commonly used start station: ', common_start_station)

# display most commonly used end station

    common_end_station = df['End Station'].mode()[0]

    print('Most commonly used end station: ', common_end_station)

# display most frequent combination of start station and end station trip

    df['comb'] = df['Start Station'] + ' to ' + df['End Station']

    common_combo = df['comb'].mode()[0]

    print('Most frequent combination of start and end station: ', common_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')

    start_time = time.time()

# display total travel time

    trip_duration = df['Trip Duration'].sum()

    print('Total trip duration: ', trip_duration)

# display mean travel time

    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    start_time = time.time()

# Display counts of user types

    user_types = df['User Type'].value_counts()

    print('Counts of User Type: ', user_types)

# Display counts of gender

    if 'Gender' in df:

        gender_count = df['Gender'].value_counts()

        print('Total Gender count: ', gender_count)

    else:

        print('Gender information is not available for this city')

# Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df:

        recent_birth_year = df['Birth Year'].max()

        print('Most recent birth year: ', recent_birth_year)

    else:

        print('Birth year information is not available for this city')

    if 'Birth Year' in df:

        common_birth_year = df['Birth Year'].mode()[0]

        print('Most common birth year: ', common_birth_year)

    else:

        print('Birth year information is not availabe for this city')

        print("\nThis took %s seconds." % (time.time() - start_time))

        print('-'*40)

#displaying answer if user want to view first five rows of data or not

    while True:

        answer = input('\nWould you like to view data? Enter yes or no\n').lower         ()

        if answer == 'yes':

            print('First five raw data\n', df.head())

            break

        elif answer == 'no':

            break

        else:

            True

def main():

    while True:

        city, month, day = get_filters()

        answer_ = load_data(city, month, day)

        time_stats(answer_)

        station_stats(answer_)

        trip_duration_stats(answer_)

        user_stats(answer_)

        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() != 'yes':

            break

if __name__ == "__main__":
    main()