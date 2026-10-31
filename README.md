# Fraud Detection MLOps – TP1 : Maîtrise de Git

**Étudiante :** Meriam Ben Ali

## Réponses aux questions

### Partie 1

**4. Comment vérifier la configuration actuelle de Git sur votre machine, notamment le nom d'utilisateur et l'adresse e-mail ?**
```bash
git config --list          
git config user.name     
git config user.email     
```

**5. Comment modifier votre adresse e-mail si vous l'avez mal configurée lors de l'installation de Git ?**

Il suffit de relancer la commande avec la bonne adresse : la nouvelle valeur remplace l'ancienne.
```bash
git config --global user.email "nouvelle.adresse@exemple.fr"
```

### Partie 2

**6. Si vous avez oublié de créer un fichier README.md lors de l'initialisation du projet, comment pouvez-vous l'ajouter après coup et committer les changements ?**
```bash
echo "# Fraud Detection MLOps" > README.md
git add README.md
git commit -m "Ajout du README"
git push origin main
```

**7. Comment définir un dépôt distant si vous n'en avez pas configuré un lors de la création du projet ?**
```bash
git remote add origin git@github.com:meriembena/fraud-detection-mlops.git
git remote -v                
git push -u origin main    
```

### Partie 3

**3. Comment annuler les modifications locales d'un fichier avant de les ajouter à l'index ?**
```bash
git restore eda.py
```
Le fichier revient à l'état du dernier commit. Les modifications sont perdues définitivement.

**4. Comment visualiser les fichiers qui sont prêts à être committés dans Git (staging) ?**
```bash
git status       
git diff --staged  
```

### Partie 4

**4. Comment suivre (track) un dépôt distant et récupérer toutes les branches de ce dépôt ?**
```bash
git fetch --all                        
git branch -a                           
git checkout --track origin/experiment-eda   
git branch -vv         
```

**5. Comment supprimer une branche locale après l'avoir fusionnée dans master ?**
```bash
git branch -d experiment-eda            
git push origin --delete experiment-eda    
```

### Partie 5

**8. Comment interrompre un rebase en cours si vous avez commis une erreur ?**
```bash
git rebase --abort
```

**9. Comment lister les commits qui vont être rebasés avant de lancer un rebase ?**
```bash
git log main..experiment-eda --oneline
```