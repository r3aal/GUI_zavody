import tkinter as tk

celkovy_cas_kola_1 = 0
pocet_zavodniku = 0
vsichni_zavodnici = []
    
with open("zavody/vysledky.txt", encoding = "utf-8") as vysledky:
        for radek in vysledky:
            radek = radek.strip()
            if not radek:
                continue

            casti = radek.split("#")

            zavodnik = {
                "jmeno": casti[0],
                "dokoncil": casti[1],
                "kolo_1": int(casti[2]),
                "kolo_2": int(casti[3]),
                "kolo_3": int(casti[4])
            }

            if zavodnik["dokoncil"] == "ano":
                dokoncil_zavod = True

            else:
                dokoncil_zavod = False

            celkovy_cas = zavodnik["kolo_1"]+zavodnik["kolo_2"]+zavodnik["kolo_3"]

            zavodnik["dokoncil_zavod"] = dokoncil_zavod
            zavodnik["celkovy_cas"] = celkovy_cas   #vytvori nove promenne do slovniku a uklada kazdy udaj
            vsichni_zavodnici.append(zavodnik)  #slouci vsechny udaje zavodnika do jedne promenne

            celkovy_cas_kola_1 += zavodnik["kolo_1"]
            pocet_zavodniku += 1

        def otevri_okno_prumeru():
            okno_prumeru = tk.Toplevel(okno)
            okno_prumeru.title("průměr závodníků")
            okno_prumeru.geometry("435x600")

            for zavodnik in vsichni_zavodnici:
                vypis = tk.Label(
                    okno_prumeru,
                    text=f"{zavodnik['jmeno']}: {zavodnik["celkovy_cas"]} sekund"
                )
                vypis.pack(anchor="w", padx=15, pady=2)
                
            if pocet_zavodniku > 0:
                prumer = celkovy_cas_kola_1 / pocet_zavodniku
                vypis_prumeru = tk.Label(
                    okno_prumeru,
                    text=f"\nPrůměrný čas za 1. kolo: {prumer} sekund"
                )
                vypis_prumeru.pack(anchor="w", padx=15, pady=10)

        def otevri_okno_nedokoncencu():
            okno_nedokoncencu = tk.Toplevel(okno)
            okno_nedokoncencu.title("závodníci, co nedokončili závod")
            okno_nedokoncencu.geometry("435x200")
                
            for zavodnik in vsichni_zavodnici:
                if zavodnik["dokoncil_zavod"] == False:
                    vypis = tk.Label(
                        okno_nedokoncencu,
                        text=f"{zavodnik['jmeno']}:{zavodnik["kolo_1"]} s"
                    )
                    vypis.pack(anchor="w", padx=15, pady=2)

        okno = tk.Tk()
        okno.title("odpovědi")
        okno.geometry("435x100")

        tlacitko_prumer = tk.Button(okno, text = "Průměry časů", command = otevri_okno_prumeru)
        tlacitko_prumer.place(x = 50, y = 30)

        tlacitko_nedokoncenci = tk.Button(okno, text = "Závodníci, co nedokončili závod", command = otevri_okno_nedokoncencu)
        tlacitko_nedokoncenci.place(x = 200, y = 30)

        okno.mainloop()