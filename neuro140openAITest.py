from openai import OpenAI
import docx2txt
import random
import csv

# Connect to the Open AI API
client = OpenAI()

# A database of all the names of girls that limericks were written about
# Use these names to prompt the GPT who to write about
names = [
    "Busola Banjoh", 
    "Caroline Ferner", 
    "Daphnee Piou", 
    "Elise Colin", 
    "Elizabeth Paglione", 
    "Ellie Shahbo",
    "Hannah Valencia",
    "Jada Jones",
    "Julia Beckmann",
    "Lizzy Gumner",
    "Maria DiMartinis",
    "Olivia Hoover",
    "Olly Gill",
    "Rachel Greenwood",
    "Stella Feder",
    "Tollu Moses",
    "Venus Nnadi",
    "Aimee Howard",
    "Ally Chun",
    "Anais Colin",
    "Ariel Beck",
    "Artha Jonassaint",
    "Ava Gavitt",
    "Binney Huffman",
    "Calla Bai",
    "Cameron Amianda",
    "Carolina Vela",
    "Caroline Mullahy",
    "Charley Meier",
    "Chloe Fair",
    "Elise Hawkins",
    "Elle Staufer",
    "Ellie Stevens",
    "Emily Guckian",
    "Emma Manigat",
    "Ericka Familia",
    "Grace Lang",
    "Hannah Bebar",
    "Key Williams",
    "Kiani Akina",
    "Lili Gavitt",
    "Luca Leschly",
    "Lucy Leel",
    "Mandy Brenner",
    "Nia Orakwue",
    "Nneka Arinzeh",
    "Rain Wang",
    "Rebecca Solomon",
    "Seo Young",
    "Solomey Alemseg",
    "Victoria Bossong",
    "Yosely Jiminez",
    "Adede Appah-Sampong",
    "Adele Lee",
    "Alex Kim",
    "Annabel Hagen",
    "Athena Ye",
    "Carly Tiras",
    "Cate Hazel",
    "Celine Ibrahim",
    "Choetsow Tenzin",
    "Dumebi Adigwe",
    "Eleanor Fitzgibbons",
    "Elena Viciera",
    "Evie Geier",
    "Grace Huslander",
    "Grace Steelman",
    "Halima Badri",
    "Hollyn Torres",
    "Izzy Nova",
    "Jenn Luong",
    "Kira Hall",
    "Leah Margulies",
    "Leyla Ewald",
    "Alexis Elliot",
    "Brooke Jovanovich",
    "Maddy Gavitt",
    "Mariel Ayiah",
    "Maya Simkowitz",
    "MeganeBantefa",
    "Meredith Langmuir",
    "Molly Chiang",
    "Olivia Proctor",
    "Ryyan Pritchett",
    "Sara Solomon",
    "Shealyn Jenkins",
    "Sierra Agarwal",
    "Sydney Mason",
    "Ava Stone",
    "Bronte Brough",
    "Brynne Faltinsky",
    "Charisma Chen",
    "Daisy Nussbaum",
    "Dariana Almonte",
    "Despina Giannakopoulos",
    "Ella Dotzler",
    "Fiene Oerlemans",
    "Grace Lang",
    "Hannah Nguyen",
    "Kaia Li",
    "Katie Krupa",
    "Kendra Morris",
    "Leah Yeshitla",
    "Liv Ernst",
    "Lucie Bai",
    "Lwam Mahari",
    "Madison Hussey",
    "Maggie Turner",
    "Maya Walter",
    "Melody Cao",
    "Mena Solomon",
    "Mfoniso Andrew",
    "Natalie Martin",
    "Nicole Chavez",
    "Olivia Callander",
    "Omolivie Eboreime",
    "Peyton Hollis",
    "Saara Chaudry",
    "Sarah Adam",
    "Saran Gregory-Nghiem",
    "Smirti Somasundaram",
    "Tessa Shahbo",
    "Willow Woodward",
    "Zoe Clark"
]

# Database of all the limerick file names
# Used to randomly select 4 limericks to use as examples
files = [
    "BusolaBanjohLimerick.docx",
    "CarolineFernerLimerick.docx",
    "DaphneePiouLimerick.docx",
    "EliseColinLimerick.docx",
    "ElizabethPaglioneLimerick.docx",
    "EllieShahboLimerick.docx",
    "HannahValenciaLimerick.docx",
    "JadaJonesLimerick.docx",
    "JuliaBeckmannLimerick.docx",
    "LizzieGummerLimerick.docx",
    "MariaDiMartinisLimerick.docx",
    "OliviaHooverLimerick.docx",
    "OllyGillLimerick.docx",
    "RachelGreenwoodLimerick.docx",
    "StellaFederLimerick.docx",
    "TolluMoses Limerick.docx",
    "VenusNnadiLimerick.docx",
    "AimeeHoward.docx",
    "AllyChun.docx",
    "AnaisColin.docx",
    "ArielBeck.docx",
    "ArthaJonassaint.docx",
    "ArthaLimerick.docx",
    "AvaGavitt.docx",
    "BinneyLimerick.docx",
    "CallaLimerick.docx",
    "CameronAmianda.docx",
    "CarolinaVela.docx",
    "CarolineMullahy.docx",
    "CharleyMeier.docx",
    "ChloeFair.docx",
    "EliseHawkins.docx",
    "ElleStaufer.docx",
    "EllieStevens.docx",
    "EmilyGuckian.docx",
    "EmmaManigat.docx",
    "ErickaFamilia.docx",
    "HannahBebar.docx",
    "KeyWilliams.docx",
    "KianiAkina.docx",
    "LiliGavitt.docx",
    "LucaLeschly.docx",
    "LucyLeel.docx",
    "MandyBrenner.docx",
    "NiaOrakwue.docx",
    "NnekaArinzeh.docx",
    "RainWang.docx",
    "RebeccaSolomon.docx",
    "SeoYoung.docx",
    "SolomeyAlemseged.docx",
    "VictoriaBossong.docx",
    "YoselyJiminez.docx",
    "AdeleLimerick.docx",
    "AlexKimLimerick.docx",
    "AdedeLimerick.docx",
    "AnnabelLimerick.docx",
    "AthenaLimerick.docx",
    "CallaLimerick2.docx",
    "CarlyLimerick.docx",
    "CateLimerick.docx",
    "CelineLimerick.docx",
    "ChoetsawLimerick.docx",
    "DumebiLimerick.docx",
    "EleanorLimerick.docx",
    "ElenaLimerick.docx",
    "EvieLimerick.docx",
    "GraceLimerick.docx",
    "GraceSteelmanLimerick.docx",
    "HalimaLimerick.docx",
    "HollynLimerick.docx",
    "IzzyLimerick.docx",
    "JennLimerick.docx",
    "KiraLimerick.docx",
    "LeahLimerick.docx",
    "LeylaLimerick.docx",
    "AlexisElliotLimerick.docx",
    "BrookeJovanovichLimerick.docx",
    "MaddyGavitt.docx",
    "MarieLimerick.docx",
    "MayaLimerick.docx",
    "MeganeLimerick.docx",
    "MeredithLimerick.docx",
    "MollyLimerick.docx",
    "OliviaLimerick.docx",
    "RyyanLimerick.docx",
    "SaraLimerick.docx",
    "SheaLimerick.docx",
    "SierraLimerick.docx",
    "SydneyLimerick.docx",
    "AvaStone.docx",
    "BronteBrough.docx",
    "BrynneFaltinsky.docx",
    "CharismaChen.docx",
    "DaisyNussbaum.docx",
    "DarianaAlmonte.docx",
    "DespinaGiannakopoulos.docx",
    "EllaDotzler.docx",
    "FieneOerlemans.docx",
    "GraceLang.docx",
    "HannahNguyen.docx",
    "KaiaLi.docx",
    "KatieKrupa.docx",
    "KatieKrupa(1).docx",
    "KendraMorris.docx",
    "LeahYeshitla.docx",
    "LivErnst.docx",
    "LucieBai.docx",
    "LwamMahari.docx",
    "MadisonHussey.docx",
    "MaggieTurner.docx",
    "MayaWalterLimerick.docx",
    "MelodyCao.docx",
    "MenaSolomon.docx",
    "MfonisoAndrew.docx",
    "NatalieMartin.docx",
    "NicoleChavez.docx",
    "OliviaCallander.docx",
    "OmolivieEboreime.docx",
    "PeytonHollis.docx",
    "SaaraChaudry.docx",
    "SarahAdam.docx",
    "SaranGregory-Nghiem.docx",
    "SmritiSomasundaram.docx",
    "TessaShahbo.docx",
    "WillowWoodward.docx",
    "ZoeClark.docx"
]

limerick = ""
# Write to the limerick_data_3 CSV file
with open('limerick_data_3.csv', 'w', newline='') as file:
    # # Create a CSV writer object
    writer = csv.writer(file)

    # Write the data to the CSV file
    writer.writerows([['Limerick', 'Type'],])

    for limerick in files:
        writer.writerows([[docx2txt.process(limerick), 0]])
    
    # CHATGPT 3 TURBO LIMERICKS
    for i in range(20):
        # Randomly select a limerick to use as an example
        random_number = random.randint(0, 88)
        text = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text2 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text3 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text4 = docx2txt.process(files[random_number])

        random_name = names[random.randint(0, 86)]
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Harvard student in the all girls IC social club. You need to write a limerick about your friend who is also in the club."},
                {"role": "user", "content": "You are going to want to write a limerick that is similar to the examples below:"},
                {"role": "user", "content": text},
                {"role": "user", "content": text2},
                {"role": "user", "content": text3},
                {"role": "user", "content": text4},
                {"role": "user", "content": f"Write a two stanza limerick about your friend {random_name} who is about to graduate"},
            ]
        )
        if (completion.choices[0].message.content):
            writer.writerows([[completion.choices[0].message.content, 1]])
    
    for i in range(20):
        random_number = random.randint(0, 88)
        text = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text2 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text3 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text4 = docx2txt.process(files[random_number])

        random_name = names[random.randint(0, 86)]
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Harvard student in the all girls IC social club. You need to write a limerick about your friend who is also in the club."},
                {"role": "user", "content": "You are going to want to write a limerick that is similar to the examples below:"},
                {"role": "user", "content": text},
                {"role": "user", "content": text2},
                {"role": "user", "content": text3},
                {"role": "user", "content": text4},
                {"role": "user", "content": f"Write a two stanza limerick about your friend {random_name} who is about to join the club"},
            ]
        )
        if (completion.choices[0].message.content):
            writer.writerows([[completion.choices[0].message.content, 1]])
    
    for i in range(20):
        random_number = random.randint(0, 88)
        text = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text2 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text3 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text4 = docx2txt.process(files[random_number])

        random_name = names[random.randint(0, 86)]
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Harvard student in the all girls IC social club. You need to write a limerick about your friend who is also in the club."},
                {"role": "user", "content": "You are going to want to write a limerick that is similar to the examples below:"},
                {"role": "user", "content": text},
                {"role": "user", "content": text2},
                {"role": "user", "content": text3},
                {"role": "user", "content": text4},
                {"role": "user", "content": f"Write a two stanza limerick about your friend {random_name} who is on the field hockey team with you"},
            ]
        )
        if (completion.choices[0].message.content):
            writer.writerows([[completion.choices[0].message.content, 1]])
    for i in range(20):
        random_number = random.randint(0, 88)
        text = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text2 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text3 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text4 = docx2txt.process(files[random_number])

        random_name = names[random.randint(0, 86)]
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Harvard student in the all girls IC social club. You need to write a limerick about your friend who is also in the club."},
                {"role": "user", "content": "You are going to want to write a limerick that is similar to the examples below:"},
                {"role": "user", "content": text},
                {"role": "user", "content": text2},
                {"role": "user", "content": text3},
                {"role": "user", "content": text4},
                {"role": "user", "content": f"Write a two stanza limerick about your friend {random_name} that makes jokes about her"},
            ]
        )
        if (completion.choices[0].message.content):
            writer.writerows([[completion.choices[0].message.content, 1]])
    for i in range(20):
        random_number = random.randint(0, 88)
        text = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text2 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text3 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text4 = docx2txt.process(files[random_number])

        random_name = names[random.randint(0, 86)]
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Harvard student in the all girls IC social club. You need to write a limerick about your friend who is also in the club."},
                {"role": "user", "content": "You are going to want to write a limerick that is similar to the examples below:"},
                {"role": "user", "content": text},
                {"role": "user", "content": text2},
                {"role": "user", "content": text3},
                {"role": "user", "content": text4},
                {"role": "user", "content": f"Write a two stanza limerick about your friend {random_name} who you love to go to parties with"},
            ]
        )
        if (completion.choices[0].message.content):
            writer.writerows([[completion.choices[0].message.content, 1]])
    
    # CHATGPT 4 LIMERICKS
    for i in range(20):
        random_number = random.randint(0, 88)
        text = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text2 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text3 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text4 = docx2txt.process(files[random_number])

        random_name = names[random.randint(0, 86)]
        
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a Harvard student in the all girls IC social club. You need to write a limerick about your friend who is also in the club."},
                {"role": "user", "content": "You are going to want to write a limerick that is similar to the examples below:"},
                {"role": "user", "content": text},
                {"role": "user", "content": text2},
                {"role": "user", "content": text3},
                {"role": "user", "content": text4},
                {"role": "user", "content": f"Write a two stanza limerick about your friend {random_name} who is about to graduate"},
            ]
        )
        if (completion.choices[0].message.content):
            writer.writerows([[completion.choices[0].message.content, 2]])
    
    for i in range(20):
        random_number = random.randint(0, 88)
        text = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text2 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text3 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text4 = docx2txt.process(files[random_number])

        random_name = names[random.randint(0, 86)]
        
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a Harvard student in the all girls IC social club. You need to write a limerick about your friend who is also in the club."},
                {"role": "user", "content": "You are going to want to write a limerick that is similar to the examples below:"},
                {"role": "user", "content": text},
                {"role": "user", "content": text2},
                {"role": "user", "content": text3},
                {"role": "user", "content": text4},
                {"role": "user", "content": f"Write a two stanza limerick about your friend {random_name} who is about to join the club"},
            ]
        )
        if (completion.choices[0].message.content):
            writer.writerows([[completion.choices[0].message.content, 2]])
    for i in range(20):
        random_number = random.randint(0, 88)
        text = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text2 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text3 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text4 = docx2txt.process(files[random_number])

        random_name = names[random.randint(0, 86)]
        
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a Harvard student in the all girls IC social club. You need to write a limerick about your friend who is also in the club."},
                {"role": "user", "content": "You are going to want to write a limerick that is similar to the examples below:"},
                {"role": "user", "content": text},
                {"role": "user", "content": text2},
                {"role": "user", "content": text3},
                {"role": "user", "content": text4},
                {"role": "user", "content": f"Write a two stanza limerick about your friend {random_name} who is on the field hockey team with you"},
            ]
        )
        if (completion.choices[0].message.content):
            writer.writerows([[completion.choices[0].message.content, 2]])
    for i in range(20):
        random_number = random.randint(0, 88)
        text = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text2 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text3 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text4 = docx2txt.process(files[random_number])

        random_name = names[random.randint(0, 86)]
        
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a Harvard student in the all girls IC social club. You need to write a limerick about your friend who is also in the club."},
                {"role": "user", "content": "You are going to want to write a limerick that is similar to the examples below:"},
                {"role": "user", "content": text},
                {"role": "user", "content": text2},
                {"role": "user", "content": text3},
                {"role": "user", "content": text4},
                {"role": "user", "content": f"Write a two stanza limerick about your friend {random_name} that makes jokes about her"},
            ]
        )
        if (completion.choices[0].message.content):
            writer.writerows([[completion.choices[0].message.content, 2]])
    for i in range(20):
        random_number = random.randint(0, 88)
        text = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text2 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text3 = docx2txt.process(files[random_number])
        random_number = random.randint(0, 88)
        text4 = docx2txt.process(files[random_number])

        random_name = names[random.randint(0, 86)]
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Harvard student in the all girls IC social club. You need to write a limerick about your friend who is also in the club."},
                {"role": "user", "content": "You are going to want to write a limerick that is similar to the examples below:"},
                {"role": "user", "content": text},
                {"role": "user", "content": text2},
                {"role": "user", "content": text3},
                {"role": "user", "content": text4},
                {"role": "user", "content": f"Write a two stanza limerick about your friend {random_name} who you love to go to parties with"},
            ]
        )
        if (completion.choices[0].message.content):
            writer.writerows([[completion.choices[0].message.content, 2]])

    
    