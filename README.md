# Gestionnaire de Fichiers

Une application console simple permettant d'explorer les répertoires, sélectionner des fichiers et effectuer des opérations basiques (copier, déplacer, supprimer).

## Prérequis

- Python 3.x installé sur votre système
- Windows, Linux, ou MacOS

## Structure du Projet

```
gestionnaire-fichiers/
│
├── interfaces.py      # Interfaces abstraites pour les opérations sur les fichiers
├── file_system.py    # Implémentation concrète des opérations système
├── file_explorer.py  # Navigation et exploration des répertoires
├── file_selector.py  # Fonctionnalité de sélection des fichiers
├── file_manager.py   # Logique métier principale
├── console_ui.py     # Interface utilisateur console
└── README.md         # Ce fichier
```

## Installation

1. Assurez-vous que Python 3.x est installé sur votre système
2. Clonez ou téléchargez ce dépôt
3. Vérifiez que tous les fichiers sont dans le même répertoire

## Utilisation

1. Ouvrez un terminal/invite de commande
2. Naviguez vers le répertoire du projet
3. Lancez l'application avec l'une de ces commandes :

```bash
# Méthode standard
python console_ui.py

# Ou avec le chemin Python explicite sous Windows
C:\Users\[VotreUtilisateur]\AppData\Local\Programs\Python\Python3x\python.exe console_ui.py
```

## Fonctionnalités

L'application propose les fonctionnalités suivantes :

1. Affichage du contenu du répertoire courant
2. Navigation dans les répertoires
3. Retour au répertoire parent
4. Sélection multiple de fichiers
5. Copie des fichiers sélectionnés
6. Déplacement des fichiers sélectionnés
7. Suppression des fichiers sélectionnés

## Options du Menu

- **1. Afficher Répertoire** : Montre le contenu du répertoire actuel
- **2. Naviguer** : Entrer dans un répertoire par son index
- **3. Répertoire Parent** : Remonter d'un niveau
- **4. Sélectionner Fichiers** : Choisir des fichiers par leurs indices (séparés par des virgules)
- **5. Copier** : Copier les fichiers sélectionnés vers une destination
- **6. Déplacer** : Déplacer les fichiers sélectionnés vers une destination
- **7. Supprimer** : Supprimer les fichiers sélectionnés
- **8. Quitter** : Fermer l'application

## Exemple d'Utilisation

```
--- Explorateur de Fichiers ---
1. Afficher Répertoire
2. Naviguer
3. Répertoire Parent
4. Sélectionner Fichiers
5. Copier
6. Déplacer
7. Supprimer
8. Quitter

Votre choix : 1
0. 📁 Dossier : Documents
1. 📄 Fichier : exemple.txt
2. 📁 Dossier : Images

Votre choix : 4
Entrez les indices des fichiers à sélectionner (séparés par des virgules) : 1
Fichiers sélectionnés :
 - exemple.txt

Votre choix : 5
Entrez le chemin de destination pour la copie : C:\Sauvegarde
```

## Architecture

L'application suit les principes SOLID et utilise l'injection de dépendances :

- **Interfaces** : Définissent les contrats abstraits pour les opérations sur les fichiers
- **FileSystem** : Implémente les opérations réelles sur le système de fichiers
- **FileExplorer** : Gère la navigation dans les répertoires
- **FileSelector** : Gère la sélection des fichiers
- **FileManager** : Orchestre les opérations entre les composants
- **Console UI** : Fournit l'interface utilisateur

## Gestion des Erreurs

L'application inclut la gestion des erreurs pour :
- Entrées utilisateur invalides
- Erreurs système de fichiers
- Erreurs de navigation
- Problèmes de permissions

## Contribution

N'hésitez pas à soumettre des problèmes et des demandes d'amélioration !

## Licence

Ce projet est open source et disponible sous la [Licence MIT](LICENSE).