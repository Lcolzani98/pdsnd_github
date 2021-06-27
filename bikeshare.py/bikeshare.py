import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list = {'january', 'february', 'march', 'april', 'may', 'june', 'all'}
day_list = {'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday','all'}


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
    print('chicago')
    print('new York city')
    print('washington')
    city = input("Please choose a city between the three option: ").lower()


    while city not in ['chicago', 'new york city', 'washington']:
        city = input('City name is invalid! Please input another name: ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please input month name: ').lower()
    while month not in month_list:
        month = input('Month name is invalid! Please input month name in the list january, february, march, april, may, june, all: ')



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please input day of week: ').lower()
    while day not in day_list:
       day = input('Day name is invalid! Please input day name in the list monday, tuesday, wednesday, thursday, friday, saturday, sunday, all: ')


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    df = df[df['month']==month]

    if day != 'all':
        df = df[df['day_of_week']==day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month= df['month'].mode()[0]
    month =['january','february','march','april','may','june']
    popular_month= month[popular_month-1]
    print('The most Popular month is',popular_month)


    # display the most common day of week
    popular_day= df['day_of_week'].mode()[0]
    print('The most Popular day is',popular_day)


    # display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    popular_hour=df['Start Hour'].mode()[0]
    print('The popular Start Hour is {}:00 hrs'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station= df['Start Station'].mode()[0]
    print('The most commonly used Start Station is {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station= df['End Station'].mode()[0]
    print('The most commonly used End Station is {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+' '+'to'+' '+ df['End Station']
    popular_com= df['combination'].mode()[0]
    print('The most frequent combination of Start and End Station is {} '.format(popular_com))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('I love watermellon')
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['duration'] = df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    total_duration=df['Trip Duration'].sum()
    minute,second=divmod(total_duration,60)
    hour,minute=divmod(minute,60)
    print('The total trip duration: {} hour(s) {} minute(s) {} second(s)'.format(hour,minute,second))


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    m,sec=divmod(mean_travel,60)
    if m>60:
        h,m=divmod(m,60)
        print('The mean trip duration: {} hour(s) {} minute(s) {} second(s)'.format(h,m,sec))
    else:
        print('The mean trip duration: {} minute(s) {} second(s)'.format(m,sec))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts= df['User Type'].value_counts()
    print('The user types are:\n',user_counts)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('There is no gender information in this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        oldest = df['Birth Year'].min()
        print('The oldest user is born on the year',oldest)
        youngest = df['Birth Year'].max()
        print('The youngest user is born on the year',youngest)
        common = df['Birth Year'].mode()[0]
        print('Most users are born on the year',common)
    else:
        print("There is no birth year information in this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    question_1 = input('Do you want to see raw data, yes or no?').lower()

    if question_1 == 'yes':
      rows = 0
      while True:
        print(df.iloc[rows: rows + 5])
        rows += 5
        question_2 = input('Would you like to see the next five rows. yes or no?').lower()
        if question_2 != 'yes':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
