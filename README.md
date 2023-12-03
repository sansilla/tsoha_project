# Bändisovellus #

Sovelluksesta löytyy eri bändejä, joista jokaisesta voi lukea tietopaketin. Bändeistä löytyy myös arvosteluja, ja niistä voi koota suosikkilistan. Käyttäjärooleja on peruskäyttäjä ja ylläpitäjä.

***Sovelluksesta:***

- Mahdollisuus kirjautua sisään ja ulos sekä luoda uusi käyttäjä.

- Sovelluksen avautuessa käyttäjä näkee listan bändeistä. Bändiä klikkaamalla näytetään tietopaketti bändistä sekä sen saamat arvostelut.

- Käyttäjä voi myös itse antaa bändistä arvion.

- Käyttäjä voi joko lisätä tai poistaa bändin suosikkilistalta.

- Ylläpitäjä voi 	~~poistaa tai~~ lisätä bändin (ja samalla tietopaketin), sekä poistaa yksittäisen käyttäjän arvostelun.

- ~~Etusivulta voi hakea bändiä nimeltä.~~

- Etusivulla bändit näkyvillä aakkosjärjestyksessä.

# Käynnistysohjeet #

Sovellusta voi testata käynnistämällä se paikallisesti

1. Kloonaa tämän sovelluksen repositorio koneellesi ja mene juurikansioon

2. Luo .env-tiedosto ja lisää sinne seuraavat kohdat:

- DATABASE_URL=postgresql:///sansilla

- SECRET_KEY=488be107d7e30f0c63d1c95b1b18494a

3. Aktivoi virtuaaliympäristö ja riippuvuudet seuraavilla komennoilla:

- pip install -r ./requirements.txt

- python3 -m venv venv

- source venv/bin/activate

4. Määritä tietokannan taulukot komennolla:

- psql < tables.sql

5. Saat sovelluksen käynnistettyä komennolla:

- flask run

# Nykytilanne & testaus: #

- Sovelluksen kaikki listatut toiminnot toimivat.

- Sovelluksen ulkoasuun tulossa vielä mahdollisesti muutosta.

- "Uuden ihmisen" testatessa (eli avatessa sovellusta ensimmäistä kertaa) ei etusivulla vielä ole bändejä, mutta oletettavasti ylläpitäjän luotua niitä voi lisätä. Luultavasti tulen lisäämään pari sql-komentoa, jotka täyttää tietokantaan valmiiksi jotain tietoa.

- Koodi on vielä hieman siistimistä vailla.
