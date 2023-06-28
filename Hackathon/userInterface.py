import terminal
import animals
from turtle import *


def draw_window():
    """

    PreCondition: turtle at origin
    PostCondition: turtle at origin + penup + facing North
    """

    speed(0)
    screensize(200, 200)
    pensize(10)
    goto(0, 400)
    left(180)
    forward(400)
    left(90)
    forward(800)
    left(90)
    forward(400)
    left(90)
    forward(400)
    pensize(2)
    penup()


def country_Choice():
    country = terminal.question_country()
    if country.lower() == "india":
        color("orange")
        write("India", font=("Arial", 65, "normal"))
        color("black")
        penup()
        pendown()
        animals.india(25, -400)
    if country.lower() == "china":
        color("Red")
        write("China", font=("Arial", 65, "normal"))
        color("black")
        animals.panda(25, -400)
    if country.lower() == "mexico":
        color("Green")
        write("Mexico", font=("Arial", 65, "normal"))
        color("black")
        animals.mexico(25, -400)
    return country


def china(china_info):
    if china_info.lower() == "traditions":
        goto(-365, 200)
        write("Today we will be \nlearning about the most\n famous festivals & \ncelebrations in China.",
              font=("Arial", 25, "bold"))
        goto(-380, -310)
        write(
            "China has many traditions \nand celebrations throughout the\n year. Some are Chinese\n New Year, the lantern \n"
            "festival, Qingming festival, \ndragon boat festival, double seventh day, \nmid-autumn festival, \n"
            "winter solstice, summer solstice, \ndouble ninth, and the hungry ghost \nfestival. To explain a few, \n"
            "Chinese New Year is the\n beginning of the new chinese calendar \nyear, the lantern festival is the last "
            "day\n "
            "of the Chinese New Year period,\n Qingming is the day for people \nto visit graves and pay respect to \n"
            "ancestors, and the mid-autumn festival\n is to worship the moon \nand eat mooncakes.\n ",
            font=("Arial", 20, "normal"))
        goto(25, 0)
        write("For more information about \nthis topic, here are some \nbooks you can reference! \nEncyclopedia of "
              "Contemporary Chinese Culture   \nby Edward Lawrence Davis\nPoPo's Lucky Chinese New Year   by Virginia "
              "Loh-Hagan\nEducation as Cultivation in \nChinese Culture   \nby Shihkuan Hsu, Yuh-Yin Wu "
              "\n---------------------\nThank you for your interest \nin learning more about \nChina's traditions!",
              font=("Arial",
                    20,
                    "normal"))
        terminal.china_traditions()
    elif china_info.lower() == "history":
        goto(-365, 200)
        write("Today we will be learning \nabout how China came to be.", font=("Arial", 25, "bold"))
        goto(-380, -310)
        write(
            "China was ruled by various dynasties \n for much of its history. \n"
            "The first dynasty is believed to be the Xia \n"
            "dynasty which formed somewhere \n around 2250 BC. During the \n Qing dynasty, western influences, \n"
            "European trade, and a \n number of wars all served to \n weaken China. Great Britain gained \n "
            "control of Hong Kong\n "
            "after the Opium Wars. \n In the early 1900s the \n people of China began to "
            "\n want reform. Revolutionary leader \n"
            "Sun Yat-sen created the \n Chinese Nationalist Peoples Party, \n"
            "also called the KMT or \n Kuomintang.Mao Zedong \n"
            "established the Peoples Republic\n of China on October 1, 1949.",
            font=("Arial", 20, "normal"))
        goto(25, 0)
        write("For more information\n about this topic, \nhere are some books you can\n reference!\nChina: A New Cultural "
              "History   by Cho-yun Hsu\nA History of Chinese Civilization   \nby Jacques Gernet \nA Brief History of "
              "China: Dynasty, Revolution \nand Transformation   \nby Jonathan Clements\n --------------------\nThank you "
              "for your interest \nin learning more about China's history!", font=("Arial", 20, "normal"))
        terminal.china_history()
    elif china_info.lower() == "food":
        goto(-365, 200)
        write("Today we will be learning \nabout the most popular \ncuisines and snacks in China.",
              font=("Arial", 25, "bold"))
        goto(-380, -310)
        write(
            "Regarded as the soul of \nthe Chinese dish, taste \ncan be divided into five classes\n - sweet, sour, bitter,\n "
            "hot and salty. Seasoning\n such as soy sauce, sugar, \nvinegar and salt in proper\n amount and in different \n"
            "sequences, contribute to the\n taste of the dish. In \nthe vast land of China, \nthere are eating habits of \n"
            "'South-Sweet, North-Salty, East-Hot\n and West-Sour' according to the \ndifferent tastes of \nthe people. Those\n "
            "in southern China like \nto add more sugar when \ncooking than others.", font=("Arial", 20, "normal"))
        goto(25, 0)
        write("For more information\n about this topic, here a\nre some books you can reference!\nThe Food of China   by "
              "E.N. Anderson\nGlobalization of Chinese Food   \nby Sidney Cheung, David Y.H. Wu\nThe Land of the Five "
              "Flavors: A Cultural \nHistory of Chinese Cuisine    \nby Thomas O. Hollmann\n----------------\n Thank you "
              "for your interest \nin learning more about China's food!",
              font=("Arial", 20, "normal"))
        terminal.china_food()


def india(india_info):
    if india_info.lower() == "traditions":
        goto(-365, 200)
        write("Today we will be learning \nabout the most popular \ncuisines and snacks in India.",
              font=("Arial",25, "bold"))
        goto(-380, -380)
        write("India is full of different\n cultures and so there\n are multitudes of traditions.\n A few popular ones are \n"
              "Diwali, Navaratri, Onam,\n Holi, Christmas, Dussehra,\n Durga Puja, Janmashtmi,\n Eid, Raksha Bandhan, Pongal, \n"
              "Lodhi, and so much more.\nTo expand on a few,\n Diwali is the festival\n of lights, Onam is the \nfestival of \n"
              "harvest, Holi is the \nfestival of colors, Janmashtmi\n is the birth of the \nlord Krishna, Eid marks\n the end of \n"
              "Ramadan, Raksha Bandhan \nis the bond of protection\n usually for siblings, and\n Lodhi is the punjabi Folk \n"
              "Festival.", font=("Arial", 20, "normal"))
        goto(25, 0)
        write("For more information about\n this topic, here are some\n books you can reference!\n "
              "Land of the Festivals:\n An Introduction to Indian Culture and Tradition\n   by Kumar Keswani Discover India:\n"
              " Festivals of India   \nby Sonia Mehta\n "
              "Festival Stories:\n Through the Year   \nby Rachna Chhabria \n ------------------\n"
              "Thank you for your interest \nin learning more about\n India's traditions!",
              font=("Arial", 20, "normal"))
        terminal.india_traditions()
    elif india_info.lower() == "history":
        goto(-365, 200)
        write("Today we will be learning\n about how India \ncame to be.",font=("Arial", 25, "bold"))
        goto(-380, -400)
        write("There is evidence, from \nthe earliest times, of \ngreat movements of peoples across South Asia, \n"
              "sometimes replacing existing \n populations, sometimes integrating with \nthem. They came from West and Central \n"
              "Asia in massive sweeps \nthrough the lofty passes\n in the northwest, bringing \nwith them the rudiments of the \n"
              "Hindu faith, later to\n be developed on Indian soil\n into a subtle and highly complex \nreligion. Other \n"
              "religions, such as \nBuddhism, Islam, Christianity \nand Zoroastrianism, have developed \nand been absorbed into \n"
              "India’s proverbial sponge.\nOf all the Europeans who came \nto trade in India, it was the\n British who ruled, \n"
              "making the Subcontinent \nthe “jewel in the crown” of their empire. \nSuccessive campaigns finally led to \n"
              "Indian independence in 1947. \nToday, with a burgeoning economy \ncompeting on the world stage, \n"
              "India’s democracy is a \ntriumph in a land of multiple \nethnic, religious and secessionist interests.\n"
              , font=("Arial", 16, "normal"))
        goto(25, 0)
        write(
            "-------------------------\n For more information about\n this topic, here are some\n books you can reference!\n "
            "Incarnations: \nA History of India in 50 Lives\n   by Sunil Khilnani\n India After Gandhi:\n The History of the "
            "World's \nLargest Democracy\n   by Ramachandra Guha\n India: A History \n  by John Keay \n"
            "---------------------\n Thank you for your interest\n in learning more about\n India's history!"
            , font=("Arial", 20, "normal"))
        terminal.india_history()
    elif india_info.lower() == "food":
        goto(-365, 200)
        write("Today we will be learning \nabout the most popular \ncuisines and snacks in India.",
              font=("Arial", 25, "bold"))
        goto(-380, -370)
        write(
            "The staple Indian foods are \nRice, Wheat and Lentils. \nAnd no Indian dish is complete\n"
            " without spices. Indian \n"
            "food is a combination of all \nsix tastes like sweet, \nsour, salty, bitter, spicy \nand astringent. In India \n"
            "different dishes are prepared \nfor different festivals. Every \nfestival tends to be \ncomplete only "
            "when \n "
            "special "
            "food associated with \nthat festival is cooked on \nthat day. Another delicious item cooked \nhere is the ‘Saag‘ that is \n"
            "prepared with a green leafy\n vegetable known as the ‘Hak‘.\n Besides chapatis other closely \n"
            "related breads baked in \nthese regions include \nTandoori, Rumaali and Naan etc.\n However in the northern \n"
            "region "
            "impact of Mughlai food \nis quite obvious.", font=("Arial", 16, "normal"))
        goto(25, 0)
        write("----------------------------- \nFor more information about \nthis topic, "
              "here are some\n books you can reference!\n Season: Big Flavors,\n Beautiful Food \n  by Nik Sharma\n "
              "A Historical Dictionary\n of India Food  \n by K.T.\n Achaya Feasts and Fasts: \nA History of Food in India\n "
              "  by Colleen Taylor Sen\n------------------------\nThank you for your \ninterest in learning \n"
              "more about India's food!", font=("Arial", 20, "normal"))
        terminal.india_food()


def mexico(mexico_info):
    if mexico_info.lower() == "traditions":
        goto(-365, 200)
        write("Today we will be learning \nabout the most famous \nfestivals and celebrations \nin Mexico.",
              font=("Arial", 25, "bold"))
        goto(-380, -400)
        write(
            "Mexico has a lot of fun\n and interesting traditions and\n celebrations. A few include \nDia de Los Muertos,\n "
            "Las Posadas, Bull Fighting,\n Siestas, Cinco de Mayo, \nand Pinatas. To explain a few, \nDia de Los Muertos is \n"
            "the day of the dead \nwhere people honor dead friends\n and family with all night\n vigils, Las Posadas is meant \n"
            "to commemorate Joseph and \nMary making their way to \nBethlehem, bull fighting is a big \nsport in Mexico, \n"
            "siestas are short naps \nthat are taken in the early \nafternoon in Mexico, and Cinco \nde Mayo commemorates \n"
            "Mexico's victory over France.",
            font=("Arial", 20, "normal"))
        goto(25, 0)
        write("For more information about this\n topic, here are some books\n you can reference!\n The Human Tradition in Mexico\n "
              "  by Jeffrey M. Pilcher\n Mexican Culture\n   by Lori McManus\n Cultural Traditions in Mexico\n   by Lynn Peppas \n"
              "------------------------- \n Thank you for your interest\n in learning more about\n Mexico's traditions!",
              font=("Arial", 20, "normal"))
        terminal.mexico_traditions()
    elif mexico_info.lower() == "history":
        goto(-365, 220)
        write("Today we will be learning\n about how Mexico came to be.", font=("Arial", 25, "bold"))
        goto(-380, -400)
        write(
            "A country rich in history,\n tradition and culture, Mexico\n is made up of 31 states \nand one federal district. \n"
            "It is the third largest country\n in Latin America and has\n one of the largest\n populations—more than 100 \n"
            "million—making it the\n home of more Spanish speakers \nthan any other nation in the\n world. Despite the \n"
            "political and social \nchanges that have occurred\n over the centuries, evidence of \npast cultures and events \n"
            "are apparent everywhere\n in Mexico. Many of Mexico’s \nrural areas are still \ninhabited by indigenous people \n"
            "whose lifestyles are quite\n similar to those of their \nancestors. In addition, many \npre-Columbian ruins \n"
            "still exist throughout\n Mexico, including the ancient\n city of Teotihuacán and the Mayan\n pyramids at Chichén\n"
            "Itzá and Tulum. Reminders of \nthe colonial past are evident \nin the architecture of towns \nlike Taxco and \n"
            "Querétaro.",
            font=("Arial", 16, "normal"))
        goto(25, 0)
        write("-----------------------\n For more information about\n this topic, here are some \nbooks you can reference!\n "
              "The Oxford History of Mexico\n   by William Beezley\n Mexican History\n   by Nora E. Jaffary\n The Great Book of"
              " Mexico\n   by Bill O'Neill\n -----------------------\n Thank you for your interest \nin "
              "learning more about\n Mexico's history!",
              font=("Arial", 20, "normal"))
        terminal.mexico_history()
    elif mexico_info.lower() == "food":
        goto(-365, 200)
        write("Today we will be learning \nabout the most popular \ncuisines and snacks in \nMexico.", font=("Arial", 25, "bold"))
        goto(-380, -350)
        write(
            "Among the staples of Mexican\n food are beans and corn. \nCorn is used to make masa, \na dough that is then \n"
            "turned into tortillas and \ntamales, whereas beans and \ncorn feature prominently in many\n dishes.Mexican \n"
            "cooking is packed with \nflavour; among the herbs \nand spices that give it its \ndistinct kick are a variety of\n "
            "chillies (fresh, dried, \nsmoked and pickled), alongside\n oregano, coriander (known \nas cilantro in North \n"
            "America), cinnamon and cocoa.\n Garlic, onions, lemons and \nlimes are also used generously.",
            font=("Arial", 20, "normal"))
        goto(25, 0)
        write("For more information about this \ntopic, here are some books\n you can reference! \nPlanet Taco: A "
              "Global History of Mexican Food   \nby Jeffrey M. Pilcher\nThe Book of Mexican Foods   by Christine "
              "Barret\nTaco USA: How Mexican Food Conquered America   \nby Gustavo Arellano\n---------------\nThank you "
              "for your interest \nin learning more about Mexico's food!", font=("Arial", 20, "normal"))
        terminal.mexico_food()


def country_info(country):
    if country.lower() == "china":
        china_info = terminal.country_knowledge_question()
        china(china_info)
    elif country.lower() == "india":
        india_info = terminal.country_knowledge_question()
        india(india_info)
    elif country.lower() == "mexico":
        mexico_info = terminal.country_knowledge_question()
        mexico(mexico_info)


def user_interface():
    draw_window()
    goto(-310, 325)
    right(90)
    country = country_Choice()
    penup()
    goto(-310, 315)
    country_info(country)


def main():
    tracer(n=0, delay=None)
    user_interface()
    done()


if __name__ == "__main__":
    main()
