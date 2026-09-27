# Skill TDAH pour Claude

Un mode de travail pour les cerveaux TDAH. Tu tapes `/tdah`, Claude te pose trois questions, puis il te rend une seule chose à faire, avec son temps estimé.

Je l'ai construit pour moi. Freelance, diagnostiqué TDAH à 36 ans, j'ai essayé Notion, Trello, GTD, les bullet journals et Sunsama : aucun n'a tenu plus de six semaines (le point commun de ces échecs, c'était moi). Ce skill est le premier système qui ne me demande pas d'être discipliné, juste de taper `/tdah` quand je suis perdu.

Le TDAH ne manque pas de motivation, il manque de structure.

## Ce qu'il fait

| Tu tapes | Quand | Ce qui se passe |
|---|---|---|
| `/tdah` | Tu t'assois et rien ne démarre | Trois questions, une à la fois, puis une seule action et son temps estimé |
| `/tdah dump` | Ta tête déborde | Tu vides tout en vrac ; il trie entre aujourd'hui, plus tard, jamais et juste noter |
| `/tdah break [tâche]` | Une tâche te fait fuir | Il la découpe en étapes de moins de 15 minutes et ne te montre que la première |
| `/tdah stuck` | Tu tournes en rond | Il sépare le cerveau qui refuse de démarrer de l'anxiété qui tourne, et traite l'un ou l'autre |
| `/tdah pomodoro [durée]` | Il faut s'y mettre | Un sprint de 10, 25 ou 45 minutes, avec un seul objectif |
| `/tdah turbo` | Bon jour, le pas-à-pas t'agace | Toute l'instruction d'un coup, et retour au pas-à-pas dès que ça coince |
| `/tdah fin` | La journée se termine | Il résume, note la chose à reprendre demain et la range dans `SESSION.md` |
| `/tdah qui` | Tu veux savoir qui a fait ça | L'histoire du skill, en trois messages |

Il repère aussi tout seul les « j'aurais dû » et les « je suis nul », et te ramène à ce qui est faisable en cinq minutes, sans commenter ton ressenti.

## Installer

### Dans Claude Code

```
/plugin marketplace add lilian-barty/skill-tdah
/plugin install tdah@lilian-barty
```

Relance Claude Code, puis tape `/tdah`.

Sans plugin, ça marche aussi : copie le dossier `skills/tdah` dans `~/.claude/skills/`.

### Dans l'app Claude, sur le web ou sur ordinateur

1. Télécharge `tdah.zip` dans la [dernière version](https://github.com/lilian-barty/skill-tdah/releases/latest).
2. Vérifie dans tes paramètres que l'exécution de code et la création de fichiers est activée.
3. Ouvre Personnaliser > Compétences, clique sur +, puis Créer une compétence > Télécharger une compétence, et choisis le zip.

Ensuite, demande le mode TDAH à Claude. Dans l'app, chaque conversation repart de zéro : le message d'accueil peut donc revenir.

## Ce qu'il ne fait pas

- Il ne soigne rien. Ce n'est ni un traitement ni un avis médical, et seul un professionnel de santé pose un diagnostic de TDAH.
- Pas de vrai chronomètre : pendant un pomodoro, c'est toi qui reviens quand le temps est écoulé.
- Ta journée reste la tienne. Il enlève le bruit ; la tâche, c'est toi qui la fais.
- D'une conversation à l'autre, il ne garde que ce que `/tdah fin` écrit dans `SESSION.md`.
- Si la conversation dépasse la question des tâches (épuisement, propos inquiétants sur toi), il le dit et arrête de te parler de travail.

Et si tu veux seulement que Claude réponde plus court et mieux rangé, [i-have-adhd](https://github.com/ayghri/i-have-adhd) fait ça très bien, en anglais. Celui-ci sert à tenir une activité entière avec un cerveau qui zappe.

## Qui l'a fait

Lilian Barty-Christophe, consultant freelance en IA à Paris. J'installe des outils IA chez des indépendants et dans des entreprises, puis je forme les équipes qui s'en servent. J'anime aussi des ateliers.

- Le site : [lilian-barty.fr/tdah](https://www.lilian-barty.fr/tdah/)
- Les nouvelles versions : [inscription facultative](https://www.lilian-barty.fr/tdah/#versions), un email par version
- Me dire ce que tu en fais : lilianchristophe.pro@gmail.com

Tu prépares une formation ou un atelier sur l'IA au travail, TDAH ou pas ? Écris-moi.

Une idée, un bug ? Ouvre une issue. Je lis tout, sans promettre de délai (le TDAH, tu connais).

## Licence

MIT. Tu peux l'utiliser, le modifier et le redistribuer, y compris pour un usage pro, à condition de garder la mention de l'auteur.

## In English

A work mode for ADHD brains, built by a French freelancer diagnosed at 36. Type `/tdah` and Claude asks three questions, then hands you one thing to do and how long it should take. The instructions are in French, but the skill answers in your language. Install it with the two commands above, or upload `tdah.zip` to the Claude app (Customize > Skills).
