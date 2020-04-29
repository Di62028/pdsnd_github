import time
import pandas as pd
import numpy as np

import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while (True):
        city = input('Enter the city (Chicago, New York City, Washington): ').lower()
        if (city == 'chicago' or city == 'new york city' or city == 'washington'):
            break
        else:
            print('Invalid input')

    # TO DO: get user input for month (all, january, february, ... , june)
    isfilter_month = input('Filter by month? (y/n): ').lower()
    if isfilter_month == 'y':
        while (True):
            month = input('Enter the month (january, february, ... , june): ').lower()

            months = ['january', 'february', 'march', 'april', 'may', 'june']
            if (month in months):
                break
            else:
                print('Invalid input')
    else:
        month = 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    isfilter_day = input('Filter by day of week? (y/n): ').lower()
    if isfilter_day == 'y':
        while (True):
            day = input('Enter the month (monday, tuesday, ... sunday): ').lower()

            days = dict(enumerate(calendar.day_name))

            if (day.title() in days.values()):
                break
            else:
                print('Invalid input')
    else:
        day = 'all'

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[popular_month - 1]

    print('Most Popular Month: ', popular_month.title())


    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]

    print('Most Popular Day of Week: ', popular_day.title())


    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def result_list(vc):
    return list(vc[vc == max(vc)].index)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    popular_StartStation = df['Start Station'].mode()[0]

    print('Most commonly used Start Station:')

    vc1 = df['Start Station'].value_counts()

    print(result_list(vc1))
    print('')

    # TO DO: display most commonly used end station

    popular_EndStation = df['End Station'].mode()[0]

    print('Most commonly used End Station:')

    vc2 = df['End Station'].value_counts()

    print(result_list(vc2))
    print('')


    # TO DO: display most frequent combination of start station and end station trip

    print('Most frequent combination of start station and end station trip:')
    vc3 = df['Start Station'] + ' --> ' + df['End Station']
    vc3 = vc3.value_counts()
    print(result_list(vc3))
    print('')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: {} minutes'.format(sum(df['Trip Duration'])))

    # TO DO: display mean travel time
    print('Mean travel time: {} minutes and {} seconds'.format(int(df['Trip Duration'].mean()/60), df['Trip Duration'].mean()%60))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User types:')
    print(df['User Type'].value_counts())

    if city != 'washington':
        # TO DO: Display counts of gender
        print('\nCounts of users Gender:')
        print(df['Gender'].value_counts())


        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nEarliest year of birth: {}'.format(int(min(df['Birth Year']))))

        print('\nMost recent year of birth: {}'.format(int(max(df['Birth Year']))))

        print('\nMost common year of birth:')

        common_birth = df['Birth Year'].value_counts()

        print(list(map(int, result_list(common_birth))))
        print('')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Displays 5 lines of raw data."""

    see_raw = input('Do you want to see raw data? (y/n): ').lower()
    if see_raw == 'y':
        i = 0
        while (True):

            print(df.iloc[[i, i+1, i+2, i+3, i+4]])
            i += 5

            see_raw = input('Do you want to see more 5 lines of raw data? (y/n): ').lower()
            if see_raw != 'y':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
