# Bändisovellus #

Sovelluksesta löytyy eri bändejä, joista jokaisesta voi lukea tietopaketin. Bändeistä löytyy myös arvosteluja, ja niistä voi koota suosikkilistan. Käyttäjärooleja on peruskäyttäjä ja ylläpitäjä.

***Sovelluksesta:***

- Mahdollisuus kirjautua sisään ja ulos sekä luoda uusi käyttäjä. Uutta käyttäjää luodessa käyttäjänimen tulee olla 3-15 merkkiä pitkä, ja salasanan 5-20 (sovellus kyllä ilmoittaa tästä).

- Sovelluksen avautuessa käyttäjä näkee listan bändeistä. Bändiä alla olevista painikkeista klikkaamalla näytetään tietopaketti bändistä sekä sen saamat arvostelut.

- Käyttäjä voi myös itse antaa bändistä arvion.

- Käyttäjä voi joko lisätä tai poistaa bändin suosikkilistalta.

- Ylläpitäjä voi lisätä bändin (ja samalla tietopaketin), sekä poistaa yksittäisen käyttäjän arvostelun.

- Etusivulla bändit näkyvillä aakkosjärjestyksessä.

# Käynnistysohjeet #

Sovellusta voi testata käynnistämällä se paikallisesti

1. Kloonaa tämän sovelluksen repositorio koneellesi ja mene juurikansioon

2. Luo .env-tiedosto ja lisää sinne seuraavat kohdat:

- DATABASE_URL=postgresql:///sansilla

- SECRET_KEY=<tänne oma secret key>

3. Aktivoi virtuaaliympäristö ja riippuvuudet seuraavilla komennoilla:

- python3 -m venv venv

- source venv/bin/activate

- pip install -r ./requirements.txt

4. Määritä tietokannan taulukot komennolla:

- psql < tables.sql

- Huom! Halutessasi voit myös luoda oman tietokannan sovellusta varten ja lisätä taulukot sinne. Tämä onnistuu seuraavalla tavalla:

    - psql

    - CREATE DATABASE sansilla

    - psql -d sansilla < tables.sql

5. Saat sovelluksen käynnistettyä komennolla:

- flask run

# Nykytilanne & testaus: #

- Sovelluksen kaikki listatut toiminnot toimivat.

- CSS otettu käyttöön ja ulkoasua siistitty.

- "Uuden ihmisen" testatessa (eli avatessa sovellusta ensimmäistä kertaa) taulukoita luodessa tietokantaan lisätään automaattisesti yksi bändi ja infopaketti bändistä parilla erillisellä sql-komennolla.
