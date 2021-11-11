import os, sys, csv
import argparse
import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('% (asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
activities = {'bc': 'Bicep Curl',
    'h': 'heavybag',
    'm': 'muscleup',
    'p': 'pullup',
    'pu': 'pushup',
    'd': 'dip',
    'pl': 'plank',
    's': 'squat'}

def logActivity(activity, reps, weight=0, duration=0):
    #logger.info('logging workout')
    with open('workoutlog.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([activity.capitalize(),weight,reps,duration,datetime.now()])
    #logger.info('workout saved.')
    print(f'{reps} {activities[activity]}s logged')

if __name__ == '__main__':
    def valid_time(d):
        try:
            return datetime.strptime(d, "%M:%S")
        except ValueError:
            raise argparse.ArgumentTypeError('Not a valid Date')

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=str, help='Activity (Bc)icep Curl, (D)ips, (H)eavyBag, (M)uscleups, (Pl)anks, (P)ullups, (Pu)shups, (S)quats' )
    parser.add_argument('-w', type=int, help='Weight')
    parser.add_argument('-r', type=int, help='Number of Reps')
    parser.add_argument('-d', type=valid_time, help='Duration of Activity - format MM:SS')
    args = parser.parse_args()
    logActivity(args.a, args.r, args.w, args.d)
