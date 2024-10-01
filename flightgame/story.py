import textwrap

story = '''Vuosi on 2040. Teknologinen kehitys on muuttanut ilmailualaa radikaalisti, ja lentorahtikuljetukset ovat nousseet tärkeäksi osaksi kansainvälistä taloutta. Sinä olet nuori ja kunnianhimoinen lentäjä, joka on perustanut oman kuljetusyhtiön. Maailmanlaajuiset yhtiöt ja yksityisasiakkaat luottavat sinuun kiireellisten ja arvokkaiden rahtien kuljetuksessa, sillä taitosi ja tehokkuutesi ovat vertaansa vailla.

Kuitenkin maailma on muuttunut. Ilmasto-olosuhteet ovat arvaamattomampia, ja lentokentät kilpailevat keskenään suotuisista reiteistä ja ilmatiloista. Jokainen matka on riskialtis, ja sinä olet vastuussa siitä, että tärkeät rahtilähetykset saapuvat määränpäähänsä turvallisesti ja ajallaan.

Pelissä sinulle annetaan erilaisia tehtäviä ja rahtipaketteja kuljetettavaksi. Jokainen lähetys voi olla kriittinen: joskus kuljetat harvinaista lääkettä, toisinaan valtavan arvokasta taideteosta tai hätäapupaketteja luonnonkatastrofialueille.
'''

# Set column width to 80 characters
wrapper = textwrap.TextWrapper(width=80, break_long_words=False, replace_whitespace=False)
# Wrap text
word_list = wrapper.wrap(text=story)


def getStory():
    return word_list