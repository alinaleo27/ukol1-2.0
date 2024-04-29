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
        return f"{self.cele_jmeno} vydelava za rok {self.rocni_plat}, a je na pozicí {self.pozice}"
    
    def ziskej_inicialy(self):
       inicialy = self.cele_jmeno.split()
       return f"{inicialy[0][0]}.{inicialy[1][0]}."
    
    def export_to_dict(self):
        return {'jmeno': self.cele_jmeno, 'rocni_plat': self.rocni_plat, 'pozice': self.pozice}

Terka = Zamestnanec('Tereza Vysoka', 700_000, 'Cvičitelka tygru')
Anet = Zamestnanec('Anet Krasna', 600_000, 'Cvičitelka vyder')
Martin = Zamestnanec('Martin Velky', 650_000, 'Cvičitel ledních medvedů')

print(Anet)

zamestnancy_dict = [Terka, Anet, Martin]
for zamestnanec in zamestnancy_dict:
    print(zamestnanec.export_to_dict())


#Reditel
class Reditel(Zamestnanec):
    def __init__(self, cele_jmeno, rocni_plat, pozice='Reditel', oblibene_zvire=Zvire):
        super().__init__(cele_jmeno, rocni_plat, pozice)
        self.oblibene_zvire = oblibene_zvire
    
    def __str__(self):
        return super().__str__() + f" - je to boss."

zvire = Zvire('Adolf', 'Tarantule Velká', 0.1)
reditel = Reditel(cele_jmeno='Karel', rocni_plat=800_000, oblibene_zvire=zvire)
assert reditel.pozice == 'Reditel'
assert isinstance(reditel.oblibene_zvire, Zvire)


#Zoo
class Zoo:
    def __init__(self, jmeno, adresa, reditel=Reditel, zamestnanci=[Zamestnanec], zvirata=[Zvire]):
        self.jmeno = jmeno
        self.adresa = adresa
        self.reditel = reditel
        self.zamestnanci = zamestnanci
        self.zvirata = zvirata

    def vaha_vsech_zvirat_v_zoo(self):
        total_weight = 0
        for one in zviratka_dict:
            if hasattr(one, 'vaha'):
                total_weight += one.vaha
        return f'{total_weight} Kg.'

    def mesicni_naklady_na_zamestnance(self):
        monthly = 0
        for one in zamestnancy_dict:
            if hasattr(one, 'rocni_plat'):
                monthly += one.rocni_plat
        monthly01 = monthly + reditel.rocni_plat
        monthly02 = monthly01 / 12
        return f'činí {round(monthly02, 2)} Kc'

zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', reditel, Zamestnanec, Zvire)

print(zoo.reditel)
print('Celková váha zvířat v ZOO: ', zoo.vaha_vsech_zvirat_v_zoo())
print('Měsíční náklady na zaměstnance:', zoo.mesicni_naklady_na_zamestnance())