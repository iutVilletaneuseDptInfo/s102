# SAÉ S1.02 : Le nouveau choixpeau pas magique de Poudlard

Ce document correspond au sujet de la SAÉ S1.02 de l'année universitaire 2025/2026. Ce travail est à faire par binôme en autonomie. Il correspond à la suite de la SAÉ S1.01.
La SAÉ devra être rendue au plus tard le **18 janvier 2026**.


## Évaluation

La SAÉ sera notée de la manière suivante :

- Évaluation du rendu : 8 points répartis de la manière suivante
    - Correction automatique du code via des tests unitaires : 2 points
    - Tests unitaires rendus : 2 points
    - Qualité du code (clarté, efficacité, commentaires, docstring) : 2 points
    - Comparaison expérimentale des méthodes de prédiction (fichier notebook) : 2 points


- Contrôle du **22 janvier 2026** : 12 points

**Attention :** Pour le contrôle, il faut connaître le sujet et le code (les structures de données utilisées et les diffférentes fonctions définies) dans les SAÉ S1.01 et S1.02. Il faut notamment connaître le type des arguments et le type de valeur retourné pour chacune des fonctions. 

## Sujet

Le sujet est la suite de la SAÉ S1.01. La correction de cette SAÉ est donnée dans le fichier `s101.py`. Le code de cette SAÉ doit être défini dans le fichier `s102.py` et les tests unitaires doivent être définis dans le fichier `test_s102.py`.

**Remarque :** Les noms des fonctions à définir sont en anglais pour faire la différence avec les fonctions définies dans la SAÉ S1.01.


## Contexte

Même si la méthode de répartition développée dans la SAÉ S1.01 est plus précise qu'une méthode de répartition aléatoire, ce n'est quand même pas incroyable, et Albus Dumbledore avec son idée d'utiliser l'informatique pour répartir les élèves est la risée des Serpentards ! Il faut sauver la situation en améliorant la méthode de répartition !

La professeure Chourave a deux idées : 
- il faut plus d'information sur les futurs élèves pour mieux les connaître. Pour cela, il leur faut répondre à 10 questions au lieu de 4. Elle a même la liste des questions (dont les réponses sont des entiers entre 1 et 10):
    - À quel point aimez-vous prendre des risques pour défendre une cause juste ?
    - Comment évaluez-vous votre curiosité intellectuelle et votre soif d’apprendre ?
    - Quelle importance accordez-vous à la loyauté envers vos amis et votre famille ?
    - À quel point êtes-vous ambitieux et déterminé à atteindre vos objectifs personnels ?
    - Comment réagissez-vous face à une injustice ? (1 = indifférence, 10 = action immédiate)
    - À quel point aimez-vous résoudre des énigmes ou des problèmes complexes ?
    - Quelle est votre capacité à travailler en équipe et à encourager les autres ?
    - À quel point êtes-vous prêt à utiliser la ruse pour obtenir ce que vous voulez ?
    - Comment gérez-vous les échecs ou les critiques ? (1 = abandon, 10 = persévérance)
    - Quelle est votre préférence : être admiré pour vos réalisations ou pour votre gentillesse ? (1 = réalisations, 10 = gentillesse)

- Si un futur élève répond de la même manière que le fondateur d'une des quatre maisons, il est fort probable qu'il faille affecter ce futur élève à cette maison. Elle propose de réveiller les fantômes des fondateurs des quatre maisons pour leur demander de répondre eux-mêmes aux 10 questions. Ainsi, il suffit de comparer les réponses de chaque futur élève à celles des fondateurs et d'affecter l'élève dans la maison du fondateur ayant les réponses les plus proches.

Comme vous avez réussi à implémenter correctement la première méthode de répartition, c'est à vous qu'il revient de coder cette nouvelle méthode. C'est parti !

### Question 1

Les réponses des futurs élèves sont codées dans un fichier. Le format est le même que dans la SAÉ précédente, excepté que pour chaque élève, il y a maintenant 10 réponses. Un exemple de fichier de réponses est  : 

```
Lisa Fischer:7/4/8/5/7/10/3/7/8/5
Donna Weiss:4/6/2/10/2/10/4/8/7/9
Justin Sanchez:6/5/9/2/2/7/6/7/8/4
```

Définir la fonction `create_answers_from_text_file` prenant en paramètre un nom de fichier contenant les réponses aux questionnaires des élèves. La fonction doit retourner les données contenues dans le fichier. 

**Attention :** comme vous avez progressé en informatique, vous vous êtes rendu compte que la structure de données composée d'un unique tableau contenant toutes les données n'était pas très pratique. Il faut stocker les données dans une autre structure de données. La fonction retournera un dictionnaire dont les clés sont les noms des élèves et les valeurs sont des tableaux de 10 entiers correspondant aux réponses des élèves. Si le fichier de données contient uniquement les données du fichier donné en exemple, l'appel de la fonction doit retourner :
```python
{
    "Lisa Fischer"   : [7, 4, 8, 5, 7, 10, 3, 7, 8, 5],
    "Donna Weiss"    : [4, 6, 2,10, 2, 10, 4, 8, 7, 9],
    "Justin Sanchez" : [6, 5, 9, 2, 2, 7, 6, 7, 8, 4]
}
```

Par la suite, on appellera une *réponse* (*answer* en anglais) un tableau de 10 entiers correspondant aux réponses d'un élève. On appellera *dictionnaire de réponses* un dictionnaire dont les clés sont les noms des élèves et les valeurs leur réponse.

### Question 2

Il s'agit de définir si deux réponses sont proches ! Le professeur Flitwick a lu dans un vieux grimoire que l'on peut utiliser la distance Euclidienne pour mesurer la similarité entre deux réponses. Cela revient à imaginer qu'une réponse est un point d'un espace multidimensionnel (en l'occurrence de dimension 10) et de mesurer la distance entre deux points correspondant à deux réponses ! Comme personne ne comprend rien, il écrit directement la formule mathématique avec sa baguette magique : 

$$
  \sqrt{\sum_{i = 1}^{10} (var_i)^2}  
$$

où $var_i$ représente la différence des deux réponses à la question numéro $i$. Devant les regards ahuris de tous les magiciens, il montre comment calculer la similitude des réponses entre Lisa Fischer et Donna Weiss (en utilisant leurs réponses données en exemple) :

$$
\sqrt{(7-4)^2 + (4 - 6)^2 + (8 - 2)^2 + \dots + (5-9)^2 } = 10.862780491200215
$$


**Remarque :** S'il n'y avait que deux questions dans le questionnaire, alors on pourrait représenter chaque réponse comme un point sur une feuille (espace à deux dimensions avec abscisses et ordonnées) et cette formule correspondrait à la distance entre les deux points sur la feuille. Notez que la valeur retournée est toujours positive ou nulle. Plus cette valeur est faible, plus les réponses aux questions sont similaires. La valeur est nulle si et seulement si les réponses sont identiques.

Définir la fonction `Euclidean_distance` prenant en paramètre deux réponses et retournant la dissimilarité (*i.e.*, différence) entre ces deux réponses en utilisant la formule de la distance Euclidienne. L'appel de la fonction avec comme valeurs de paramètre `[7, 4, 8, 5, 7, 10, 3, 7, 8, 5]` et `[4, 6, 2,10, 2, 10, 4, 8, 7, 9]` (réponses de Lisa et Donna) doit retourner 10.862780491200215.

### Question 3

Les fantômes des fondateurs des maisons ont répondu. Leurs réponses sont stockées dans un tableau de dictionnaires. Chaque case de ce tableau  correspond à une réponse qui est un dictionnaire avec deux clés : `answer` et `house`. La valeur associée à `answer` est une réponse (tableau de 10 entiers) et celle associée à `house` est le nom de la maison à laquelle appartient celui qui a donné cette réponse. Les réponses des fondateurs sont donc stockées sous la forme : 
```python
[   
    {
        "house": "Serpentard", 
        "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]
    },
    {
        "house": "Poufsouffle", 
        "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
    }, 
    {
        "house": "Serdaigle", 
        "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]
    }, 
    {
        "house": "Gryffondor", 
        "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
    } 
]
```

Par la suite, on appellera *ensemble de références* un tel type de tableau, une *référence* correspondant à ce type de dictionnaire.

Définir la fonction `Euclidean_house` prenant en paramètre une réponse et un ensemble de références, et retournant la maison à laquelle affecter l'élève qui a donné cette réponse. La maison est celle de la référence dont la réponse est la plus similaire à celle donnée en paramètre, c'est-à-dire la maison de son *plus proche voisin*. 

Par exemple, l'appel de cette fonction avec la réponse `[9, 4, 5, 3, 9, 2, 5, 1, 8, 2]` et l'ensemble de références donné en exemple retourne `"Gryffondor"` car le plus proche voisin de la réponse est la dernière référence de l'ensemble (distance Euclidienne de 2).

### Question 4

Définir la fonction `Euclidean_repartition` prenant un dictionnaire de réponses et un ensemble de références. La fonction doit retourner un dictionnaire dont les clés sont les noms des élèves et les valeurs la maison où ils ont été affectés avec la méthode de la distance Euclidienne (maison du plus proche voisin).

L'appel de la fonction avec le dictionnaire de réponses donné dans la question 1 et l'ensemble de références donné dans la question 3 doit retourner le dictionnaire suivant :
```python
{
    "Lisa Fischer"   : "Serpentard",
    "Donna Weiss"    : "Serpentard",
    "Justin Sanchez" : "Serdaigle"
}
```

En utilisant la fonction `nb_erreurs`, calculer le pourcentage d'erreur de cette méthode par rapport à la prédiction du choixpeau pour les élèves de première année. On prendra comme ensemble de références celui donné dans le fichier `houses_ref.json`. Les réponses des élèves aux dix questions se trouvent dans le fichier `questionnaire_premiere_annee_10q.txt`.

Cette méthode est-elle meilleure que celle implémentée dans la SAÉ S1.01 ?

### Question 5

Le professeur Binns trouve que les fondateurs, même s'ils représentent bien leur maison respective, ne sont pas suffisants pour complètement représenter l'ensemble de tous les sorciers ayant été affectés à cette maison. Il a donc choisi dans l'histoire de chaque maison les 10 magiciens les plus illustres et a demandé à leur fantôme de répondre au questionnaire. 
L'ensemble des réponses est stocké dans le fichier `houses_multiple_refs.json` (le format est un ensemble de références). Il propose d'appliquer la même méthode mais en prenant comme ensemble de références ces 40 références plutôt que juste les 4 références des fondateurs.

Appliquer la méthode développée précédemment avec ce nouvel ensemble de références change-t-il la précision de la répartition ?


### Question 6


La professeure Gobe-Planche pense que la méthode implémentée est améliorable. En effet, la méthode implémentée consiste à affecter à un élève la maison de son plus proche voisin (*nearest neighbor* en anglais). Cependant, il est possible que le plus proche voisin appartiennent à une maison (par exemple Serdaigle) mais que tous les autres voisins proches appartiennent à une autre maison (par exemple Poufsouffle). Dans ce cas, il est sûrement préférable d'affecter l'élève à la maison Poufsouffle. 

La professeure propose de choisir la maison en fonction de celles des `k` plus proches voisins. L'affectation se fait en deux temps : 

- déterminer un tableau contenant les `k` références (voisins) les plus proches d'un élève ;
- déterminer en fonction de ce tableau dans quelle maison affecter l'élève.

Pour trouver les plus proches voisins, on utilisera une variante du tri par insertion.

Définir la fonction `insertion_position_NN` prenant en paramètre : 
- la réponse d'un élève `answer`,
- une référence `ref`,
- un tableau de références trié du plus proche au moins proche `neighbors`.

La fonction doit retourner l'indice auquel insérer `ref` dans le tableau `neighbors` pour que ce dernier reste trié du plus proche au moins proche.
Si `ref` est moins proche que les autres références du tableau `neighbors`, alors la fonction doit retourner `len(neighbors)`.


**Remarque :** Le tableau de références des fondateurs donné à la Question 3 est trié du plus proche au moins proche par rapport à la réponse `[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]`.

Par exemple, l'appel de la fonction avec comme valeur pour `neigbors` l'ensemble de références des fondateurs donné à la Question 3, et pour `answer` la valeur 
`[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]` doit retourner : 

- 0 si `ref` vaut :
  ```python
  {
    "house": "Serdaigle",
    "answer": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
  }
  ```
- 4 si `ref` vaut :
  ```python
  {
    "house": "Serdaigle",
    "answer": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  }
  ```

En effet, dans le premier cas, `ref` est le plus proche voisin (distance de 0) et doit donc être inséré en début de tableau `neighbors`. Dans le second cas,  `ref` correspond au moins proche voisin et doit donc être inséré après tous les autres.


### Question 7

Définir la fonction `insertion_NN` prenant en paramètre :
- la réponse d'un élève `answer`,
- une référence `ref`,
- un tableau de références trié du plus proche au moins proche `neighbors`,
- un entier `k` tel que `len(neighbors) <= k`.

La fonction ajoute la `ref` dans le tableau `neighbors` au bon endroit, sachant que le tableau `neighbors` doit être de taille au plus `k`. Il faut pour cela  peut-être supprimer un voisin de `neigbors` ou ne pas ajouter la `ref` dans le tableau.

Par exemple, l'appel de la fonction avec comme valeur pour `neigbors` l'ensemble de références des fondateurs donné à la Question 3, pour `answer` la valeur 
`[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]` et pour `ref` la valeur 
```python
  {
    "house": "Serdaigle",
    "answer": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  }
```
doit ajouter `ref` à la fin du tableau `neighbors` uniquement si `k` a une valeur supérieure ou égale à 5.

### Question 8

Définir la fonction `NN` prenant en paramètre la réponse d'un élève, un tableau de références et un entier `k` et retournant un tableau des `k` plus proches voisins triés du plus proche au moins proche.

Par exemple, l'appel de la fonction avec la réponse `[2, 1, 5, 6, 8, 2, 4, 3, 5, 9]`, le tableau de références des fondateurs donné à la Question 3 et la valeur 2 pour l'entier doit retourner le tableau : 
```python
[
    {
        'house': 'Poufsouffle', 
        'answer': [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
    }, 
    {
        'house': 'Gryffondor', 
        'answer': [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
    }
]
```
car la distance Euclidienne des fondateurs est respectivement de 13.38, 10.20, 14.93 et 11.70 (valeurs arrondies à deux décimales).


### Question 9

Définir la fonction `NN_house` prenant en paramètre un tableau de voisins `neighbors` et retournant la maison d'affectation de l'élève dont `neighbors` représente les plus proches voisins. La règle est la suivante : on retourne la maison la plus fréquente parmi celles des voisins. En cas d'égalité, parmi les maisons les plus fréquentes, on retourne celle correspondant au plus proche voisin. 

Par exemple, l'appel de la fonction doit retourner :
- `"Gryffondor"` si `neighbors` vaut :
  ```python
  [   
    {
        "house": "Serpentard", 
        "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]
    },
    {
        "house": "Gryffondor", 
        "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
    }, 
    {
        "house": "Serdaigle", 
        "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]
    }, 
    {
        "house": "Gryffondor", 
        "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
    } 
  ]
  ```
  puisque deux voisins sont de Gryffondor,
- `"Serpentard"` si `neighbors` vaut :
  ```python
  [   
    {
        "house": "Serpentard", 
        "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]
    },
    {
        "house": "Gryffondor", 
        "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]
    }, 
    {
        "house": "Serdaigle", 
        "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]
    }, 
    {
        "house": "Gryffondor", 
        "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]
    },
    {
        "house": "Serpentard", 
        "answer": [8, 6, 6, 10, 8, 5, 5, 6, 7, 8]
    } 
 
  ]
  ```
  puisque Serpentard et Gryffondor sont les maisons les plus fréquentes parmi les     voisins et que le plus proche voisin parmi ces deux maisons est un voisin de Serpentard.

**Remarque :** Pour cette question, on n'a pas besoin de regarder les réponses des voisins car on sait qu'ils sont classés du plus proche au moins proche.


### Question 10

Définir la fonction `NN_repartition` prenant un dictionnaire de réponses, un ensemble de références et un entier `k`. La fonction doit retourner un dictionnaire dont les clés sont les noms des élèves et les valeurs la maison où ils ont été affectés avec la méthode des `k` plus proches voisins.


En utilisant la fonction `nb_erreurs`, calculer le pourcentage d'erreur de cette méthode avec les valeurs 1 à 5 pour `k` par rapport à la prédiction du choixpeau. L'une de ces méthodes est-elle meilleure que les précédentes ? Pour quelle valeur de `k` ?


