class CompteBancaire:
    def __init__(self, nom, sold=0.0):
        self.nom_pro = nom
        self.sold = sold
    
    def depose(self, montant):
        if montant > 0:
            print('montant ajouter', montant)
        else:
            print('montant no ajoute')
            
    def retirer(self,  montant):
        if montant > 0:
            if self.sold >= montant:
                print('monatnt retirer:', montant)
            else:
                print('sold is not enough')
    
    def afficher_solde(self):
        print('le nom du propriétaire:', self.nom)
        print('le solde actuel:', self.sold)
        
compte1 = CompteBancaire('sikou', 10000)
compte1.depose(500)
compte1.retirer(20000)
compte1.afficher_solde()