import sqlite3

DB_ADI = "restoran.db"


def baglanti_kur():
    """ RDBMS yapılarda her istek (request) için veri tabanı oturumu yeniden oluşturulur. """
    return sqlite3.connect(DB_ADI)


def db_hazirla():
    """ Tablolar yoksa oluşturur. """
    with baglanti_kur() as baglanti:
        baglanti.execute(
            'CREATE TABLE IF NOT EXISTS menu (id INTEGER PRIMARY KEY AUTOINCREMENT, isim TEXT NOT NULL, aciklama TEXT, kategori TEXT NOT NULL, fiyat REAL NOT NULL, gorsel_yolu TEXT)')
    baglanti.close()


def menuyu_getir():
    """ menu tablosunda kayıtlı tüm yemekleri getirecektir. """
    with baglanti_kur() as baglanti:
        imlec = baglanti.cursor()
        imlec.execute("SELECT * FROM menu")
        menu = imlec.fetchall()
    baglanti.close()
    return menu


def ekle(isim, kategori, fiyat, gorsel_yolu, aciklama=None):
    with baglanti_kur() as baglanti:
        baglanti.execute("INSERT INTO menu (isim, aciklama, kategori, fiyat, gorsel_yolu) VALUES (?,?,?,?,?)",
                         (isim, aciklama, kategori, fiyat, gorsel_yolu))
    baglanti.close()


def sil(menu_id):
    with baglanti_kur() as baglanti:
        baglanti.execute("DELETE FROM menu WHERE id = ?", (menu_id))
    baglanti.close()
