from random import choice
from random import seed
from time import sleep

def generator(name, princess, location):
    seed()
    name = choice(name)
    seed()
    princess = choice(princess)
    seed()
    location = choice(location)
    print "THANK YOU MARIO BUT OUR %s IS IN ANOTHER %s." % (princess, location)

def main():
    name = ["JACOB",
    "MICHAEL",
    "JOSHUA",
    "MATTHEW",
    "DANIEL",
    "CHRISTOPHER",
    "ANDREW",
    "ETHAN",
    "JOSEPH",
    "WILLIAM",
    "ANTHONY",
    "DAVID",
    "ALEXANDER",
    "NICHOLAS",
    "RYAN",
    "TYLER",
    "JAMES",
    "JOHN",
    "JONATHAN",
    "NOAH",
    "BRANDON",
    "CHRISTIAN",
    "DYLAN",
    "SAMUEL",
    "BENJAMIN",
    "NATHAN",
    "ZACHARY",
    "LOGAN",
    "JUSTIN",
    "GABRIEL",
    "JOSE",
    "AUSTIN",
    "KEVIN",
    "ELIJAH",
    "CALEB",
    "ROBERT",
    "THOMAS",
    "JORDAN",
    "CAMERON",
    "JACK",
    "HUNTER",
    "JACKSON",
    "ANGEL",
    "ISAIAH",
    "EVAN",
    "ISAAC",
    "LUKE",
    "MASON",
    "JASON",
    "JAYDEN",
    "GAVIN",
    "AARON",
    "CONNOR",
    "AIDEN",
    "AIDAN",
    "KYLE",
    "JUAN",
    "CHARLES",
    "LUIS",
    "ADAM",
    "LUCAS",
    "BRIAN",
    "ERIC",
    "ADRIAN",
    "NATHANIEL",
    "SEAN",
    "ALEX",
    "CARLOS",
    "IAN",
    "BRYAN",
    "OWEN",
    "JESUS",
    "LANDON",
    "JULIAN",
    "CHASE",
    "COLE",
    "DIEGO",
    "JEREMIAH",
    "STEVEN",
    "SEBASTIAN",
    "XAVIER",
    "TIMOTHY",
    "CARTER",
    "WYATT",
    "BRAYDEN",
    "BLAKE",
    "HAYDEN",
    "DEVIN",
    "CODY",
    "RICHARD",
    "SETH",
    "DOMINIC",
    "JADEN",
    "ANTONIO",
    "MIGUEL",
    "LIAM",
    "PATRICK",
    "CARSON",
    "JESSE",
    "TRISTAN",
    "ALEJANDRO",
    "HENRY",
    "VICTOR",
    "TREVOR",
    "BRYCE",
    "JAKE",
    "RILEY",
    "COLIN",
    "JARED",
    "JEREMY",
    "MARK",
    "CADEN",
    "GARRETT",
    "PARKER",
    "MARCUS",
    "VINCENT",
    "KALEB",
    "KADEN",
    "BRADY",
    "COLTON",
    "KENNETH",
    "JOEL",
    "OSCAR",
    "JOSIAH",
    "JORGE",
    "COOPER",
    "ASHTON",
    "TANNER",
    "EDUARDO",
    "PAUL",
    "EDWARD",
    "IVAN",
    "PRESTON",
    "MAXWELL",
    "ALAN",
    "LEVI",
    "STEPHEN",
    "GRANT",
    "NICOLAS",
    "OMAR",
    "DAKOTA",
    "ALEXIS",
    "GEORGE",
    "COLLIN",
    "ELI",
    "SPENCER",
    "GAGE",
    "MAX",
    "CRISTIAN",
    "RICARDO",
    "DEREK",
    "MICAH",
    "BRODY",
    "FRANCISCO",
    "NOLAN",
    "AYDEN",
    "DALTON",
    "SHANE",
    "PETER",
    "DAMIAN",
    "JEFFREY",
    "BRENDAN",
    "TRAVIS",
    "FERNANDO",
    "PEYTON",
    "CONNER",
    "ANDRES",
    "JAVIER",
    "GIOVANNI",
    "SHAWN",
    "BRADEN",
    "JONAH",
    "BRADLEY",
    "CESAR",
    "EMMANUEL",
    "MANUEL",
    "EDGAR",
    "MARIO",
    "ERIK",
    "EDWIN",
    "JOHNATHAN",
    "DEVON",
    "ERICK",
    "WESLEY",
    "OLIVER",
    "TRENTON",
    "HECTOR",
    "MALACHI",
    "JALEN",
    "RAYMOND",
    "GREGORY",
    "ABRAHAM",
    "ELIAS",
    "LEONARDO",
    "SERGIO",
    "DONOVAN",
    "COLBY",
    "MARCO",
    "BRYSON",
    "MARTIN",
    "EMILY",
    "MADISON",
    "EMMA",
    "OLIVIA",
    "HANNAH",
    "ABIGAIL",
    "ISABELLA",
    "SAMANTHA",
    "ELIZABETH",
    "ASHLEY",
    "ALEXIS",
    "SARAH",
    "SOPHIA",
    "ALYSSA",
    "GRACE",
    "AVA",
    "TAYLOR",
    "BRIANNA",
    "LAUREN",
    "CHLOE",
    "NATALIE",
    "KAYLA",
    "JESSICA",
    "ANNA",
    "VICTORIA",
    "MIA",
    "HAILEY",
    "SYDNEY",
    "JASMINE",
    "JULIA",
    "MORGAN",
    "DESTINY",
    "RACHEL",
    "ELLA",
    "KAITLYN",
    "MEGAN",
    "KATHERINE",
    "SAVANNAH",
    "JENNIFER",
    "ALEXANDRA",
    "ALLISON",
    "HALEY",
    "MARIA",
    "KAYLEE",
    "LILY",
    "MAKAYLA",
    "BROOKE",
    "NICOLE",
    "MACKENZIE",
    "ADDISON",
    "STEPHANIE",
    "LILLIAN",
    "ANDREA",
    "ZOE",
    "FAITH",
    "KIMBERLY",
    "MADELINE",
    "ALEXA",
    "KATELYN",
    "GABRIELLA",
    "GABRIELLE",
    "TRINITY",
    "AMANDA",
    "KYLIE",
    "MARY",
    "PAIGE",
    "RILEY",
    "LEAH",
    "JENNA",
    "SARA",
    "REBECCA",
    "MICHELLE",
    "SOFIA",
    "VANESSA",
    "JORDAN",
    "ANGELINA",
    "CAROLINE",
    "AVERY",
    "AUDREY",
    "EVELYN",
    "MAYA",
    "CLAIRE",
    "AUTUMN",
    "JOCELYN",
    "ARIANA",
    "NEVAEH",
    "ARIANNA",
    "JADA",
    "BAILEY",
    "BROOKLYN",
    "AALIYAH",
    "AMBER",
    "ISABEL",
    "MARIAH",
    "DANIELLE",
    "MELANIE",
    "SIERRA",
    "ERIN",
    "MOLLY",
    "AMELIA",
    "ISABELLE",
    "MADELYN",
    "MELISSA",
    "JACQUELINE",
    "MARISSA",
    "SHELBY",
    "ANGELA",
    "LESLIE",
    "KATIE",
    "JADE",
    "CATHERINE",
    "DIANA",
    "AUBREY",
    "MYA",
    "AMY",
    "BRIANA",
    "SOPHIE",
    "GABRIELA",
    "BREANNA",
    "GIANNA",
    "KENNEDY",
    "GRACIE",
    "PEYTON",
    "ADRIANA",
    "CHRISTINA",
    "COURTNEY",
    "DANIELA",
    "LYDIA",
    "KATHRYN",
    "VALERIA",
    "LAYLA",
    "ALEXANDRIA",
    "NATALIA",
    "ANGEL",
    "LAURA",
    "CHARLOTTE",
    "MARGARET",
    "CHEYENNE",
    "MIKAYLA",
    "MIRANDA",
    "NAOMI",
    "KELSEY",
    "PAYTON",
    "ANA",
    "ALICIA",
    "JILLIAN",
    "DAISY",
    "MCKENZIE",
    "ASHLYN",
    "SABRINA",
    "CAITLIN",
    "SUMMER",
    "RUBY",
    "RYLEE",
    "VALERIE",
    "SKYLAR",
    "LINDSEY",
    "KELLY",
    "GENESIS",
    "ZOEY",
    "EVA",
    "SADIE",
    "ALEXIA",
    "CASSIDY",
    "KYLEE",
    "KENDALL",
    "JORDYN",
    "KATE",
    "JAYLA",
    "KAREN",
    "TIFFANY",
    "CASSANDRA",
    "JULIANA",
    "REAGAN",
    "CAITLYN",
    "GISELLE",
    "SERENITY",
    "ALONDRA",
    "LUCY",
    "BIANCA",
    "KIARA",
    "CRYSTAL",
    "ERICA",
    "ANGELICA",
    "HOPE",
    "CHELSEA",
    "ALANA",
    "LILIANA",
    "BRITTANY",
    "CAMILA",
    "MAKENZIE",
    "LILLY",
    "VERONICA",
    "ABBY",
    "JAZMIN",
    "ADRIANNA",
    "DELANEY",
    "KARINA",
    "ELLIE",
    "JASMIN"
  ]

    princess= ["HERO",
    "ANALYST",
    "REASONER",
    "BUREAUCRAT",
    "LAWYER",
    "ACCOUNTANT",
    "POLITICIAN",
    "MANAGER",
    "CARETAKER",
    "DOCTOR",
    "HEALER",
    "NURSE",
    "CATALYST",
    "COWARD",
    "CURMUDGEON",
    "GRUMP",
    "MENTOR",
    "ELDER",
    "TEACHER",
    "PROFESSOR",
    "PARENT",
    "SHAMAN",
    "GUIDE",
    "SOOTHSAYER",
    "EXPOSITOR",
    "HIEROPHANT",
    "TRICKSTER",
    "SHAPESHIFTER",
    "MAGICIAN",
    "DEVIL",
    "FOOL",
    "JOKER",
    "JESTER",
    "IDIOT",
    "CHILD",
    "INNOCENT",
    "VIRGIN",
    "YOUTH",
    "INGENUE",
    "SELF",
    "MIRROR-IMAGE",
    "HERMIT",
    "LONER",
    "INTROVERT",
    "WANDERER",
    "TRAVELER",
    "EXPLORER",
    "HUNTER",
    "SEEKER",
    "TRACKER",
    "INSPECTOR",
    "JUDGE",
    "JUSTICE",
    "MAGISTRATE",
    "ARBITER",
    "SHERIFF",
    "REFEREE",
    "EXAMINER",
    "WEAVER",
    "CREATOR",
    "SPINNER",
    "DEATH",
    "EXECUTIONER",
    "GIVER",
    "BENEFACTOR",
    "SUPERHUMAN",
    "DREAMER",
    "THINKER",
    "GOSSIP",
    "TATTLETALE",
    "WHISPERER",
    "COMMUNICATOR",
    "GUARDIAN",
    "PROTECTOR",
    "HEDONIST",
    "PLEASURE-SEEKER",
    "LEADER",
    "CAPTAIN",
    "GENERAL",
    "MARTYR",
    "EVERYMAN",
    "POET",
    "BARD",
    "SINGER",
    "PHILOSOPHER",
    "REBEL",
    "ROGUE",
    "OUTSIDER",
    "FIGHTER",
    "SLAVE",
    "CAPTIVE",
    "LABORER",
    "SAMARITAN",
    "SCHOLAR",
    "DIDACT",
    "ACADEMIC",
    "LEARNER",
    "SURVIVOR",
    "ESCAPEE",
    "SYCOPHANT",
    "YES-MAN",
    "TEMPTRESS",
    "SEDUCTRESS",
    "TYRANT",
    "BULLY",
    "VICTIM",
    "TARGET",
    "SUFFERER",
    "WAIF",
    "WEAKLING",
    "RAGAMUFFIN",
    "URCHIN",
    "MINION",
    "LACKEY",
    "WORKER",
    "EMPLOYEE",
    "PRINCESS",
    "QUEEN",
    "KING",
    "PRINCE"]

    location = ["AQUARIUM",
    "ARCADE",
    "ART GALLERY",
    "BOWLING ALLEY",
    "CASINO",
    "CIRCUS",
    "COMEDY CLUB",
    "CONCERT HALL",
    "COUNTRY DANCE CLUB",
    "DISC GOLF",
    "GENERAL ENTERTAINMENT",
    "GO KART TRACK",
    "HISTORIC SITE",
    "LASER TAG",
    "MINI GOLF",
    "MOVIE THEATER",
    "ART MUSEUM",
    "HISTORY MUSEUM"
    "PLANETARIUM",
    "SCIENCE MUSEUM",
    "MUSIC VENUE",
    "JAZZ CLUB",
    "PIANO BAR",
    "ROCK CLUB",
    "OUTDOOR SCULPTURE",
    "PERFORMING ARTS VENUE",
    "DANCE STUDIO",
    "INDIE THEATER",
    "OPERA HOUSE"
    "THEATER",
    "POOL HALL",
    "PUBLIC ART",
    "RACETRACK",
    "ROLLER RINK",
    "SALSA CLUB",
    "STADIUM",
    "BASEBALL STADIUM",
    "BASKETBALL STADIUM",
    "CRICKET GROUND",
    "FOOTBALL STADIUM",
    "HOCKEY ARENA",
    "SOCCER STADIUM",
    "TENNIS COURT",
    "TRACK FIELD",
    "STREET ART INSTALLATION",
    "THEME PARK",
    "WATER PARK",
    "ZOO",
    "ACADEMIC BUILDING",
    "DORM",
    "ADMINISTRATIVE BUILDING",
    "CORPORATE OFFICE",
    "AUDITORIUM",
    "BOOKSTORE",
    "CAFETERIA",
    "CLASSROOM",
    "GYM",
    "LAB",
    "LIBRARY",
    "RECREATION CENTER",
    "RESIDENCE HALL",
    "COMMUNITY COLLEGE",
    "FRATERNITY HOUSE",
    "LAW SCHOOL",
    "SORORITY HOUSE",
    "MEDICAL SCHOOL",
    "STUDENT CENTER",
    "TRADE SCHOOL",
    "UNIVERSITY",
    "EVENT",
    "CONFERENCE",
    "CONVENTION",
    "FESTIVAL",
    "MUSIC FESTIVAL",
    "PARADE",
    "STOOP SALE",
    "STREET FAIR",
    "AFGHAN RESTAURANT",
    "AFRICAN RESTAURANT",
    "AMERICAN RESTAURANT",
    "AREPA RESTAURANT",
    "ARGENTINIAN RESTAURANT",
    "ASIAN RESTAURANT",
    "AUSTRALIAN RESTAURANT",
    "AUSTRIAN RESTAURANT",
    "BBQ JOINT",
    "BAGEL SHOP",
    "BAKERY",
    "BELARUSIAN RESTAURANT",
    "BELGIAN RESTAURANT",
    "BISTRO",
    "BRAZILIAN RESTAURANT",
    "BREAKFAST SPOT",
    "BUBBLE TEA SHOP",
    "BUFFET",
    "BURGER JOINT",
    "BURRITO PLACE",
    "CAFE",
    "CAJUN RESTAURANT",
    "CAMBODIA RESTAURANT",
    "CARIBBEAN RESTAURANT",
    "CHINESE RESTAURANT",
    "COFFEE SHOP",
    "CREPERIE",
    "CUBAN RESTAURANT",
    "CUPCAKE SHOP",
    "CZECH RESTAURANT",
    "DELI",
    "BODEGA",
    "DESSERT SHOP",
    "DIM SUM RESTAURANT",
    "DINER",
    "DISTILLERY",
    "DONUT SHOP",
    "DUMPLING RESTAURANT",
    "BRITISH RESTAURANT",
    "ETHIOPIAN RESTAURANT",
    "FALAFEL RESTAURANT",
    "FAST FOOD PLACE",
    "FISH & CHIPS SHOP",
    "FONDUE RESTAURANT",
    "FOOD TRUCK",
    "FRENCH RESTAURANT",
    "FRIED CHICKEN JOINT",
    "GASTROPUB",
    "GERMAN BEER HALL",
    "GLUTEN-FREE RESTAURANT",
    "GREEK RESTAURANT",
    "HALAL RESTAURANT",
    "HAWAIIAN RESTAURANT",
    "HIMALAYAN RESTAURANT",
    "HOT DOG CART",
    "KOREAN BBQ",
    "ICE CREAM SHOP",
    "INDIAN BUFFET",
    "INDONESIAN RESTAURANT",
    "IRISH PUB",
    "ITALIAN RESTAURANT",
    "JAPANESE RESTAURANT",
    "SUSHI RESTAURANT",
    "JEWISH DELI",
    "JUICE BAR",
    "KOREAN RESTAURANT",
    "MAC & CHEESE JOINT",
    "MALAYSIAN RESTAURANT",
    "MEDITERRANEAN RESTAURANT",
    "MEXICAN RESTAURANT",
    "MIDDLE EASTERN RESTAURANT",
    "MOLECUR GASTRONOMY RESTAURANT",
    "MONGOLIAN RESTAURANT",
    "MOROCCAN RESTAURANT",
    "MUSEUM OF JURASSIC TECHNOLOGY",
    "PAKISTANI RESTAURANT",
    "PERSIAN RESTAURANT",
    "PERUVIAN RESTAURANT",
    "PIE SHOP",
    "PIZZA PLACE",
    "POLISH RESTAURANT",
    "RAMEN SHOP",
    "NOODLE HOUSE",
    "RUSSIAN RESTAURANT",
    "HUNGARIAN RESTAURANT",
    "ROMANIAN RESTAURANT",
    "SALAD SHOP",
    "SANDWICH PLACE",
    "SCANDINAVIAN RESTAURANT",
    "SEAFOOD RESTAURANT",
    "SNACK PLACE",
    "SOUP PLACE",
    "SOUTHERN RESTAURANT",
    "SOUL FOOD RESTAURANT",
    "SOUVLAKI SHOP",
    "SPANISH RESTAURANT",
    "STEAKHOUSE",
    "SWISS RESTAURANT",
    "TACO SHOP",
    "TAPAS RESTAURANT",
    "TEA ROOM",
    "THAI RESTAURANT",
    "PHO SOUP SHOP",
    "TURKISH RESTAURANT",
    "UKRAINIAN RESTAURANT",
    "VEGETARIAN RESTAURANT",
    "VEGAN RESTAURANT",
    "VIETNAMESE RESTAURANT",
    "WINERY",
    "WING JOINT",
    "FROZEN YOGURT SHOP",
    "BAR",
    "BEACH BAR",
    "BEER GARDEN",
    "BREWERY",
    "CHAMPAGNE BAR",
    "COCKTAIL BAR",
    "DIVE BAR",
    "GAY BAR",
    "HOOKAH BAR",
    "HOTEL BAR",
    "KARAOKE BAR",
    "LOUNGE",
    "NIGHT MARKET",
    "NIGHTCLUB",
    "PUB",
    "SAKE BAR",
    "SPEAKEASY",
    "SPORTS BAR",
    "STRIP CLUB",
    "WHISKEY BAR",
    "WINE BAR",
    "BADMINTON COURT",
    "BASEBALL FIELD",
    "BASKETBALL COURT", 
    "BOWLING GREEN",
    "GOLF COURSE",
    "HOCKEY FIELD",
    "PAINTBALL FIELD",
    "RUGBY PITCH",
    "SKATE PARK",
    "SKATING RINK",
    "SOCCER FIELD",
    "SPORTS CLUB",
    "SQUASH COURT",
    "TENNIS COURT",
    "VOLLEYBALL COURT",
    "BATH HOUSE",
    "BATHING AREA",
    "BEACH",
    "NUDE BEACH",
    "SURF SPOT",
    "BOTANICAL GARDEN",
    "BRIDGE",
    "CAMPGROUND",
    "CASTLE",
    "CEMETERY",
    "DIVE SPOT",
    "DOG RUN",
    "FARM",
    "FIELD"
    "FISHING SPOT",
    "FOREST",
    "GARDEN",
    "GUN RANGE",
    "HARBOR",
    "MARINA",
    "HOT SPRING",
    "ISLAND",
    "LAKE",
    "LIGHTHOUSE",
    "MOUNTAIN",
    "NATIONAL PARK",
    "PALACE",
    "PARK",
    "PEDESTRIAN PLAZA",
    "PLAYGROUND",
    "PLAZA",
    "POOL",
    "RAFTING SPOT",
    "RIVER",
    "ROCK CLIMBING GYM",
    "SCENIC LOOKOUT",
    "SCULPTURE GARDEN",
    "SKI VILLAGE",
    "HORSE STABLE",
    "CITY",
    "COUNTY",
    "COUNTRY",
    "NEIGHBORHOOD",
    "STATE",
    "TOWN",
    "NATION",
    "VILLAGE",
    "SUMMER CAMP",
    "TRAIL",
    "TREE",
    "VINEYARD",
    "VOLCANO",
    "WELL",
    "ANIMAL SHELTER",
    "AUDITORIUM",
    "BUILDING",
    "CLUB HOUSE",
    "COMMUNITY CENTER",
    "CONVENTION CENTER",
    "MEETING ROOM",
    "CULTURAL CENTER",
    "DISTRIBUTION CENTER",
    "EVENT SPACE",
    "FACTORY",
    "FAIR",
    "FUNERAL HOME",
    "CAPITOL BUILDING",
    "CITY HALL",
    "COURTHOUSE",
    "EMBASSY",
    "CONSULATE",
    "FIRE STATION",
    "MONUMENT",
    "LANDMARK",
    "POLICE STATION",
    "TOWN HALL",
    "MEDICAL CENTER",
    "DENTIST'S OFFICE",
    "DOCTOR'S OFFICE",
    "EMERGENCY ROOM",
    "HOSPITAL",
    "LABORATORY",
    "VETERINARIAN OFFICE",
    "MILITARY BASE",
    "NON-PROFIT",
    "OFFICE",
    "AD AGENCY",
    "CAMPAIGN OFFICE",
    "CONFERENCE ROOM",
    "CO-WORKING SPACE",
    "TECH STARTUP",
    "PARKING STRUCTURE",
    "POST OFFICE",
    "PRISON",
    "RADIO STATION",
    "RECRUITING AGENCY",
    "SCHOOL",
    "CIRCUS SCHOOL",
    "DRIVING SCHOOL",
    "ELEMENTARY SCHOOL",
    "FLIGHT SCHOOL",
    "HIGH SCHOOL",
    "LANGUAGE SCHOOL",
    "MIDDLE SCHOOL",
    "MUSIC SCHOOL",
    "NURSERY SCHOOL",
    "PRESCHOOL",
    "PRIVATE SCHOOL",
    "RELIGIOUS SCHOOL",
    "SWIM SCHOOL",
    "SOCIAL CLUB",
    "BUDDHIST TEMPLE",
    "CHURCH",
    "HINDU TEMPLE",
    "MONASTERY",
    "MOSQUE",
    "PRAYER ROOM",
    "SHRINE",
    "SYNAGOGUE",
    "TEMPLE",
    "TV STATION",
    "VOTING BOOTH",
    "WAREHOUSE"
    "ASSISTED LIVING FACILITY",
    "HOME",
    "HOUSING DEVELOPMENT",
    "APARTMENT BUILDING",
    "TRAILER PARK",
    "ATM LOBBY",
    "ADULT BOUTIQUE",
    "ANTIQUE SHOP",
    "ARTS & CRAFTS STORE",
    "ASTROLOGER",
    "AUTO GARAGE",
    "AUTOMOTIVE SHOP",
    "BABY STORE",
    "BANK",
    "BETTING SHOP",
    "BIG BOX STORE",
    "IKEA",
    "BIKE SHOP",
    "BOARD SHOP",
    "BOOKTSORE",
    "BRIDAL SHOP",
    "CAMERA STORE",
    "CANDY STORE",
    "CAR DEALERSHIP",
    "CAR WASH",
    "CARPET STORE",
    "CHECK CASHING STORE",
    "CHOCOLATE SHOP",
    "CHRISTMAS MARKET",
    "CLOTHING STORE",
    "SHOE STORE",
    "COMIC SHOP",
    "CONVENIENCE STORE",
    "COSMETICS SHOP",
    "COSTUME SHOP",
    "CREDIT UNION",
    "DAYCARE",
    "DEPARTMENT STORE",
    "DESIGN STUDIO",
    "DISCOUNT STORE",
    "DIVE SHOP",
    "DRUGSTORE",
    "PHARMACY",
    "DRY CLEANER",
    "EV CHARGING STATION",
    "ELECTRONICS STORE",
    "FABRIC SHOP",
    "FISHING TACKLE SHOP",
    "FLEA MARKET",
    "FLOWER SHOP",
    "BEER DISTRIBUTOR",
    "BUTCHER SHOP",
    "CHEESE SHOP",
    "FARMERS MARKET",
    "FISH MARKET",
    "FOOD COURT",
    "GROCERY STORE",
    "HEALTH FOOD STORE",
    "LIQUOR SHOP",
    "ORGANIC GROCERY",
    "STREET FOOD STALL",
    "SUPERMARKET",
    "WINE SHOP",
    "FRAME STORE",
    "FURNITURE STORE",
    "GAMING CAFE",
    "GARDEN CENTER",
    "GAS STATION",
    "GARAGE",
    "GIFT SHOP",
    "GUN RANGE",
    "FITNESS CENTER",
    "BOXING GYM",
    "CLIMBING GYM",
    "CYCLE STUDIO",
    "DOJO",
    "YOGA STUDIO",
    "HARDWARE STORE",
    "SPA",
    "HOBBY SHOP",
    "IT SERVICES BUILDING",
    "INTERNET CAFE",
    "JEWELRY STORE",
    "KNITTING STORE",
    "LAUNDROMAT",
    "LAUNDRY SERVICE",
    "LEATHER GOODS STORE",
    "LOCKSMITH",
    "LOTTERY RETAILER",
    "LUGGAGE STORE",
    "MALL",
    "MARIJUANA DISPENSARY",
    "MARKET",
    "MASSAGE STUDIO",
    "MATTRESS STORE",
    "99 CENTS SHOP",
    "MOBILE PHONE STORE",
    "RECORD STORE",
    "NAIL SALON",
    "NEWSSTAND",
    "OPTICS SHOP",
    "OUTDOOR OUTFITTERS STORE",
    "OUTLET STORE",
    "OFFICE SUPPLIES STORE",
    "PAWN SHOP",
    "PET STORE",
    "PHOTO LAB",
    "PIERCING PAGODA",
    "POP-UP SHOP",
    "PRINT SHOP",
    "REAL ESTATE OFFICE",
    "RECORDING STUDIO",
    "RECYCLING FACILITY",
    "SALON",
    "BARBERSHOP",
    "SHIPPING STORE",
    "COBBLER",
    "SMOKE SHOP"
    "HEAD SHOP",
    "SMOOTHIE SHOP",
    "SOUVENIR SHOP",
    "TANNING SALON",
    "TATTOO PARLOR",
    "THRIFT STORE",
    "VINTAGE STORE",
    "TOY STORE",
    "TRAVEL AGENCY",
    "USED BOOKSTORE",
    "VIDEOGAME STORE",
    "VIDEO STORE",
    "WATCH REPAIR SHOP",
    "AIRPORT",
    "AIRPORT LOUNGE",
    "TERMINAL",
    "PLANE",
    "BOAT",
    "FERRY",
    "BUS STATION",
    "BUS STOP",
    "CABLE CAR",
    "HOTEL",
    "BED & BREAKFAST",
    "HOSTEL",
    "HOTEL POOL",
    "MOTEL",
    "RESORT",
    "ROOF DECK",
    "PIER",
    "RV PARK",
    "REST AREA",
    "RENTAL CAR OFFICE",
    "SUBWAY",
    "TAXI STAND",
    "TOLL BOOTH",
    "TOLL PLAZA",
    "TOURIST INFORMATION CENTER",
    "TRAIN STATION",
    "TRAM",
    "TRAVEL LOUNGE",
    "TUNNEL"]

    while(1):
        generator(name,princess,location)
        sleep(4)
if __name__ == "__main__":
    main()