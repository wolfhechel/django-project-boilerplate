rm LICENSE README.md
git init .
virtualenv .

source bin/activate
pip install -r requirements/development.txt

rm $0
