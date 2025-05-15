# Afsluttende-eksamen
# V.2 //// 15/05/2025
- DENNE VERSION ER TESTET OG ER FUNKTIONEL MED EN UNDTAGELSE
- klokkeslæt for målinger er 2 timer for tidlige
- updated index.html med fejlrettelser til visning af data
- updated app.py med diverse fejlrettelser, bl.a. angående visning af data
- tilføjet clear_db.py til at rense dataen. dette script er oprettet med henblik på test, og en rensning inden den endelige eksaminations data bliver taget
- updated subscriber.py med fejlrettelser til indsættelse af data
- updated arduino script så den ikke sender tid, da vi har valgt at droppe RTC. Dette er grundet at vi alligevel ikke logger noget, så skulle raspberry pi miste forbindelse med internettet, vil alt data gå tabt alligevel. Af den årsag kan vi lige så godt bruge Azure serverens egen tid.
# V.2 //// 14/05/2025
- DENNE VERSION ER INDTIL VIDERE UTESTET OG KUN LAVET TEORETISK. TESTES DEN 15/05/2025 OG OPDATERES TIL V.3
- updated index.html for at også vise gyro data i tabellen
- updated pi_sender.py til at send faktisk data fra arduino sensorer, istedet for random data
- updated subscriber.py for at tage højde for de nye data der bliver sendt, da gyro ikke var inkluderet før og derfor mangler i tabellen.
# V.1 //// 13/05/2025
- updated diverse navne på objekter i koden så der ikke kommer fejl.
- denne version af opsætningen virker uden problemer OBS: DENNE OPSÆTNING BRUGER FIKTIV DATA OG IKKE RÉEL DATA FRA ARDUINO
- pi_sender.py køres på raspberry pi.
- samlet.ino køres på Arduino
- subscriber.py, app.py samt templates mappe ligger på azure VM som en del af webappen.
- init_users.py & requirements.txt skal teknisk set kun benyttes til opsætning og ikke videre brug.