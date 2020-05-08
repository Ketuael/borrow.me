## API - to backup these borrowments!

### API branch for project "borrow.me"
Aby uzyskać działające API na swoim urządzeniu, należy:

0. Mieć zainstalowanego Pythona w wersji 3.6
1. Sklonować to repozytorium
2. Stworzyć pythonowe venv / utworzyć projekt w PyCharmie
3. Zainstalować następujące pakiety (mając uruchomione venv):

pip install Django && pip install django-rest-framework && pip install Pillow && pip install django-cors-headers

4. Aby uruchomić serwer należy, będąc w głównym katalogu i przy uruchomionym venv, wpisać w konsoli:

python manage.py runserver

5. Konsola powinna zwrócić adres serwera na localhoscie
6. Ale najprościej jest po prostu wejść w ten link: http://ketuael.eu.pythonanywhere.com/api/ :)
