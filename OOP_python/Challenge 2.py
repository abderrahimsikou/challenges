from abc import ABC, abstractmethod

class Personne(ABC):
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    
    @abstractmethod
    def afficher_infos(self):
        pass

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule
        self.notes = []
    
    def ajouter_note(self, note):
        if 0 <= note <= 20:
            self.notes.append(note)
        else:
            raise ValueError("La note doit être entre 0 et 20")
    
    def moyenne(self):
        if not self.notes:
            return 0
        return sum(self.notes) / len(self.notes)
    
    def afficher_infos(self):
        return f"Étudiant: {self.prenom} {self.nom}, Âge: {self.age}, Matricule: {self.matricule}, Moyenne: {self.moyenne():.2f}"

class Enseignant(Personne):
    def __init__(self, nom, prenom, age, specialite, salaire):
        super().__init__(nom, prenom, age)
        self.specialite = specialite
        self._salaire = salaire
    
    @property
    def salaire(self):
        return self._salaire
    
    @salaire.setter
    def salaire(self, valeur):
        if valeur < 0:
            raise ValueError("Le salaire ne peut pas être négatif")
        self._salaire = valeur
    
    def afficher_infos(self):
        return f"Enseignant: {self.prenom} {self.nom}, Âge: {self.age}, Spécialité: {self.specialite}, Salaire: {self.salaire} DH"

class Ecole:
    def __init__(self, nom):
        self.nom = nom
        self.liste_etudiants = []
        self.liste_enseignants = []
    
    def ajouter_etudiant(self, etudiant):
        self.liste_etudiants.append(etudiant)
        
    def ajouter_enseignant(self, enseignant):
        self.liste_enseignants.append(enseignant)
        
    def afficher_tous_les_membres(self):
        print(f"Membres de l'école {self.nom} ===")
        for enseignant in self.liste_enseignants:
            print(" - " + enseignant.afficher_infos())
        