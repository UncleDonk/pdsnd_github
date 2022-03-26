import time
import pandas as pd
import numpy as np

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

    while True:

            city = input('Please enter a city: Chicago, New York city, Washington: ')
            city = city.lower()

            if city == 'chicago' or city =='new york city' or city == 'washington':

                  break

    # TO DO: get user input for month (all, january, february, ... , june)

    month = input('Please select a month: January, February, March, April, May, June or All: ')
    month = month.title()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input('Please select a day of the week: Monday to Sunday or All: ')
    day = day.title()


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
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)



    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != "All" and day != "All":
        df = df[df['month']==month]
        df = df[df['day_of_week']==day]
    elif month == "All" and day != "All":
        df = df[df['day_of_week']==day]
    elif month != "All" and day == "All":
        df = df[df['month']==month]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]
    print('The most popular month is: ', common_month)

    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('The most popular day of the week is: ', common_day)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular end station is: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total duration in seconds: ', int(total_travel_time))

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Average duration in seconds: ', int(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print(df['User Type'].value_counts().to_frame())


    # TO DO: Display counts of gender

    if "Gender" in df.columns:

        print(df['Gender'].value_counts().to_frame())

    else:

        print("Gender information is not available")

    # TO DO: Display earliest, most recent, and most common year of birth

    if "Birth Year" in df.columns:

        earliest_year = df['Birth Year'].min()
        print("The earliest year of birth is: ", int(earliest_year))

        recent_year = df['Birth Year'].max()
        print("The most recent year of birth is: ", int(recent_year))

        common_year = df['Birth Year'].mode()[0]
        print("The most common birth year is: ", int(common_year))

    else:

        print("Birth year information is unavailable")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):

    raw = input('Would you like to see the next 5 lines of raw data? Yes or No\n')
    raw = raw.lower()

    i=0

    while True:
        if raw == 'no':
            break
        print(df.iloc[i:i + 5])
        i = i + 5
        raw = input('Would you like to see the next 5 lines of raw data? Yes or No\n')
        raw = raw.lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
