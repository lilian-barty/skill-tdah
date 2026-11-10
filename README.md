# Skill TDAH pour Claude

Un mode de travail pour les cerveaux TDAH. Vous tapez `/tdah`, Claude vous demande sur quoi vous voulez avancer, puis il vous rend une seule chose à faire, avec son temps estimé.

Je l'ai construit pour moi. Freelance, diagnostiqué TDAH à 36 ans, j'ai essayé Notion, Trello, GTD, les bullet journals et Sunsama : aucun n'a tenu plus de 6 semaines (le point commun de ces échecs, c'était moi). Ce skill est le premier système qui ne me demande pas d'être discipliné, juste de taper `/tdah` quand je suis perdu.

Je suis convaincu qu'un cerveau TDAH avance dès qu'on lui donne une structure, et que la motivation arrive après.

## Les modes

| Vous tapez | Quand | Ce qui se passe |
|---|---|---|
| `/tdah` | Vous vous asseyez et rien ne démarre | Une question, puis une seule action et son temps estimé ; s'il trouve un `SESSION.md`, il vous propose de reprendre là où vous vous étiez arrêté |
| `/tdah dump` | Votre tête déborde | Vous videz tout en vrac ; il trie entre aujourd'hui, plus tard, jamais et juste noter |
| `/tdah break [tâche]` | Une tâche vous fait fuir | Il la découpe en étapes de moins de 15 minutes et ne lance que la première |
| `/tdah stuck` | Vous tournez en rond | Il cherche la cause (flou, démarrage, tête qui tourne, fatigue) et ne traite que celle-là |
| `/tdah pomodoro [durée]` | Il faut s'y mettre | Un sprint de 10, 25 ou 45 minutes, minuteur du téléphone lancé, un seul objectif |
| `/tdah turbo` | Bon jour, le pas-à-pas vous agace | Toute l'instruction d'un coup, et retour au pas-à-pas dès que ça coince |
| `/tdah stop` | Impossible de décrocher, ou il faut changer de tâche | Il note où vous en êtes et par quoi reprendre, puis vous fait lever |
| `/tdah fin` | La journée se termine | Il liste ce qu'il a vu passer, note la chose à reprendre et range tout dans `SESSION.md` |
| `/tdah qui` | Vous voulez savoir qui a fait ça | L'histoire du skill, en 3 messages |

Il repère aussi tout seul les "je suis nul" et les "tout le monde y arrive sauf moi", les reconnaît en une phrase puis vous ramène à ce qui est faisable en 5 minutes.

Il compare enfin le temps prévu au temps réel, et au bout de quelques sessions ses estimations tiennent compte de votre propre écart.

## Installer

### Dans Claude Code

```
/plugin marketplace add lilian-barty/skill-tdah
/plugin install tdah@lilian-barty
```

Relancez Claude Code, puis tapez `/tdah`.

Sans plugin, ça marche aussi : copiez le dossier `skills/tdah` dans `~/.claude/skills/`.

### Dans l'app Claude, sur le web ou sur ordinateur

1. Téléchargez `tdah.zip` dans la [dernière version](https://github.com/lilian-barty/skill-tdah/releases/latest).
2. Vérifiez dans vos paramètres que l'exécution de code et la création de fichiers sont activées.
3. Ouvrez Personnaliser > Compétences, cliquez sur +, puis Créer une compétence > Télécharger une compétence, et choisissez le zip.

Ensuite, demandez le mode TDAH à Claude. Dans l'app, chaque conversation repart de zéro : la présentation peut donc revenir.

## Limites

- Il ne soigne rien. Ce n'est ni un traitement ni un avis médical, et seul un professionnel de santé pose un diagnostic de TDAH.
- Il ne chronomètre rien, puisque Claude ne voit pas le temps passer : c'est pour ça qu'il vous fait lancer le minuteur de votre téléphone.
- Il enlève le bruit autour de votre journée, et c'est vous qui faites la tâche.
- D'une conversation à l'autre, il ne garde que ce que `/tdah fin` et `/tdah stop` écrivent dans `SESSION.md`.
- Si la conversation dépasse la question des tâches (épuisement, propos inquiétants sur vous), il le dit et arrête de vous parler de travail.

Et si vous voulez seulement que Claude réponde plus court et mieux rangé, [i-have-adhd](https://github.com/ayghri/i-have-adhd) fait ça très bien, en anglais. Celui-ci sert à tenir une activité entière avec un cerveau qui zappe.

## L'auteur

Lilian Barty-Christophe, consultant freelance en IA à Paris. J'installe des outils IA chez des indépendants et dans des entreprises, puis je forme les équipes qui s'en servent. J'anime aussi des ateliers.

- Le site : [lilian-barty.fr/tdah](https://www.lilian-barty.fr/tdah/)
- Les nouvelles versions : [inscription facultative](https://www.lilian-barty.fr/tdah/#versions), un email par version
- Me dire ce que vous en faites : lilianchristophe.pro@gmail.com

Vous préparez une formation ou un atelier sur l'IA au travail, TDAH ou pas ? Écrivez-moi.

Une idée, un bug ? Ouvrez une issue. Je lis tout, sans promettre de délai (le TDAH, vous connaissez).

## Licence

MIT. Vous pouvez l'utiliser, le modifier et le redistribuer, y compris pour un usage pro, à condition de garder la mention de l'auteur.

## In English

A work mode for ADHD brains, built by a French freelancer diagnosed at 36. Type `/tdah` and Claude asks what you want to move forward on, then hands you one thing to do and how long it should take. It makes you start a phone timer for every sprint, compares estimated and actual time, and helps you stop when hyperfocus won't let go. The instructions are in French, but the skill answers in your language. Install it with the two commands above, or upload `tdah.zip` to the Claude app (Customize > Skills).
