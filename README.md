# Afsluttende-eksamen
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