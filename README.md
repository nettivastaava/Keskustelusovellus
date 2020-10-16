Linkki Herokuun: https://tsoha-chat-app.herokuapp.com/

Palautus 1:

Sovellukseni idea on kurssimateriaalissa annettua esimerkkiä mukaileva keskustelusovellus, jossa tulee olemaan seuraavat toiminnallisuudet:

    • Uuden käyttäjän rekisteröiminen ja sisäänkirjautuminen
    
    • Uuden viestiketjun lisääminen
    
    • Viestiketjuun kommentoiminen
    
    • Tykkäyksen antaminen viestille
    
    • Käyttäjäprofiilien selaaminen sekä mahdollisuus estää toinen käyttäjä (tällöin käyttäjät eivät näe toistensa aloittamia viestiketjuja)
    

Lisäksi mahdollisuus viestien lisäämiseen ja tykkäysten antamiseen edellyttää sovellukseen kirjautumista. Viestejä pääsee kuitenkin lukemaan kuka tahansa.

Palautus 2:

Tässä vaiheessa sovelluksessa on alustavasti toteutettu kaikki muut toiminnallisuudet, paitsi käyttäjän estäminen ja mahdollisuus profiilien selaamiseen. Myös jo toteutetuissa toiminnallisuuksissa on vielä paranneltavaa. Esimerkiksi tällä hetkellä käyttäjä ei pysty perumaan tykkäystään eikä poistamaan lähettämiään viestejä. Myös syötteiden validointi on osin kesken (Käyttäjä pystyy esimerkiksi lähettämään tyhjiä viestejä). Näiden puutteiden lisäksi sovelluksen ulkoasu kaipaa vielä hiomista.

Palautus 3:

Tässä vaiheessa sovellus on pääpiirteittäin valmis. Syötteiden validointiin on kiinnitetty enemmän huomiota eikä käyttäjän enää pitäisi pystyä lähettämään tyhjiä lomakkeita. Myös sovelluksen nagivointia on helpotettu lisäämällä oikean ylälaidan TCA-tekstiin linkki pääsivulle. 
	Sovelluksesta tuli pitkälti sellainen kuin ensimmäinen viikon palautuksessa suunnittelinkin. Harkinnan jälkeen päädyin kuitenkin tekemään joihinkin toiminnallisuuksiin pieniä muutoksia. Esimerkiksi käyttäjän blockaaminen estää ainoastaan tätä kommentoimasta tai antamasta tykkäystä estäjän viestiketjuihin. Koska sovelluksen idea on, että rekisteröitymätönkin käyttäjä voi selata viestiketjuja, olisi alkuperäinen toteutus ollut sangen tehoton. Päädyin myös lisäämään sovellukseen toiminnallisuuksia, joita en ollut listannut alkuperäiseen suunnitelmaani. Tällaisia lisäyksiä olivat mm. hakutoiminnallisuus käyttäjien etsimiseen sekä mahdollisuus poistaa oma viestiketju. 
	Koska sovelluksessa on vain 5 tietokantataulua, ajattelin vielä lisätä sovellukseen taulun “tags”, keskustelun tunnisteet, joiden perusteella viestiketjuja on helpompi seuloa. Tavoitteena on myös karsia turhaa koodia pois sekä siistä html-pohjia luettavampaan muotoon.

Lopullinen palautus:

Sovelluksen lopulliseen versioon ei nähdäkseni jäänyt mitään suurempia vikoja. Viimeisimmässä palautuksessa esiintynyt ongelma, joka aiheutui /-merkkejä sisältävästä käyttäjänimestä, on nyt korjattu sallimmalla käyttäjänimeen pelkästään kirjaimia ja numeroita. Sovelluksen ulkoasu on ehkä hieman mitäänsanomaton, mutta mielestäni kuitenkin yhtenevä jokaisella sivulla.
	Varsinaisia lisäyksiä sovellukseen tuli enää vähän. Uusiin toiminnallisuuksiin lukeutuvat kuitenkin keskusteluntunnisteet sekä mahdollisuus poistaa oma kommentti viestiketjusta. Suunnitelmani mukaisesti myös siistin koodia ja parantelin SQL-kyselyjä hakemaan vain tarvittavaa tietoa.
