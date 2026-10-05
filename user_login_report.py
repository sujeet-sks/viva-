import os
from datetime import datetime

#(username, login_time)
login_history = []
current_users = {}

current_sys_user = os.environ.get('USERNAME') or os.environ.get('USER') or "unknown"
current_users[current_sys_user] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#all currently logged-in users and login times
print("--- Currently Logged-in Users & Times ---")
for user, l_time in current_users.items():
    print(f"User: {user} | Logged in at: {l_time}")

#total number of currently logged in users
print(f"\nTotal Currently Logged-in Users: {len(current_users)}")

#number of unique users who have ever logged in
all_logins = [session[0] for session in login_history] + [current_sys_user]
unique_count = len(set(all_logins))
print(f"Total Unique Users (Historical): {unique_count}")

#last 10 user logins
print("\n--- Last 10 User Logins (Most Recent First) ---")
full_history = login_history + [(current_sys_user, current_users[current_sys_user])]
last_10 = full_history[-10:][::-1]

for user, l_time in last_10:
    print(f"[{l_time}] {user} logged in")

#Check if a user taken from input is currently logged in or not
search_user = input("Enter a username to check status: ").strip()

if search_user in current_users:
    print(f"Yes! {search_user} is currently logged in (Since: {current_users[search_user]}).")
else:
    print(f"No. {search_user} is not logged in right now.")
