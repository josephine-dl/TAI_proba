
vp = int(input("entrer le nombre de vrai positif : "))
vn = int(input("entrer le nombre de vrai négatif : "))
fp = int(input("entrer le nombre de faux positif : "))
fn = int(input("entrer le nombre de faux négatif : "))

se = vp/(vp+fn) # sensibilite
sp = (vn)/(vn+fp) # specificite
pr= (vp+fn)/(vp+vn+fp+fn)  # prevalence
vpp = vp/(vp+fp)  # valeur prédictive positive 
vpn = vn/(vn +fn) # valeur prédictive négative 
print ("sensibilité : ",se, "sepcificité : ",sp,"prévalence ",pr)
print ("valeur prédictive positive :", vpp, "valeur prédictive négative :",vpn)