from trueskill import Rating, rate

teams = [(Rating(), ), (Rating(), ), (Rating(), ), (Rating(), )]
rankings = [1,2,3,4]

teams_updated = rate(teams, rankings)

print('Without partial update.')
print(teams_updated)

print('\n')

partial_weights = [(1, ), (1, ), (0.5, ), (0.3, )]
teams_updated_partial = rate(teams, rankings, partial_weights=partial_weights)
print('With partial update.')
print(teams_updated_partial)