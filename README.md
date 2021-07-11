python version 3.9
install requirements : pip install -r requirements.txt
run application :  python manage.py runserver 8000


supper user : lasith:admin123

login curl -X POST \
  http://127.0.0.1:8000/bms/user/login \
  -H 'Accept: */*' \
  -F password=admin123


curl -X GET \
  http://127.0.0.1:8000/bms/player/1 \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MDI2MDI0LCJqdGkiOiI0Yzk2NGZmZjU3ZmE0NGNlYTY0N2M3OWRjYjJiODk4ZiIsInVzZXJfaWQiOjF9.kTsJjQ9louwOagX_jYnyiDq0NLypP0LxuVa89H1GsFg'