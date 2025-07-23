from typing import Optional

from core.enums.direction_enum import DirectionEnum
from core.models.city import City
from core.models.point import Point
from core.static.country_names import CountryNames


class CityNames:
    CITY_AMSTERDAM = 'Amsterdam'
    CITY_ANGORA = 'Angora'
    CITY_ATHINA = 'Athina'
    CITY_BARCELONA = 'Barcelona'
    CITY_BERLIN = 'Berlin'
    CITY_BREST = 'Brest'
    CITY_BRINDISI = 'Brindisi'
    CITY_BRUXELLES = 'Bruxelles'
    CITY_BUCURESTI = 'Bucuresti'
    CITY_BUDAPEST = 'Budapest'
    CITY_CADIZ = 'Cadiz'
    CITY_CONSTANTINOPLE = 'Constantinople'
    CITY_DANZIG = 'Danzig'
    CITY_DIEPPE = 'Dieppe'
    CITY_EDINBURGH = 'Edinburgh'
    CITY_ERZURUM = 'Erzurum'
    CITY_ESSEN = 'Essen'
    CITY_FRANKFURT = 'Frankfurt'
    CITY_KHARKOV = 'Kharkov'
    CITY_KOBENHAVN = 'Kobenhavn'
    CITY_KYIV = 'Kyiv'
    CITY_LISBOA = 'Lisboa'
    CITY_LONDON = 'London'
    CITY_MADRID = 'Madrid'
    CITY_MARSEILLE = 'Marseille'
    CITY_MOSKVA = 'Moskva'
    CITY_MUNCHEN = 'Munchen'
    CITY_PALERMO = 'Palermo'
    CITY_PAMPLONA = 'Pamplona'
    CITY_PARIS = 'Paris'
    CITY_PETROGRAD = 'Petrograd'
    CITY_RIGA = 'Riga'
    CITY_ROMA = 'Roma'
    CITY_ROSTOV = 'Rostov'
    CITY_SARAJEVO = 'Sarajevo'
    CITY_SEVASTOPOL = 'Sevastopol'
    CITY_SMOLENSK = 'Smolensk'
    CITY_SMYRNA = 'Smyrna'
    CITY_SOCHI = 'Sochi'
    CITY_SOFIA = 'Sofia'
    CITY_STOCKHOLM = 'Stockholm'
    CITY_VENEZIA = 'Venezia'
    CITY_WARSZAWA = 'Warszawa'
    CITY_WIEN = 'Wien'
    CITY_WILNO = 'Wilno'
    CITY_ZAGRAB = 'Zagrab'
    CITY_ZURICH = 'Zurich'

    CITIES = {
        CITY_AMSTERDAM: City(CITY_AMSTERDAM, CountryNames.COUNTRY_NETHERLANDS, Point(x=642, y=427)),
        CITY_ANGORA: City(CITY_ANGORA, CountryNames.COUNTRY_TURKEY, Point(x=1663, y=1210), DirectionEnum.SOUTH_EAST,
                          edge_point=True),
        CITY_ATHINA: City(CITY_ATHINA, CountryNames.COUNTRY_GREECE, Point(x=1289, y=1214)),
        CITY_BARCELONA: City(CITY_BARCELONA, CountryNames.COUNTRY_SPAIN, Point(x=442, y=1141)),
        CITY_BERLIN: City(CITY_BERLIN, CountryNames.COUNTRY_GERMANY, Point(x=972, y=466)),
        CITY_BREST: City(CITY_BREST, CountryNames.COUNTRY_FRANCE, Point(x=275, y=645), DirectionEnum.NORTH_WEST,
                         edge_point=True),
        CITY_BRINDISI: City(CITY_BRINDISI, CountryNames.COUNTRY_ITALY, Point(x=1069, y=1065)),
        CITY_BRUXELLES: City(CITY_BRUXELLES, CountryNames.COUNTRY_BELGIUM, Point(x=603, y=516)),
        CITY_BUCURESTI: City(CITY_BUCURESTI, CountryNames.COUNTRY_ROMANIA, Point(x=1430, y=872)),
        CITY_BUDAPEST: City(CITY_BUDAPEST, CountryNames.COUNTRY_HUNGARY, Point(x=1160, y=739)),
        CITY_CADIZ: City(CITY_CADIZ, CountryNames.COUNTRY_SPAIN, Point(x=231, y=1267), DirectionEnum.SOUTH_WEST,
                         edge_point=True),
        CITY_CONSTANTINOPLE: City(CITY_CONSTANTINOPLE, CountryNames.COUNTRY_TURKEY, Point(x=1525, y=1113)),
        CITY_DANZIG: City(CITY_DANZIG, CountryNames.COUNTRY_POLAND, Point(x=1176, y=314)),
        CITY_DIEPPE: City(CITY_DIEPPE, CountryNames.COUNTRY_FRANCE, Point(x=442, y=588)),
        CITY_EDINBURGH: City(CITY_EDINBURGH, CountryNames.COUNTRY_ENGLAND, Point(x=348, y=137),
                             DirectionEnum.NORTH_WEST, edge_point=True),
        CITY_ERZURUM: City(CITY_ERZURUM, CountryNames.COUNTRY_TURKEY, Point(x=1810, y=1171), DirectionEnum.SOUTH_EAST,
                           edge_point=True),
        CITY_ESSEN: City(CITY_ESSEN, CountryNames.COUNTRY_GERMANY, Point(x=785, y=439)),
        CITY_FRANKFURT: City(CITY_FRANKFURT, CountryNames.COUNTRY_GERMANY, Point(x=761, y=572)),
        CITY_KHARKOV: City(CITY_KHARKOV, CountryNames.COUNTRY_UKRAINE, Point(x=1778, y=660)),
        CITY_KOBENHAVN: City(CITY_KOBENHAVN, CountryNames.COUNTRY_DENMARK, Point(x=918, y=240), DirectionEnum.NORTH,
                             edge_point=True),
        CITY_KYIV: City(CITY_KYIV, CountryNames.COUNTRY_UKRAINE, Point(x=1544, y=557)),
        CITY_LISBOA: City(CITY_LISBOA, CountryNames.COUNTRY_PORTUGAL, Point(x=105, y=1171), DirectionEnum.SOUTH_WEST,
                          edge_point=True),
        CITY_LONDON: City(CITY_LONDON, CountryNames.COUNTRY_ENGLAND, Point(x=460, y=420)),
        CITY_MADRID: City(CITY_MADRID, CountryNames.COUNTRY_SPAIN, Point(x=235, y=1125)),
        CITY_MARSEILLE: City(CITY_MARSEILLE, CountryNames.COUNTRY_FRANCE, Point(x=695, y=956)),
        CITY_MOSKVA: City(CITY_MOSKVA, CountryNames.COUNTRY_RUSSIA, Point(x=1805, y=370), DirectionEnum.NORTH_EAST,
                          edge_point=True),
        CITY_MUNCHEN: City(CITY_MUNCHEN, CountryNames.COUNTRY_GERMANY, Point(x=877, y=662)),
        CITY_PALERMO: City(CITY_PALERMO, CountryNames.COUNTRY_ITALY, Point(x=986, y=1269), DirectionEnum.SOUTH,
                           edge_point=True),
        CITY_PAMPLONA: City(CITY_PAMPLONA, CountryNames.COUNTRY_SPAIN, Point(x=411, y=964)),
        CITY_PARIS: City(CITY_PARIS, CITY_PARIS, Point(x=531, y=675)),
        CITY_PETROGRAD: City(CITY_PETROGRAD, CountryNames.COUNTRY_RUSSIA, Point(x=1629, y=141),
                             DirectionEnum.NORTH_EAST,
                             edge_point=True),
        CITY_RIGA: City(CITY_RIGA, CountryNames.COUNTRY_LATVIA, Point(x=1326, y=150)),
        CITY_ROMA: City(CITY_ROMA, CountryNames.COUNTRY_ITALY, Point(x=914, y=1012)),
        CITY_ROSTOV: City(CITY_ROSTOV, CountryNames.COUNTRY_RUSSIA, Point(x=1857, y=760)),
        CITY_SARAJEVO: City(CITY_SARAJEVO, CountryNames.COUNTRY_BAH, Point(x=1206, y=979)),
        CITY_SEVASTOPOL: City(CITY_SEVASTOPOL, CountryNames.COUNTRY_UKRAINE, Point(x=1678, y=898)),
        CITY_SMOLENSK: City(CITY_SMOLENSK, CountryNames.COUNTRY_RUSSIA, Point(x=1655, y=416)),
        CITY_SMYRNA: City(CITY_SMYRNA, CountryNames.COUNTRY_TURKEY, Point(x=1440, y=1267), DirectionEnum.SOUTH_EAST,
                          edge_point=True),
        CITY_SOCHI: City(CITY_SOCHI, CountryNames.COUNTRY_RUSSIA, Point(x=1848, y=931), DirectionEnum.SOUTH_EAST,
                         edge_point=True),
        CITY_SOFIA: City(CITY_SOFIA, CountryNames.COUNTRY_BULGARIA, Point(x=1326, y=993)),
        CITY_STOCKHOLM: City(CITY_STOCKHOLM, CountryNames.COUNTRY_SWEDEN, Point(x=1111, y=94), DirectionEnum.NORTH,
                             edge_point=True),
        CITY_VENEZIA: City(CITY_VENEZIA, CountryNames.COUNTRY_ITALY, Point(x=899, y=843)),
        CITY_WARSZAWA: City(CITY_WARSZAWA, CountryNames.COUNTRY_POLAND, Point(x=1271, y=448)),
        CITY_WIEN: City(CITY_WIEN, CountryNames.COUNTRY_AUSTRIA, Point(x=1071, y=692)),
        CITY_WILNO: City(CITY_WILNO, CountryNames.COUNTRY_LITHUANIA, Point(x=1471, y=405)),
        CITY_ZAGRAB: City(CITY_ZAGRAB, CountryNames.COUNTRY_CROATIA, Point(x=1050, y=868)),
        CITY_ZURICH: City(CITY_ZURICH, CountryNames.COUNTRY_SWITZERLAND, Point(x=755, y=782))
    }

    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")

    @classmethod
    def get(cls, city_name: str) -> Optional[City]:
        if city_name in cls.CITIES:
            return cls.CITIES[city_name]
        return None
