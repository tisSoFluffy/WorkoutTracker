import csv
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import argparse

goals = {
    'pushups':100,
    'pullups':50,
    'dips':50 }
keys = {'pushups':'Pu', 'pullups':'P', 'dips':'D'}

workout = pd.read_csv('workoutlog.csv')
workout['DateTime'] = pd.to_datetime(workout['DateTime'])
workout['Weight'] = workout['Weight'].astype('category')
workout['Date'] = workout['DateTime'].dt.date

def main(show_goal=False, yester=True, progress=False):
    
    if progress:
        print('Today\'s Progress:')
        today = workout[workout['Date'] == datetime.now().date()]
        if len(today) == 0:
            print('No activity recorded today, get busy!')
        else:
            stats = today.groupby('Activity')
            print(stats.sum())
            print('-------------------------')
            print('-------------------------')
            print('Progress left')
            for goal,v in goals.items():
                print(f"{goals[goal] - stats.get_group(keys[goal]).sum()['Reps']} {goal} to Go")
    
    if yester:
        print('Yesterday\'s Workout Summary')
        yesterday = workout[workout['Date'] == datetime.now().date() - timedelta(1)]
        stats = yesterday.groupby('Activity')
        print(stats.sum())

    if show_goal:
        print('-------------------------')
        print('-------------------------')
        print("Daily workout routine is:")
        for k,v in goals.items():
            print(f'{k}: {v}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-goal', action='store_true', help='Display my Daily Goal')
    parser.add_argument('-y', action='store_true', help='Display Yesterday\'s workout')
    parser.add_argument('-p', action='store_true', help='Display Today\'s Progress')
    args = parser.parse_args()
    main(show_goal=args.goal, yester=args.y, progress=args.p)