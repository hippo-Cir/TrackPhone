
# Localisation de Numéros de Téléphone

Ce programme permet de trouver la localisation géographique de numéros de téléphone mobile en utilisant les services de Phonenumbers et OpenCage Geocoder. Il crée également des cartes interactives avec Folium pour visualiser les localisations trouvées.

## Prérequis

Avant d'exécuter ce programme, assurez-vous d'avoir installé les bibliothèques Python nécessaires en utilisant `pip` :

```bash
pip install phonenumbers folium opencage
```

## Configuration

Assurez-vous d'avoir une clé API valide pour OpenCage Geocoder. Vous pouvez obtenir une clé en vous inscrivant sur leur [site web](https://opencagedata.com/).

Enregistrez cette clé dans le fichier `main.py` :

```python
key = 'VOTRE_CLÉ_API_ICI'
```

## Utilisation

1. Créez un fichier `myphone.py` contenant une liste de numéros de téléphone à localiser :

```python
# myphone.py

numbers = [
    "+33633476732",
    # Ajoutez d'autres numéros si nécessaire
]
```

2. Exécutez le script `main.py` :

```bash
python main.py
```

Le programme affichera la localisation de chaque numéro dans la console et générera un fichier HTML pour chaque localisation avec une carte interactive.

## Remarque

- Assurez-vous d'utiliser ce programme de manière responsable et conforme aux lois et réglementations locales concernant la confidentialité et l'utilisation des données personnelles.
```

Ce README explique les prérequis, la configuration, l'utilisation et contient également une remarque sur l'utilisation responsable du programme. Vous pouvez bien sûr le personnaliser davantage en fonction de vos besoins spécifiques.
