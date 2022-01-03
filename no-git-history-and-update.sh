rm -rf .git/
git init
git branch -M main
git add .
git commit -m "update"
git remote add origin git@github.com:topazus/fedora-copr.git
git push -f origin main
