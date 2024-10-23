from TikTokApi import TikTokApi
import random
api = TikTokApi()

tiktoker_tags = ["sonosempreiris","alessia_basile_","iriss.vallaranii", "aliseabruno","martina_os", "bunnybunny924","777.siria_","elisa.radulescu","lisa_luchetta","lucreziagrande_"]
class TikToker:
    ELO = 1500
    def __init__(self, tag):
        self.tag = tag
tiktokers = []
for tiktoker in tiktoker_tags:
    tiktokers.append(TikToker(tiktoker))

for x in range(10):
    s = tiktokers[random.randint(0,len(tiktokers)-1)]
    d = tiktokers[random.randint(0,len(tiktokers)-1)]
    expected_s = 1/ (1+10**((d.ELO - s.ELO)/400))
    expected_d = 1/ (1+10**((s.ELO - d.ELO)/400))
    vincitrice = input(f"Preferiresti: \n(S) {s.tag} o {d.tag} (D)")
    vincitrice = vincitrice.lower()
    K = 32
    if vincitrice == "d":
        d.ELO += K*(1-expected_d)
        s.ELO += K*(0-expected_s)
    if vincitrice == "s":
        d.ELO += K*(0-expected_d)
        s.ELO += K*(1-expected_s)
tiktokers.sort(key= lambda x: x.ELO, reverse=True)
for num, tiktoker in enumerate(tiktokers):
    print(f"{num+1}a: {tiktoker.tag}, ELO: {tiktoker.ELO}")