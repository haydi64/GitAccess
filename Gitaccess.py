from github import Github
from datetime import datetime, timedelta
g = Github("haydi64", "Icybreeze@68821")

user = g.get_user()

repo_LCA = g.get_repo("haydi64/LCA")

repo_aleth = g.get_repo("haydi64/aleth")

since = datetime.now() - timedelta(days=30)
commits = repo_LCA.get_commits(since=since)
print(user.login)
print("Time of last commit in the " + repo_LCA.name + " repo is:")
print(commits[0].commit.author.date)

print(list(repo_aleth.get_branches()))