unconfirmed_users = ['A', 'bhshs', 'cshdhd']
confirmed_users = []

while unconfirmed_users:
    user = unconfirmed_users.pop()
    print(f"Verifying user '{user}'")
    confirmed_users.append(user.title())

for user in confirmed_users:
    print(f"Confirmed user is {user}")