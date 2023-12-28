def temizlik():
    metin="WikiLeaks (/ˈwɪkiliːks/) is a media organisation and publisher founded in 2006. It operates as a non-profit and is funded by donations[13] and media partnerships. It has published classified documents and other media provided by anonymous sources.[14] It was founded by Julian Assange, an Australian editor, publisher, and activist, who is currently challenging extradition to the United States over his work with WikiLeaks.[15] Since September 2018, Kristinn Hrafnsson has served as its editor-in-chief.[16][17] Its website states that it has released more than ten million documents and associated analyses.[18] WikiLeaks' most recent publication was in 2021, and its most recent publication of original documents was in 2019.[19] Beginning in November 2022, many of the documents on the organisation's website could not be accessed.[19][20][21][22]"
    tirnak=(metin.count(";"))-1
    metin2=metin.replace(";","",tirnak)
    soruisareti=(metin2.count("?"))-1
    metin2=metin2.replace("?","",soruisareti)
    nokta=(metin2.count("."))-1
    metin2=metin2.replace(".","",nokta)
    print(metin2)

temizlik()