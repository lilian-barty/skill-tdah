# Skill TDAH pour Claude

Un mode de travail pour Claude, pensé pour les adultes TDAH. Vous tapez `/tdah`, Claude vous demande sur quoi vous voulez avancer et vous rend une seule action, avec son temps estimé.

La plupart des règles du skill s'appuient sur un résultat publié, cité plus bas avec son niveau de preuve, et celles qui n'en ont pas sont listées à part. Le skill lui-même n'a jamais été évalué par une étude, et la plupart des travaux cités portent sur des enfants ou sur des personnes sans TDAH : le transfert à un adulte TDAH qui travaille reste une hypothèse, signalée à chaque fois.

## Les modes

| Vous tapez | Quand | Ce qui se passe |
|---|---|---|
| `/tdah` | Rien ne démarre | Une question, puis une seule action et son temps estimé ; s'il trouve un `SESSION.md`, il propose de reprendre là où vous vous étiez arrêté |
| `/tdah dump` | Votre tête déborde | Vous videz tout en vrac ; il trie entre aujourd'hui, plus tard, jamais et juste noter |
| `/tdah break [tâche]` | Une tâche vous fait fuir | Il la découpe en étapes de moins de 15 minutes et ne lance que la première |
| `/tdah stuck` | Vous tournez en rond | Il cherche la cause (flou, démarrage, tête qui tourne, manque d'énergie) et ne traite que celle-là |
| `/tdah honte` | Vous vous jugez durement | Il le reconnaît en une phrase, puis revient à une action de 5 minutes ; il s'active aussi seul quand vous vous jugez |
| `/tdah pomodoro [durée]` | Il faut s'y mettre | Un sprint de 10, 25 ou 45 minutes, minuteur du téléphone lancé, un seul objectif |
| `/tdah turbo` | Bon jour, le pas-à-pas vous ralentit | Toute l'instruction d'un coup, et retour au pas-à-pas dès que ça coince |
| `/tdah stop` | Impossible de décrocher, ou il faut changer de tâche | Il note où vous en êtes et par quoi reprendre, puis vous invite à vous lever |
| `/tdah fin` | La journée se termine | Il liste ce qu'il a vu passer, note la chose à reprendre et propose de tout ranger dans `SESSION.md` |
| `/tdah qui` | Vous voulez savoir qui l'a écrit | L'histoire du skill, en 3 messages |

## Les sources de chaque règle

**Une seule action à la fois, des messages courts.** Le modèle de Barkley décrit le TDAH comme un déficit d'inhibition qui perturbe la mémoire de travail et l'autorégulation [1]. Garder une seule consigne en tête coûte moins qu'en garder 5. Niveau de preuve : modèle théorique, construit surtout à partir d'études sur l'enfant.

**Un minuteur pour chaque sprint.** Une revue de 2013 conclut que les personnes TDAH perçoivent et reproduisent moins bien les durées [2]. Barkley recommande de placer l'aide là où l'action se fait, sous forme de repère extérieur, plutôt que de compter sur la mémoire [3]. Claude ne voit pas le temps passer entre 2 messages, donc le skill vous fait lancer le minuteur de votre téléphone. Niveau de preuve : revue de la littérature (enfants et adultes) pour le déficit, avis d'expert pour le repère extérieur.

**Comparer le temps prévu au temps réel.** Tout le monde sous-estime la durée de ses propres tâches [4]. Le skill garde vos paires prévu/réel et en tire un ratio qui corrige les estimations suivantes. Niveau de preuve : expériences en population générale ; aucune étude trouvée ne l'a mesuré chez l'adulte TDAH.

**Découper en étapes qui commencent par un verbe.** Formuler à l'avance "quand X arrive, je fais Y" a permis à des enfants TDAH d'inhiber une réponse aussi bien que des enfants sans TDAH, sur une tâche de laboratoire [5]. Le découpage de `break` en reprend l'idée : une étape concrète décidée d'avance. Niveau de preuve : 2 expériences contrôlées, enfants ; le transfert au travail d'un adulte reste à démontrer.

**Noter ce qui tourne et écrire par quoi reprendre (`dump`, `stop`, `fin`).** Faire un plan précis pour un but inachevé supprime l'interférence de ce but sur la tâche en cours [6]. Niveau de preuve : plusieurs expériences, étudiants sans TDAH.

**Après 3 blocages, repartir par le plus facile.** Une suite de consignes faciles, presque toujours suivies, augmente les chances de suivre ensuite une consigne difficile [7]. Niveau de preuve : études expérimentales à cas unique, hors TDAH ; l'application ici est une extrapolation.

**Reconnaître la honte en une phrase (`honte`).** Chercher à chasser une pensée la fait revenir plus fort ensuite [8], même si les réplications donnent des effets variables. Une faible autocompassion explique une partie du lien entre procrastination et stress [9]. Les adultes TDAH rapportent une autocompassion plus faible et davantage de critiques perçues [10], et leur autocompassion explique une partie de leur détresse psychologique [11]. La dysrégulation émotionnelle est fréquente dans le TDAH [12]. Niveau de preuve : expériences (suppression de pensée), études corrélationnelles (autocompassion), revue (émotions) ; aucun essai n'a testé une réponse de ce type dans un outil.

**Reconnaître tout de suite une tâche finie.** Le modèle à double voie de Sonuga-Barke décrit une aversion au délai dans le TDAH : une récompense lointaine motive peu [13]. Niveau de preuve : modèle théorique, enfants.

**Un mode pour décrocher (`stop`).** L'hyperfocus est souvent rapporté par les personnes TDAH, mais la recherche le définit encore mal et l'a peu étudié [14]. Le mode `stop` repose donc surtout sur le résultat [6] : écrire la reprise libère la tâche en cours.

## Les règles sans preuve

- **Le pomodoro.** Aucune étude contrôlée publiée ne l'a testé chez l'adulte TDAH. Les essais sur les pauses portent sur des étudiants, avec des résultats mitigés. Le skill garde le sprint chronométré parce qu'il fournit un repère extérieur [3], sans promettre plus.
- **La présence de Claude pendant le travail** (le "body doubling"). Beaucoup de personnes TDAH disent que ça les aide, mais aucun essai contrôlé n'a été publié.
- **Le mode turbo.** Il vient de l'expérience de l'auteur, qui a des bons et des mauvais jours, sans source.
- **Le skill dans son ensemble.** Il n'a pas été évalué. Si vous l'utilisez, votre retour (ce qui aide, ce qui gêne) sert à le corriger : ouvrez une issue ou écrivez à lilianchristophe.pro@gmail.com.

## Limites

- Il ne soigne rien. Ce n'est ni un traitement ni un avis médical, et seul un professionnel de santé pose un diagnostic de TDAH.
- Il ne chronomètre rien : le minuteur, c'est votre téléphone.
- D'une conversation à l'autre, il ne garde que ce que `/tdah dump`, `/tdah stop` et `/tdah fin` écrivent dans `SESSION.md`.
- Si la conversation dépasse la question des tâches (épuisement, propos inquiétants sur vous), il le dit, vous suggère d'en parler à un proche ou à un professionnel et arrête de vous parler de travail. En cas d'idées suicidaires, il donne le 3114 en France ou le numéro d'urgence de votre pays.
- Si vous voulez seulement que Claude réponde plus court et mieux rangé, [i-have-adhd](https://github.com/ayghri/i-have-adhd) fait ça, en anglais.

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

## Références

1. Barkley, R. A. (1997). Behavioral inhibition, sustained attention, and executive functions: constructing a unifying theory of ADHD. *Psychological Bulletin*, 121(1), 65-94. https://doi.org/10.1037/0033-2909.121.1.65
2. Noreika, V., Falter, C. M., & Rubia, K. (2013). Timing deficits in attention-deficit/hyperactivity disorder (ADHD): evidence from neurocognitive and neuroimaging studies. *Neuropsychologia*, 51(2), 235-266. https://doi.org/10.1016/j.neuropsychologia.2012.09.036
3. Barkley, R. A. (1997). *ADHD and the Nature of Self-Control*. Guilford Press. Résumé par l'auteur : [Executive Functioning and Self-Regulation in ADHD](https://www.russellbarkley.org/factsheets/ADHD_EF_and_SR.pdf).
4. Buehler, R., Griffin, D., & Ross, M. (1994). Exploring the "planning fallacy": why people underestimate their task completion times. *Journal of Personality and Social Psychology*, 67(3), 366-381. https://doi.org/10.1037/0022-3514.67.3.366
5. Gawrilow, C., & Gollwitzer, P. M. (2008). Implementation intentions facilitate response inhibition in children with ADHD. *Cognitive Therapy and Research*, 32, 261-280. https://doi.org/10.1007/s10608-007-9150-1
6. Masicampo, E. J., & Baumeister, R. F. (2011). Consider it done! Plan making can eliminate the cognitive effects of unfulfilled goals. *Journal of Personality and Social Psychology*, 101(4), 667-683. https://doi.org/10.1037/a0024192
7. Mace, F. C., Hock, M. L., Lalli, J. S., West, B. J., Belfiore, P., Pinter, E., & Brown, D. K. (1988). Behavioral momentum in the treatment of noncompliance. *Journal of Applied Behavior Analysis*, 21(2), 123-141. https://doi.org/10.1901/jaba.1988.21-123
8. Wegner, D. M., Schneider, D. J., Carter, S. R., & White, T. L. (1987). Paradoxical effects of thought suppression. *Journal of Personality and Social Psychology*, 53(1), 5-13. https://doi.org/10.1037/0022-3514.53.1.5
9. Sirois, F. M. (2014). Procrastination and stress: exploring the role of self-compassion. *Self and Identity*, 13(2), 128-145. https://doi.org/10.1080/15298868.2013.763404
10. Beaton, D. M., Sirois, F., & Milne, E. (2020). Self-compassion and perceived criticism in adults with attention deficit hyperactivity disorder (ADHD). *Mindfulness*, 11(11), 2506-2518. https://doi.org/10.1007/s12671-020-01464-w
11. Beaton, D. M., Sirois, F., & Milne, E. (2022). The role of self-compassion in the mental health of adults with ADHD. *Journal of Clinical Psychology*, 78(12), 2497-2512. https://doi.org/10.1002/jclp.23354
12. Shaw, P., Stringaris, A., Nigg, J., & Leibenluft, E. (2014). Emotion dysregulation in attention deficit hyperactivity disorder. *American Journal of Psychiatry*, 171(3), 276-293. https://doi.org/10.1176/appi.ajp.2013.13070966
13. Sonuga-Barke, E. J. S. (2003). The dual pathway model of AD/HD: an elaboration of neuro-developmental characteristics. *Neuroscience & Biobehavioral Reviews*, 27(7), 593-604. https://doi.org/10.1016/j.neubiorev.2003.08.005
14. Ashinoff, B. K., & Abu-Akel, A. (2021). Hyperfocus: the forgotten frontier of attention. *Psychological Research*, 85(1), 1-19. https://doi.org/10.1007/s00426-019-01245-8

Références vérifiées le 10 novembre 2026. Une erreur, une étude plus récente ou plus solide ? Ouvrez une issue pour la signaler.

## L'auteur

Lilian Barty-Christophe, consultant en adoption de l'IA et automatisation à Paris, diagnostiqué TDAH à 36 ans. Il a écrit ce skill pour son propre travail et s'en sert tous les jours.

- Le site : [lilian-barty.fr/tdah](https://www.lilian-barty.fr/tdah/)
- Les nouvelles versions : [inscription facultative](https://www.lilian-barty.fr/tdah/#versions), un email par version
- Contact : lilianchristophe.pro@gmail.com

## Licence

MIT. Vous pouvez l'utiliser, le modifier et le redistribuer, y compris pour un usage pro, à condition de garder la mention de l'auteur.

## In English

A work mode for Claude, designed for adults with ADHD. Type `/tdah` and Claude asks what you want to move forward on, then gives you one action and its estimated time. Most rules are linked to published research (see "Références" above, with DOIs) and to their level of evidence, and the rules without evidence are listed separately: most studies involve children or people without ADHD, and the skill itself has not been evaluated. The instructions are in French, but the skill answers in your language. Install it with the two commands above, or upload `tdah.zip` to the Claude app (Customize > Skills).
