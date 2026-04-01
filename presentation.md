\# Mr. Le Président



\## 1. Présentation globale



Mr. Le Président est un jeu né à la base d'un autre jeu : "Lapse: A Forgotten Future". 

C'est un jeu que nous avions beaucoup apprécié et nous souhaitions à notre tour créer 

un jeu narratif. Cependant, nous avons décidé de modifier la quasi-totalité du 

fonctionnement de ce jeu pour donner plus d'importance au chemin narratif. De ce fait, 

nous avons gardé uniquement le principe de gestion et le contexte pour nous focaliser 

sur la création d'un jeu laissant au joueur un nombre de fins plus élevé, centré surtout 

sur les décisions morales auxquelles le joueur est confronté. En résumé, Mr. Le Président 

est le projet que nous considérons comme le jeu que nous aurions voulu avoir plus tôt 

dans notre enfance.



Dans ce jeu, le joueur incarne le président d'une nation proche-futuriste en guerre. 

Au fil du temps, plusieurs personnages membres de l'État lui proposeront des décisions 

à prendre afin de gérer différentes crises nationales, telles que la guerre, l'économie 

ou encore la stabilité politique. Selon les choix effectués, le joueur influencera le 

destin du pays et débloquera plusieurs fins possibles, ainsi que des fins inédites 

pouvant apparaître durant l'intrigue.



Pour ce projet, nous nous sommes vite rendu compte que le plus important était de trouver 

un moyen simple et organisé d'appliquer chaque conséquence aux différentes questions et 

dialogues que nous avions imaginés. Pour résoudre ce problème, nous avons utilisé une 

notion importante de programmation étudiée en classe : les listes.



Nous avons placé toutes nos lignes de dialogue dans des listes en veillant à respecter 

un ordre précis pour chacune d'entre elles. Pour les questions impactant les jauges de 

gameplay (armée, environnement, économie et population), nous avons décidé de créer 

3 questions pour chacune des relations (+environnement / -armée, +population / 

\-environnement, etc.), ce qui représente au total 36 questions.



À chaque clic, une phrase "situation" est piochée au hasard depuis la liste contenant 

les dialogues du fichier "histoire.txt". Celle-ci explique un problème au joueur qui, 

une fois lu, cliquera une nouvelle fois pour faire apparaître la question correspondante 

dans "question.txt", ayant le même index que la présentation. De ce fait, chaque 

présentation est associée à la question qui lui correspond. Les index servent aussi à 

augmenter ou diminuer les jauges de gameplay. Par exemple, toutes les questions entre 

l'index 0 et 2 font augmenter l'environnement et baisser l'armée.



Les dialogues spéciaux fonctionnent également grâce à ce système d'index. Toutes les 

X questions, un dialogue spécial s'affiche en fonction du nombre de dialogues spéciaux 

déjà affichés ainsi que des réponses antérieurement sélectionnées. Puis, en fonction 

des choix effectués, on adapte l'index pour afficher le bon dialogue.



\## 2. Organisation du travail



Pour réaliser ce projet, nous avons formé un groupe de 3 personnes : Maxence 

Tropia-Party, Apolline Bec et Laura Leonor.



Nous nous sommes réparti différents rôles tout au long du développement.



\*\*Maxence\*\* est à l'origine de l'idée du projet. Il a contribué au développement du 

système de jauges, du système d'affichage du texte et a aidé Laura à créer le système 

des textes spéciaux


\*\*Laura\*\* a développé le système de textes spéciaux et a organisé les différents 

dialogues suivant les choix du joueur. Elle a également designé tous les personnages 

présents à l'écran.



\*\*Apolline\*\*, quant à elle, a géré le système à des différents personnages, 

du background ainsi que tous les effets visuels visibles. Elle a aussi participé à la 

création du graphisme en ayant créé le bureau visible tout au long du jeu.



Au total, ce projet a duré environ 6 semaines avec une présentation en classe en début 

de projet (2ème et 3ème semaines). Il est important de noter qu'une partie de nos 

épreuves blanches du baccalauréat s'est déroulée durant cette période.



\## 3. Étapes du projet



Durant la première semaine, nous avons imaginé quel type de jeu nous allions créer et 

avons commencé à réunir toutes nos idées de gameplay ainsi que de graphisme.



Durant la deuxième semaine, nous avons trié les idées retenues et avons commencé à 

coder les premières bases de notre jeu (affichage du texte, positionnement de la 

fenêtre, etc.).



La troisième semaine a marqué le début d'une phase plus intense avec la programmation 

du système de jauges et des premières questions, qui sont restées jusqu'à la dernière 

version du projet.



Entre la 3ème et la 4ème semaine, nous avons également commencé le système de textes 

spéciaux ainsi que le développement du scénario.



La 5ème semaine a conclu le travail principal du code. Tous les grands systèmes sont 

créés, les dernières questions et lignes du script sont implémentées et les index 

définitivement adaptés.



Enfin, la dernière semaine a peaufiné l'aspect visuel du jeu et intégré les graphismes. 

(Jusque-là, le jeu n'était qu'un triste écran noir)



\## 4. Fonctionnement et tests



\### État d'avancement

Au moment du dépôt, toutes les questions et tous les dialogues sont implémentés. 

Le jeu est entièrement jouable, de l'introduction jusqu'aux 10 fins disponibles.



\### Méthode de débogage

Le débogage a été réalisé de manière assez simple. Les deux principales mécaniques 

qui nous ont permis de vérifier le bon fonctionnement du jeu sont :

\- L'affichage des valeurs des jauges via des `print()` dans la console après chaque 

choix du joueur.

\- Une réduction du délai avant l'apparition des textes spéciaux : tout au long du 

développement, les textes spéciaux apparaissaient 3 fois plus vite, ce qui nous 

permettait de vérifier rapidement tous les chemins narratifs.



\### Difficultés rencontrées

Les principaux problèmes rencontrés étaient des erreurs de gestion de fonctions : 

certaines étaient mal appelées ou leur logique était incorrecte. Ces erreurs étaient 

facilement détectables et corrigées rapidement. Un deuxième type de bug récurrent 

concernait des textes qui ne s'affichaient pas au bon moment, notamment lorsque nous 

ajoutions de nouvelles lignes de dialogue, ce qui entraînait un décalage de tous les 

index.



\## 5. Ouverture



\### Idées d'amélioration

Nous trouvons que ce jeu, reposant sur différentes fins possibles, manque justement 

de choix et de chemins différents. Notre temps de développement étant limité et notre 

démarrage tardif, nous avons pu développer seulement 10 fins — ce qui reste satisfaisant 

— mais avec une moyenne de 2 à 4 choix par chemin. Avec plus de temps, nous aurions 

Nous aurions souhaité enrichir davantage le scénario et ajouter de nouvelles fins. 

Nous aurions également souhaité implémenter plus de mécaniques imaginées au départ comme :
-l'affichage de l'argent à la place d'une jauge économie
-plus de personnages
-un dossier avec un résumé du passé de chaque personnage



\### Analyse critique

Nous pensons que ce projet reste une réussite malgré tout, notamment du point de vue 

de la programmation. Nous avons réussi à incorporer un grand nombre de notions étudiées 

en classe : les listes, les boucles, les conditions, ainsi que les dictionnaires, que 

nous avons découverts en plein milieu du développement et que nous avons pu réutiliser 

immédiatement de façon concrète. C'est précisément le but principal des Trophées NSI.



Le programme permet d'implémenter facilement de nouvelles questions et chemins en 

modifiant simplement certains index, ce qui rend notre code flexible et indépendant 

des questions et dialogues originaux.



Je trouve cependant que ce projet manque de profondeur, comme mentionné précédemment. 

Il pourrait être vraiment amélioré avec plus de choix, de questions et de mises à jour 

graphiques.



\### Compétences développées

Ce projet nous a permis d'apprendre à réutiliser les bases de la programmation dans 

des projets concrets. Il nous a aussi permis de comprendre la structure 

fonctions / boucle principale. Ce projet étant réalisé à trois, nous avons pu 

comprendre comment des fonctions sont créées et réutilisées par d'autres personnes.



\### Démarche d'inclusion

Notre jeu vidéo a l'avantage d'être accessible à n'importe quel type de joueur et 

peut satisfaire tous les goûts. Aucune compétence n'est requise pour y jouer : les 

commandes sont simples, il suffit de cliquer, ce qui rappelle que ce jeu se base 

avant tout sur les choix du joueur.







\### Nature du code et usage de l'IA



\#### Degré de création originale

Le code de Mr. Le Président a été entièrement conçu et développé par les trois membres 

de l'équipe. Toute la structure du projet comme le système de jauges, le système d'index pour les 

dialogues, les chemins narratifs et les textes spéciaux sont des créations originales.



\#### Sources externes

Nous avons utilisé un tutoriel YouTube pour la création du système de boutons, en raison 

de l'utilisation des classes, notion non étudiée en cours :

https://youtu.be/G8MYGDf\_9ho

Le code issu de ce tutoriel a été adapté et intégré à notre projet.



\#### Exploitation de codes existants

Aucun code existant n'a été copié-collé directement. Le tutoriel cité ci-dessus nous a 

servi de base pour comprendre le fonctionnement des classes en Python, que nous avons 

ensuite adaptée à notre projet.



\#### Utilisation de l'intelligence artificielle

L'IA a été utilisée de manière limitée, uniquement pour corriger certains problèmes 

extérieurs à la programmation :

\- Correction orthographique des dialogues et du script du jeu (dyslexie oblige).

\- Réorganisation des variables du script : au début du développement, aucun système 

d'organisation n'était prévu, ce qui rendait le code chaotique. L'IA nous a aidés 
 à restructurer les variables pour plus de lisibilité.





