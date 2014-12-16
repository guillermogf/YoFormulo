#!/usr/bin/python
# coding: utf-8

# 2014 © Guillermo Gómez Fonfría <guillermo.gf@openmailbox.org>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib2
import json
import sys


def search(busqueda):
    busqueda = urllib2.quote(busqueda)
    searchraw = urllib2.urlopen("http://www.yoformulo.com/api/index.php?action"
                                "=search&str=" + busqueda).read()
    searchlist = json.loads(searchraw)
    return searchlist


def getData(id_num):
    dataraw = urllib2.urlopen("http://yoformulo.com/api/index.php?action=get"
                              "Data&str=" + id_num).read()
    data = json.loads(dataraw)
    return data


def main():
    busqueda = raw_input("Compuesto a buscar: ")
    searchlist = search(busqueda)
    if len(searchlist) == 0:
        print("No se econtraron resultados")
        sys.exit(1)
    elif len(searchlist) > 1:
        n = 0
        for i in searchlist:
            print("[" + str(n) + "] " + i["formula"])
            n = n + 1
        while True:
            select = raw_input("Elije: ")
            try:
                select = int(select)
                if not select > n - 1:
                    break
                else:
                    print("Debe ser un número de los listados")
            except:
                print("Debe ser un número de los listados")
    else:
        select = 0
    num_id = searchlist[select]["id"]

    data = getData(num_id)
    print(u"Fórmula: " + data[0]["formula"])
    print(u"Sistemática: " + data[0]["sistematica"])
    print(u"Stock: " + data[0]["stock"])
    print(u"Tradicional: " + data[0]["tradicional"])
    cat = data[0]["key"]
    if cat == "oxidometalico":
        cat = "Óxido metálico"
    elif cat == "oxidonometalico":
        cat = "Óxido no metálico"
    elif cat == "halurodeoxigeno":
        cat = "Haluro de oxígeno"
    elif cat == "peroxido":
        cat = "Peróxido"
    elif cat == "hidrurometalico":
        cat = "Hidruro metálico"
    elif cat == "hidruronometalico":
        cat = "Hidruro no metálico"
    elif cat == "hidroxido":
        cat = "Hidróxido"
    elif cat == "halurodehidrogenooacidohidracido":
        cat = "Ácido hidrácido"
    elif cat == "acidooxacido":
        cat = "Ácido oxácido"
    elif cat == "acidooxacido":
        cat = "Ácido oxácido"
    elif cat == "salbinaria":
        cat = "Sal binaria"
    elif cat == "salternaria":
        cat = "Sal ternaria"
    elif cat == "salacida":
        cat = "Sal ácida"
    else:
        cat = str(cat)
    print("Categoría: " + cat)

main()
