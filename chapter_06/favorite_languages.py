favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust'
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}")
point_value = favorite_languages.get('point', 'No such string defined')
print(point_value)