# Versions

## 1.4.1, le 26 novembre 2026

- Deux messages reformulés : "Revenez me dire quand c'est fait (ou si quelque chose bloque)" et, après un sprint inachevé, "Qu'est-ce qui vous a arrêté ?".

## 1.4.0, le 26 novembre 2026

- Lien avec le skill `/orga` : `/tdah` propose le bloc du jour lu dans `SEMAINE.md` et coche les blocs faits au `fin`.
- Plusieurs tâches citées : l'ordre de choix passe par ce qui bloque le reste (accès, outil en panne), puis l'argent à faire rentrer, puis la préparation d'un rendez-vous proche, avant l'échéance la plus proche.
- `fin` raye d'une semaine planifiée les réponses attendues qui sont arrivées.
- La reprise notée par `stop` et `fin` s'écrit "quand [moment], alors [geste]". L'effet de ce format sur le passage à l'acte est petit (d = 0,27), le skill ne promet pas de déclic.
- `pomodoro` fait préparer la place avant de lancer le minuteur : fichier ouvert, notifications coupées.
- Une tâche d'apprentissage découpée par `break` finit par 3 questions sans les notes, jamais par une relecture.
- Pour s'engager devant quelqu'un, le skill propose d'annoncer un geste daté à une personne dont vous respectez le jugement, plutôt qu'une ambition.
- Retiré : le "réservoir vide" après 3 blocages. L'idée d'une volonté qui s'épuise comme un muscle ne se réplique pas.
- Nouveau fichier `references/engagement-apports-2026-11.md` : les études derrière ces règles, leurs limites, et les résultats rétractés à ne pas citer comme preuve.

## 1.3.0, le 10 novembre 2026

Révision complète après une critique du skill au regard de ce qu'on sait du TDAH.

- Vouvoiement partout, avec des formulations neutres en genre. Le tutoiement reste possible si vous le demandez.
- Chaque sprint commence par un minuteur que vous lancez sur votre téléphone : Claude ne voit pas le temps passer, et un cerveau TDAH non plus.
- Le skill compare le temps prévu au temps réel et garde votre ratio dans `SESSION.md` pour ajuster les estimations suivantes.
- Le démarrage tient en une question. S'il trouve un `SESSION.md`, il propose de reprendre là où vous vous étiez arrêté.
- `stuck` distingue 4 causes : ne pas savoir par où commencer, ne pas réussir à démarrer, la tête qui tourne, le manque d'énergie.
- Après 3 blocages, il fait repartir sur la tâche la plus facile.
- `honte` reconnaît le jugement en une phrase avant de revenir à l'action, et ne se déclenche plus sur un simple constat.
- Nouveau mode `stop` pour décrocher d'un hyperfocus ou changer de tâche sans perdre le fil.
- `fin` liste d'abord ce que Claude a vu passer et propose de rayer ce qui traîne depuis plus de 2 semaines.
- Le fichier de première utilisation va dans `~/.claude/` au lieu de la racine de chaque projet.
- Le README cite la source de chaque règle avec son niveau de preuve, et liste les règles qui n'en ont pas.

## 1.2.0, le 28 octobre 2026

- Marche aussi sans accès aux fichiers (app Claude, téléphone) : la grande intro ne revient pas à chaque conversation, les "plus tard" restent dans la conversation et le bilan de `fin` sort dans un encadré à copier.
- Les sous-commandes se tapent avec ou sans barre oblique : "dump" suffit sur téléphone.
- En cas d'idées suicidaires, le skill donne le 3114 en France et le numéro d'urgence du pays ailleurs.
- Le message du vendredi ne s'ajoute plus quand le skill ne connaît pas la date du jour.

## 1.1.0, le 20 octobre 2026

- `/tdah` rappelle les modes disponibles à chaque lancement, en deux lignes, avant la première question.

## 1.0.0, le 27 septembre 2026

Première version en libre accès.

- Neuf modes : démarrage, `dump`, `break`, `turbo`, `stuck`, `honte`, `pomodoro`, `fin` et `qui`.
- Le mode turbo coupe désormais au premier signe de blocage, y compris un simple « je suis perdu ».
- Installation par plugin dans Claude Code, ou par zip dans l'app Claude.
