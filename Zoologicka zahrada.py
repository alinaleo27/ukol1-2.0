#Zvire
from dataclasses import dataclass

@dataclass
class Zvire:
    jmeno: str
    druh: str
    vaha: int

    def __str__(self):
        return f"Zvire {self.name} je {self.druh} a vazi {self.vaha} Kg. Vitej v nasi zahrade!"

    def export_to_dict(self):
        return {'jmeno': self.jmeno, 'druh': self.druh, 'vaha': self.vaha}

ruzenka = Zvire('Růženka', 'Panda Velká', 150)
vilda = Zvire('Vilda', 'Vydra Mořská', 20)
matysek = Zvire('Matýsek', 'Tygr Sumaterský', 300)
karlik = Zvire('Karlík', 'Lední medvěd', 700)

zviratka_dict = [ruzenka, vilda, matysek, karlik]
for zviratko in zviratka_dict:
    print(zviratko.export_to_dict())


#Zamestnanec
@dataclass
class Zamestnanec:
    cele_jmeno: str
    rocni_plat: int
    pozice: str

    def __str__(self):
        return f"{self.cele_jmeno} vydelava za rok {self.rocni_plat} a je na pozici {self.pozice}"
    
    def ziskej_inicialy(self):
       inicialy = self.cele_jmeno.split()
       return f"{inicialy[0][0]}.{inicialy[1][0]}."
    
    def export_to_dict(self):
        return {'jmeno': self.cele_jmeno, 'rocni_plat': self.rocni_plat, 'pozice': self.pozice}

Terka = Zamestnanec('Tereza Vysoka', 700_000, 'Cvicitelka tygru')
Anet = Zamestnanec('Anet Krasna', 600_000, 'Cvicitelka vyder')
Martin = Zamestnanec('Martin Velky', 650_000, 'Cvicitel lednich medvedu')

zamestnancy_dict = [Terka, Anet, Martin]
for zamestnanec in zamestnancy_dict:
    print(zamestnanec.export_to_dict())


#Reditel
class Reditel(Zamestnanec):
    def __init__(self, cele_jmeno, rocni_plat, pozice='Reditel', oblibene_zvire=Zvire):
        super().__init__(cele_jmeno, rocni_plat, pozice)
        self.oblibene_zvire = oblibene_zvire

zvire = Zvire('Adolf', 'Tarantule Velká', 0.1)
reditel = Reditel(cele_jmeno='Karel', rocni_plat=800_000, oblibene_zvire=zvire)
assert reditel.pozice == 'Reditel'
assert isinstance(reditel.oblibene_zvire, Zvire)


#Zoo
@dataclass
class Zoo:
    jmeno: str
    adresa: str
    reditel: Reditel
    zamestnanci: Zamestnanec
    zvirata: Zvire

    def vaha_vsech_zvirat_v_zoo(self):
        total_weight = 0
        for vaha in zviratka_dict:
            total_weight += self.vaha

zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', reditel, Terka, ruzenka)

print(zoo.reditel)
print('Celková váha zvířat v ZOO:', zoo.vaha_vsech_zvirat_v_zoo())
print('Měsíční náklady na zaměstnance:', zoo.mesicni_naklady_na_zamestnance())
    