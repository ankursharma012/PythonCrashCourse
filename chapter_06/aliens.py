aliens = []

for alien_number in range(30):
    new_alien = {"color":"green", "points":alien_number}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)

print(f"Total number of aliens are: {len(aliens)}")
