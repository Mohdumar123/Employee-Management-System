
echo "BUILD START"
python3.10 -m pip install -r rquirements.txt
python3.10 manage.py collectstatic --noinput --clear
echo "BUILD END"