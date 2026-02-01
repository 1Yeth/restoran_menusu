import streamlit as st

from src import database, views


def run():
    st.set_page_config("Restoran Menü Sistemi", "📜")
    database.db_hazirla()

    st.sidebar.title("Gezinti")
    secim = st.sidebar.radio("Sayfalar",["Menü Ekranı","Yönetim Paneli"])
    if secim == "Yönetim Paneli":
        views.yonetim_sayfasi()
    elif secim == "Menü Ekranı":
        views.menu_sayfasi()


if __name__ == "__main__":
    run()
