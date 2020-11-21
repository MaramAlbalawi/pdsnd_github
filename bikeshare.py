import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#Filtering
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! My name is Maram. Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input ("\nWrite the name of the city that you want to know about from chicago, new york city, or washington to read about: ").lower()

    while city.lower() not in [ 'chicago', 'new york city', 'washington']:
         city = input( "There is an error in your choice, would you select another city? ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("\nWrite the name of the month from january, february, march, april, may, june, or all : ").lower()

    while month.lower() not in [ 'january', 'february', 'march', 'april', 'may', 'june', 'all']:
         month = input( "There is an error in your choice, would you select another month? ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nWrite the name of the day from monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all : ").lower()

    while day.lower() not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
         day = input("There is an error in your choice, would you select another day? ").lower()

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
    # to read and manipulate columns

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    #filtering by month and day

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Based in our data the most common month is: {}'.format(common_month))

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    common_day = df['day_of_week'].mode()[0]
    print('Based in our data the most common day is: {}'.format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('Based in our data the most common start hour is: {}'.format(common_start_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df['Start Station'].mode()[0]
    print("Based in our data the most commonly used start station is: {}".format(commonly_start_station))

    # TO DO: display most commonly used end station
    commonly_end_station = df['End Station'].mode()[0]
    print('Based in our data the most commonly used end station is: {}'.format(commonly_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    combination_start_end = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print('Based in our data the most frequent combination of start and end station are: {}'.format(combination_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

   #Displaying data
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of user types: {}'.format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_of_gender = df['Gender'].value_counts()
        print('The counts of gender: {}'.format(counts_of_gender))

    # TO DO: Display earliest, most recent, and most common year of birth

    #The earliest year of birth
    earliest_year_birth = df['Birth Year'].min()
    print('The earliest year of birth is {}'.format(earliest_year_birth))

    #The most recent year of birth
    most_year_birth = df['Birth Year'].max()
    print('The most recent year of birth is {}'.format(most_year_birth))

    #The most common year of birth
    most_common_year_birth = df['Birth Year'].mode()[0]
    print('The most common year of birth is {}'.format(most_common_year_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
