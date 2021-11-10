import os, sys, csv
import argparse
import logging
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('% (asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
activities = {'bc': 'Bicep Curl',
    'm': 'muscleup',
    'p': 'pullup',
    'pu': 'pushup',
    'd': 'dip',
    'pl': 'plank',
    's': 'squat'}

def logActivity(activity, reps, weight=0):
    #logger.info('logging workout')
    with open('workoutlog.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([activity.capitalize(),weight,reps,datetime.datetime.now()])
    #logger.info('workout saved.')
    print(f'{reps} {activities[activity]}s logged')
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=str, help='Activity (Bc)icep Curl, (M)uscleups, (P)ullups, (Pu)shups, (D)ips, (Pl)anks,(S)quats' )
    parser.add_argument('-w', type=int, help='Weight')
    parser.add_argument('-r', type=int, help='Number of Reps')
    args = parser.parse_args()
    logActivity(args.a, args.r, args.w)
