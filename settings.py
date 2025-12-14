
headers: dict ={
    "accept": "application/json, text/plain, */*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "o7dip8CvHQ7AbBa-2ZoNczbPsb44R5ygcVbKzhEcg2Jq",
    "dnt": "1",
    "origin": "https://play.pixels.xyz",
    "priority": "u=1, i",
    "referer": "https://play.pixels.xyz/",
    "sec-ch-ua": "'Not/A)Brand';v='8', 'Chromium';v='126', 'Google Chrome';v='126'",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "Android",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
}

# Screw не продается, поэтому включен в рецепт в виде составляющих его частей
# Cooking Tier 1 посчитан в двух вариантах - ингредиенты выращиваются или покупаются на маркете

items_data: dict = {'Plants': {'Popberry': [1, 1.5],  # затраты, энергия
                               'Grainbow': [2, 1.5],
                               'Blue Grumpkin': [3, 2.5],
                               'Orange Grumpkin': [4, 1.5],
                               'Clover': [8, 2.5],
                               'Tato Fruit': [10, 2.5],
                               'Java Bean': [12, 2.5],
                               'Muckchuck': [14, 2.5],
                               },
                    'Mine': {'Mine 1 Tier':[['Clay Matrix', 0.1608], ['Copperite Ore', 0.1765], ['Gravelglass Matrix', 0.0549],
                                            ['Ochrux Matrix', 0.0275]],  # количество ресурса за 1 энергию
                             'Mine 2 Tier':[['Clay Matrix', 0.1555], ['Copperite Ore', 0.1962], ['Gravelglass Matrix', 0.0072],
                                            ['Ochrux Matrix', 0.012], ['Bronzenite Ore', 0.201], ['Marbleite Matrix', 0.3397]],
                             'Wood 1 Tier': [['Whittlewood Log', 0.18], ['Sap', 0.0415]],
                             'Wood 2 Tier':[['Craftbark Log', 0.17], ['Sap', 0.0426]]

                             },
                    'Craft': {  # Woodworking Tier 1
                              'Glue': [['Sap', 2], ['Sawdust', 1], 10],  # Ингредиенты, их количество, энергия
                              'Sawdust': [['Whittlewood Log', 1], 4],
                              'Whittlewood Plank': [['Whittlewood Log', 3], 10],
                                # Woodworking Tier 2
                              'Craftbark Plank': [['Craftbark Log', 3], 20],

                                # Metalworking Tier 1
                              'Basic Magnifying Glass': [['Copperite Ore', 4], ['Gravelglass Matrix', 1], 15],
                              'Copperite Bar': [['Copperite Ore', 3], 10],
                              'Copperite Nail': [['Copperite Ore', 2], 7],

                                # Stoneshaping Tier 1
                              'Clay Brick': [['Clay Powder', 2], 8],
                              'Clay Powder': [['Clay Matrix', 2], 6],
                              'Glass': [['Gravelglass Matrix', 3], 9],
                              'Plaster': [['Clay Powder', 2], ['Sap', 1], 15],
                                # Stoneshaping Tier 2
                              'Marbleite Brick': [['Marbleite Powder', 2], 22],
                              'Marbleite Powder': [['Marbleite Matrix', 2], 15],

                                # Cooking Tier 1
                              'Grumpkin Loaf': [['Blue Grumpkin Puree', 3], ['Grainbow Flour', 2], 2],
                              'Blue Grumpkin Pie': [['Blue Grumpkin Puree', 2], ['Cooking Mix', 1], 20],
                              'Blue Grumpkin Puree': [['Blue Grumpkin', 2], 13],
                              'Grainbow Flour': [['Grainbow', 2], 10],
                              'Grainbow Tart': [['Grainbow Flour', 2], ['Popberry Jam', 1], 15],
                              'Orange Grumpkin Puree': [['Orange Grumpkin', 2], 14],
                              'Popberry Jam': [['Popberry', 2], 8],
                              'Popberry Loaf': [['Popberry Jam', 3], ['Grainbow Flour', 2], 14],
                              'Popberry Pie': [['Popberry Jam', 2], ['Cooking Mix', 1], 15],
                              'Syrup': [['Sap', 2], 8],
                              'Vinegar': [['Grainbow', 2], ['Cooking Mix', 1], 8],
                                # Cooking Tier 2
                              'Clover Fruit Jam': [['Clover', 2], 15],
                              'Clover Fruit Pie': [['Clover Fruit Jam', 2], ['Cooking Mix', 1], 24],
                              'Java Jam': [['Java Bean', 2], 15],
                              'Java Pie': [['Java Jam', 2], ['Cooking Mix', 1], 25],
                              'Muckchuck Jam': [['Muckchuck', 2], 18],
                              'Orange Grumpkin Pie': [['Orange Grumpkin Puree', 2], ['Cooking Mix', 1], 16],
                              'Tato Hash': [['Tato Fruit', 2], 14],
                              'Tato Scramble': [['Tato Hash', 2], ['Popberry', 1], ['Blue Grumpkin', 1],
                                                ['Orange Grumpkin', 1], ['Clover', 1], 26]
                              }
                    }
