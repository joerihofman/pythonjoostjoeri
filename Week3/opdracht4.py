"""
try:
    statement1
    statement2
    statement3
except Exception1:
    # Handle exception
except Exception2:
    # Handle exception
except Exception3:
    # Handle exception
finally:
    statement4

statement5

a) Stel statement2 'werpt' een exceptie, wordt statement 3 dan nog uitgevoerd ?
Nee, na een exception wordt de opdracht afgebroken

b) Stel dat de exceptie niet wordt 'gevangen', wordt statement 4 dan ook uitgevoerd ? En hoe zit het dan met
statement 5 ?
statement 4 wordt uitgevoerd en statement 5 wordt sowieso uitgevoerd omdat die buiten de try staat

c) Stel dat de exceptie van het type Exception2 is, wordt statement 4 dan ook uitgevoerd ? En hoe zit het dan
met statement 5 ?
Statement 4 wordt niet uitgevoerd, statement 5 wel

"""