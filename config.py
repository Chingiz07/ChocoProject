from down_att import names, attachment_dir
import pandas as pd

kaspiname = attachment_dir + '/' + 'Kaspi17.04.2018.xls'
qazkomname = attachment_dir + '/' + '13318-EC27_12_12_merchantrep_17.04.2018-17.04.2018.htm'
rpsname = attachment_dir + '/' + 'RPS_20180409.xls'
processingname = attachment_dir + '/' + 'Chocotravel Отчет по транзакциям за 20180405.xls'

def kaspi(filename):
    k = 'Kaspi'
    df = pd.read_excel(filename)
    date = df["Дата транзакции"].dt.normalize()
    order_ID = df["Номер бронирования"]
    return date, order_ID, k

def qazkom(filename):
    q = 'QazKom'
    df = pd.read_html(filename)[-1]
    names = df.iloc[0].values.tolist()
    df = pd.DataFrame.from_records(data=df.values[1:], columns=names)
    date = df["Post Date"]
    date = pd.to_datetime(date)
    order_ID = df["Ret Ref Number"]
    return date, order_ID, q

def rps(filename):
    r = 'RPS'
    df = pd.read_excel(filename, skiprows = 1, skipfooter=1)
    date = df["Дата"]
    order_ID = df["Номер брони"]
    return date, order_ID, r

def processing(filename):
    p = 'Processing.kz'
    df = pd.read_excel(filename, skiprows=4)
    date = df["AlmDate"]
    order_ID = df["Order ID"]
    return date, order_ID, p


print(processing(processingname))