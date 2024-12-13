- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip3 install pip --upgrade`
- `pip3 install rasa`
- `rasa init --no-prompt`

- for only rasa run:  `rasa shell`

- rasani ma'lumotlarni to'g'irlab bo'lgan train qilish: `rasa train`

- project run: `python manage.py runserver`
- rasa run with action: `rasa run actions & rasa shell`

- run action other port: `rasa run actions --port 5056`
 

- portni kim ishlatayorganini ko'rish: `sudo lson -i :5055`
- sudo kill <PID>