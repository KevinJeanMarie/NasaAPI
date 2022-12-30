Installation du projet :

git clone https://github.com/KevinJeanMarie/NasaAPI.git 

cd NasaAPI

tapez la commande : "pip install -r requirements.txt" pour installer les packages qui se trouvent dans le fichier requirements.txt pour faire fonctionner le projet.

puis tapez la commande "python manage.py runserver" pour lancer le projet.

Voici ce que vous verrez (image ci-dessous)
<img width="958" alt="Capture d’écran 2022-12-30 212734" src="https://user-images.githubusercontent.com/90609887/210112443-9dd744a6-a451-4638-b1a1-38e3811250b0.png">


en cliquant sur le lien de l'api vous avez l'affichage

<img width="959" alt="Capture d’écran 2022-12-30 210807" src="https://user-images.githubusercontent.com/90609887/210108301-1798dfbd-0f2e-471b-9ade-0c456d7c4542.png">

Vous n'avez pas besoin de vous connecter en tant qu'admin pour accéder aux projet mais si jamais vous souhaitez le faire pour modifier des données voici les instructions pour vous connecter : 

Cliquez sur ce lien http://127.0.0.1:8000/admin/login/?next=/admin/

<img width="494" alt="Capture d’écran 2022-12-30 214040" src="https://user-images.githubusercontent.com/90609887/210112460-d2983c9e-c807-4ccf-a537-1b85bb20413d.png">

login : test
password : rootrootroot

<img width="948" alt="Capture d’écran 2022-12-30 221642" src="https://user-images.githubusercontent.com/90609887/210112497-4754523c-eadb-4ec3-a14a-c0372a51523b.png">
<img width="960" alt="Capture d’écran 2022-12-30 211643" src="https://user-images.githubusercontent.com/90609887/210112498-5fa5946f-3a20-4e17-bab0-17ffffdd9065.png">

Dans le fichier "apinasa.py" vous avez l'api de la NASA et une clé API généré :

<img width="506" alt="Capture d’écran 2022-12-30 221759" src="https://user-images.githubusercontent.com/90609887/210113522-81cba6fc-98b2-4dad-81b7-f2785d836dc0.png">

base de données PostgreSQL:
<img width="760" alt="Capture d’écran 2022-12-30 211712" src="https://user-images.githubusercontent.com/90609887/210112543-48bbd393-6226-4012-a028-3cb63c285bf8.png">
