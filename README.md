# Project Repo for Reverse_Geocoding

When ever starting to work if the branch is a shared branch, always do a `git pull` prior to making any changes. It will avoid headaches from merge conflicts. 

After making changes especially if working at the same time as someone else remember to commit changes frequently. The commands to add and commit are in `commit.sh`.

To commit changes in this repo you can use the commit.sh command, but I would get familiar with the script or copy the script to other repos you use. To run the script run

`bash commit.sh 'commit message'`

### Useful git commands:

* Update the repo with your latest changes
```
git add --all
git commit -m 'updating'
git push
```

* Pull any changes others have made
```
git pull
```

* Switch to a different branch (Do not include the <> just the name of the branch switch too)
```
git checkout <branch name>
```

* List all branches and show the current branch you are working in.
```
git branch
```