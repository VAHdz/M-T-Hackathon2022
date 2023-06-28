def question_country():
    country = input("What country do you want to learn about? (India, Mexico, or China): ")
    return country


def country_knowledge_question():
    question1 = input("What do you want to learn more about?(traditions, history, or food): ")
    return question1.lower()


def india_traditions():
    input("Thank you for your interest in learning more about India's traditions!(press enter to keep going)")
    print("-------------------------------------------------------")
    input("Today we will be learning about the most famous festivals and celebrations in India. (press enter to keep "
          "going)")
    print("-------------------------------------------------------")
    input("India is full of different cultures and so there are multitudes of traditions. A few popular ones are \n"
          "Diwali, Navaratri, Onam, Holi, Christmas, Dussehra, Durga Puja, Janmashtmi, Eid, Raksha Bandhan, Pongal, \n"
          "Lodhi, and so much more.To expand on a few, Diwali is the festival of lights, Onam is the festival of \n"
          "harvest, Holi is the festival of colors, Janmashtmi is the birth of the lord Krishna, Eid marks the end of \n"
          "Ramadan, Raksha Bandhan is the bond of protection usually for siblings, and Lodhi is the punjabi Folk \n"
          "Festival.\n (press enter to keep going))")
    print("For more information about this topic, here are some books you can reference!")
    print("Land of the Festivals: An Introduction to Indian Culture and Tradition   by Kumar Keswani")
    print("Discover India: Festivals of India   by Sonia Mehta")
    print("Festival Stories: Through the Year   by Rachna Chhabria")
    print("-------------------------------------------------------")
    print("Thank you for your interest in learning more about India's traditions!")
    user_input = input("Would you like to take a quiz? yes/no")
    if user_input.lower() == "yes":
        india_quiz()
    else:
        print("Have a nice day!")
        quit()


def india_history():
    input("Thank you for your interest in learning more about India's history!(press enter to keep going)")
    print("-------------------------------------------------------")
    input("Today we will be learning about how India came to be.(press enter to keep going)")
    print("-------------------------------------------------------")
    input("There is evidence, from the earliest times, of great movements of peoples across South Asia, \n"
          "sometimes replacing existing populations, sometimes integrating with them. They came from West and Central \n"
          "Asia in massive sweeps through the lofty passes in the northwest, bringing with them the rudiments of the \n"
          "Hindu faith, later to be developed on Indian soil into a subtle and highly complex religion. Other \n"
          "religions, such as Buddhism, Islam, Christianity and Zoroastrianism, have developed and been absorbed into \n"
          "India’s proverbial sponge.Of all the Europeans who came to trade in India, it was the British who ruled, \n"
          "making the Subcontinent the “jewel in the crown” of their empire. Successive campaigns finally led to \n"
          "Indian independence in 1947. Today, with a burgeoning economy competing on the world stage, \n"
          "India’s democracy is a triumph in a land of multiple ethnic, religious and secessionist interests.\n"
          " (press enter to keep going)")
    print("-------------------------------------------------------")
    print("For more information about this topic, here are some books you can reference!")
    print("Incarnations: A History of India in 50 Lives   by Sunil Khilnani")
    print("India After Gandhi: The History of the World's Largest Democracy   by Ramachandra Guha")
    print("India: A History   by John Keay")
    print("-------------------------------------------------------")
    print("Thank you for your interest in learning more about India's history!")
    user_input = input("Would you like to take a quiz? yes/no")
    if user_input.lower() == "yes":
        india_quiz()
    else:
        print("Have a nice day!")
        quit()


def india_food():
    input("Thank you for your interest in learning more about India's food! (press enter to keep going)")
    print("-------------------------------------------------------")
    input("Today we will be learning about the most popular cuisines and snacks in India.(press enter to keep going)")
    input(
        "The staple Indian foods are Rice, Wheat and Lentils. And no Indian dish is complete without spices. Indian \n"
        "food is a combination of all six tastes like sweet, sour, salty, bitter, spicy and astringent. In India \n"
        "different dishes are prepared for different festivals. Every festival tends to be complete only when \n"
        "special "
        "food associated with that festival is cooked on that day. Like Holi can not be complete without Gujhiya and \n"
        "Eid without Sewai. India is the only country in the world where there is Unity in Diversity not only its \n"
        "culture & religion but also its cuisine.Food in the north India, to begin with, Kashmiri cuisines reflect\n"
        "strong Central Asian influences. In Kashmir, mostly all the dishes are prepared around the main course of \n"
        "rice found abundantly in the beautiful valley. Another delicious item cooked here is the ‘Saag‘ that is \n"
        "prepared with a green leafy vegetable known as the ‘Hak‘.But on the other hand states like the Punjab, \n"
        "Haryana and Uttar Pradesh show high consumption of chapatis as staple food. Again, these chapatis are \n"
        "prepared with a variety of flours such as wheat, rice, maida, besan etc. Besides chapatis other closely \n"
        "related breads baked in these regions include Tandoori, Rumaali and Naan etc. However in the northern \n"
        "region "
        "impact of Mughlai food is quite obvious. \n(press enter to keep going)")
    print("-------------------------------------------------------")
    print("For more information about this topic, here are some books you can reference!")
    print("Season: Big Flavors, Beautiful Food   by Nik Sharma")
    print("A Historical Dictionary of India Food   by K.T. Achaya")
    print("Feasts and Fasts: A History of Food in India   by Colleen Taylor Sen")
    print("-------------------------------------------------------")
    print("Thank you for your interest in learning more about India's food!")
    user_input = input("Would you like to take a quiz? yes/no")
    if user_input.lower() == "yes":
        india_quiz()
    else:
        print("Have a nice day!")
        quit()


def china_traditions():
    input("Thank you for your interest in learning more about China's traditions!(press enter to keep going)")
    print("-------------------------------------------------------")
    input("Today we will be learning about the most famous festivals and celebrations in China. (press enter to keep "
          "going)")
    print("-------------------------------------------------------")
    input("China has many traditions and celebrations throughout the year. Some are Chinese New Year, the lantern \n"
          "festival, Qingming festival, dragon boat festival, double seventh day, mid-autumn festival, \n"
          "winter solstice, summer solstice, double ninth, and the hungry ghost festival. To explain a few, \n"
          "Chinese New Year is the beginning of the new chinese calendar year, the lantern festival is the last day\n "
          "of the Chinese New Year period, Qingming is the day for people to visit graves and pay respect to \n"
          "ancestors, and the mid-autumn festival is to worship the moon and eat mooncakes.\n (press enter to keep "
          "going)")
    print("For more information about this topic, here are some books you can reference!")
    print("Encyclopedia of Contemporary Chinese Culture   by Edward Lawrence Davis")
    print("PoPo's Lucky Chinese New Year   by Virginia Loh-Hagan")
    print("Education as Cultivation in Chinese Culture   by Shihkuan Hsu, Yuh-Yin Wu")
    print("-------------------------------------------------------")
    print("Thank you for your interest in learning more about China's traditions!")
    user_input = input("Would you like to take a quiz? yes/no")
    if user_input.lower() == "yes":
        china_quiz()
    else:
        print("Have a nice day!")
        quit()


def china_history():
    input("Thank you for your interest in learning more about China's history!(press enter to keep going)")
    print("-------------------------------------------------------")
    input("Today we will be learning about how China came to be.(press enter to keep going)")
    print("-------------------------------------------------------")
    input(
        "China was ruled by various dynasties for much of its history. The first dynasty is believed to be the Xia \n"
        "dynasty which formed somewhere around 2250 BC. During the Qing dynasty, western influences, \n"
        "European trade, and a number of wars all served to weaken China. Great Britain gained control of Hong Kong\n "
        "after the Opium Wars. In the early 1900s the people of China began to want reform. Revolutionary leader \n"
        "Sun Yat-sen created the Chinese Nationalist Peoples Party, also called the KMT or Kuomintang.Mao Zedong \n"
        "established the Peoples Republic of China on October 1, 1949.\n(press enter to keep going)")
    print("-------------------------------------------------------")
    print("For more information about this topic, here are some books you can reference!")
    print("China: A New Cultural History   by Cho-yun Hsu")
    print("A History of Chinese Civilization   by Jacques Gernet")
    print("A Brief History of China: Dynasty, Revolution and Transformation   by Jonathan Clements")
    print("-------------------------------------------------------")
    print("Thank you for your interest in learning more about China's history!")
    user_input = input("Would you like to take a quiz? yes/no")
    if user_input.lower() == "yes":
        china_quiz()
    else:
        print("Have a nice day!")
        quit()


def china_food():
    input("Thank you for your interest in learning more about China's food! (press enter to keep going)")
    print("-------------------------------------------------------")
    input("Today we will be learning about the most popular cuisines and snacks in China.(press enter to keep going)")
    input("Regarded as the soul of the Chinese dish, taste can be divided into five classes - sweet, sour, bitter,\n "
          "hot and salty. Seasoning such as soy sauce, sugar, vinegar and salt in proper amount and in different \n"
          "sequences, contribute to the taste of the dish. In the vast land of China, there are eating habits of \n"
          "'South-Sweet, North-Salty, East-Hot and West-Sour' according to the different tastes of the people. Those\n "
          "in southern China like to add more sugar when cooking than others. \n(press enter to keep going)")
    print("-------------------------------------------------------")
    print("For more information about this topic, here are some books you can reference!")
    print("The Food of China   by E.N. Anderson")
    print("Globalization of Chinese Food   by Sidney Cheung, David Y.H. Wu")
    print("The Land of the Five Flavors: A Cultural History of Chinese Cuisine    by Thomas O. Hollmann")
    print("-------------------------------------------------------")
    print("Thank you for your interest in learning more about China's food!")
    user_input = input("Would you like to take a quiz? yes/no")
    if user_input.lower() == "yes":
        china_quiz()
    else:
        print("Have a nice day!")
        quit()


def mexico_traditions():
    input("Thank you for your interest in learning more about Mexico's traditions!(press enter to keep going)")
    print("-------------------------------------------------------")
    input("Today we will be learning about the most famous festivals and celebrations in Mexico. (press enter to keep "
          "going)")
    print("-------------------------------------------------------")
    input("Mexico has a lot of fun and interesting traditions and celebrations. A few include Dia de Los Muertos,\n "
          "Las Posadas, Bull Fighting, Siestas, Cinco de Mayo, and Pinatas. To explain a few, Dia de Los Muertos is \n"
          "the day of the dead where people honor dead friends and family with all night vigils, Las Posadas is meant \n"
          "to commemorate Joseph and Mary making their way to Bethlehem, bull fighting is a big sport in Mexico, \n"
          "siestas are short naps that are taken in the early afternoon in Mexico, and Cinco de Mayo commemorates \n"
          "Mexico's victory over France. \n(press enter to keep going)")
    print("For more information about this topic, here are some books you can reference!")
    print("The Human Tradition in Mexico   by Jeffrey M. Pilcher")
    print("Mexican Culture   by Lori McManus")
    print("Cultural Traditions in Mexico   by Lynn Peppas")
    print("-------------------------------------------------------")
    print("Thank you for your interest in learning more about Mexico's traditions!")
    user_input = input("Would you like to take a quiz? yes/no")
    if user_input.lower() == "yes":
        mexico_quiz()
    else:
        print("Have a nice day!")
        quit()


def mexico_history():
    input("Thank you for your interest in learning more about Mexico's history!(press enter to keep going)")
    print("-------------------------------------------------------")
    input("Today we will be learning about how Mexico came to be.(press enter to keep going)")
    print("-------------------------------------------------------")
    input(
        "A country rich in history, tradition and culture, Mexico is made up of 31 states and one federal district. \n"
        "It is the third largest country in Latin America and has one of the largest populations—more than 100 \n"
        "million—making it the home of more Spanish speakers than any other nation in the world. Despite the \n"
        "political and social changes that have occurred over the centuries, evidence of past cultures and events \n"
        "are apparent everywhere in Mexico. Many of Mexico’s rural areas are still inhabited by indigenous people \n"
        "whose lifestyles are quite similar to those of their ancestors. In addition, many pre-Columbian ruins \n"
        "still exist throughout Mexico, including the ancient city of Teotihuacán and the Mayan pyramids at Chichén\n"
        "Itzá and Tulum. Reminders of the colonial past are evident in the architecture of towns like Taxco and \n"
        "Querétaro.\n(press enter to keep going)")
    print("-------------------------------------------------------")
    print("For more information about this topic, here are some books you can reference!")
    print("The Oxford History of Mexico   by William Beezley")
    print("Mexican History   by Nora E. Jaffary")
    print("The Great Book of Mexico   by Bill O'Neill")
    print("-------------------------------------------------------")
    print("Thank you for your interest in learning more about Mexico's history!")
    user_input = input("Would you like to take a quiz? yes/no")
    if user_input.lower() == "yes":
        mexico_quiz()
    else:
        print("Have a nice day!")
        quit()


def mexico_food():
    input("Thank you for your interest in learning more about Mexico's food! (press enter to keep going)")
    print("-------------------------------------------------------")
    input("Today we will be learning about the most popular cuisines and snacks in Mexico.(press enter to keep going)")
    print("-------------------------------------------------------")
    input("Among the staples of Mexican food are beans and corn. Corn is used to make masa, a dough that is then \n"
          "turned into tortillas and tamales, whereas beans and corn feature prominently in many dishes.Mexican \n"
          "cooking is packed with flavour; among the herbs and spices that give it its distinct kick are a variety of\n "
          "chillies (fresh, dried, smoked and pickled), alongside oregano, coriander (known as cilantro in North \n"
          "America), cinnamon and cocoa. Garlic, onions, lemons and limes are also used generously.\n(press enter to keep going)")
    print("-------------------------------------------------------")
    print("For more information about this topic, here are some books you can reference!")
    print("Planet Taco: A Global History of Mexican Food   by Jeffrey M. Pilcher")
    print("The Book of Mexican Foods   by Christine Barret")
    print("Taco USA: How Mexican Food Conquered America   by Gustavo Arellano")
    print("-------------------------------------------------------")
    print("Thank you for your interest in learning more about Mexico's food!")
    user_input = input("Would you like to take a quiz? yes/no")
    if user_input.lower() == "yes":
        mexico_quiz()
    else:
        print("Have a nice day!")
        quit()


def india_quiz():
    question1 = input("What is the festival of lights called?")
    if question1.lower() == "diwali":
        input("Correct! Wow you are smart! Press Enter to move on to the next question.")
        question2 = input("Is India a continent?")
    else:
        input("Incorrect. Better luck in the next one! Press Enter to move on to the next question.")
        question2 = input("Is India a continent?")
    if question2.lower() == "no":
        input("Correct! Wow you are smart! Press Enter to move on to the next question.")
        question3 = input("True or False: India only has one religion.")
    else:
        input("Incorrect. Better luck in the next one! Press Enter to move on to the next question.")
        question3 = input("True or False: India only has one religion.")
    if question3.lower() == "false":
        input("Correct! Wow you are smart! Press Enter to end.")
    else:
        input("Incorrect. Better luck in the next one! Press Enter to end.")
        quit()


def china_quiz():
    question1 = input("Does the moon festival take place in autumn?")
    if question1.lower() == "yes":
        input("Correct! Wow you are smart! Press Enter to move on to the next question.")
        question2 = input("The war fought between China and Britain was over what drug?")
    else:
        input("Incorrect. Better luck in the next one! Press Enter to move on to the next question.")
        question2 = input("The war fought between China and Britain was over what drug?")
    if question2.lower() == "opium":
        input("Correct! Wow you are smart! Press Enter to move on to the next question.")
        question3 = input("What is the national animal of China?")
    else:
        input("Incorrect. Better luck in the next one! Press Enter to move on to the next question.")
        question3 = input("What is the national animal of China?")
    if question3.lower() == "panda":
        input("Correct! Wow you are smart! Press Enter to move end.")
    else:
        input("Incorrect. Better luck in the next one! Press Enter to move on to end.")
        quit()

def mexico_quiz():
    question1 = input("What animal is on the Mexican flag?")
    if question1.lower() == "eagle":
        input("Correct! Wow you are smart! Press Enter to move on to the next question.")
        question2 = input("What country did Mexico win over in the Cinco de Mayo battle?")
    else:
        input("Incorrect. Better luck in the next one! Press Enter to move on to the next question.")
        question2 = input("What country did Mexico win over in the Cinco de Mayo battle?")
    if question2.lower() == "france":
        input("Correct! Wow you are smart! Press Enter to move on to the next question.")
        question3 = input("Is Mexico a US state?")
    else:
        input("Incorrect. Better luck in the next one! Press Enter to move on to the next question.")
        question3 = input("Is Mexico a US state?")
    if question3.lower() == "no":
        input("Correct! Wow you are smart! Press Enter to Press Enter to move end.")
    else:
        input("Incorrect. Better luck in the next one! Press Enter to move on to end.")
        quit()
