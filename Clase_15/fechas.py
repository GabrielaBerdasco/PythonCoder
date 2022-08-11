from datetime import datetime


def cumpleaños(mes, dia) :
    dt = datetime.now()

    dif_meses = mes - dt.month
    dif_dias = dia - dt.day

    print(dif_dias, dif_meses)
    print(dif_dias * 86400)
    print(dif_meses * 2.628e+6)
    segundos = (dif_dias * 86400) + (dif_meses * 2.628e+6)

    return segundos


seg_cumpleaños = cumpleaños(12, 16)

print(seg_cumpleaños)