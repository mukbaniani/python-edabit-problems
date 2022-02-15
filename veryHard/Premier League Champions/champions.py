def champions(teams):
    team_score, team_name, goal_difference = 0, '', 0
    for team in teams:
        score = team.get('wins') * 3 + team.get('draws')
        difference = team.get('scored') - team.get('conceded')
        if score > team_score:
            team_name = team.get('name')
            team_score = score
            goal_difference = difference
        elif score == team_score:
            if difference > goal_difference:
                team_name = team.get('name')
                goal_difference = difference
    return team_name
    