def init():
    global status_config
    status_config = {}
    global item_config
    item_config = {}
    global endian_check_offset
    endian_check_offset = 0xA8
    global character_offset
    character_offset = 0xA324
    global costume_offset
    costume_offset = 0xA318
    global weapon_offset
    weapon_offset = 0xA210
    global accessory_offset
    accessory_offset = 0xA2F0
    global chapter_index_offset
    chapter_index_offset = 0xA634, 0xA688
    global chapter_offset
    chapter_offset = 0xA638
    global checkpoint_offset
    checkpoint_offset = 0xA660
    global character_to_id
    character_to_id = {
        "Bayonetta": 0x00,
        "Jeanne":    0x01,
        "Balder":    0x02,
        "Rodin":     0x03,
        "Rosa":      0x04
    }
    global id_to_character
    id_to_character = {value: key for key, value in character_to_id.items()}
    global costume_to_id
    costume_to_id = {
        "Bayonetta": {
            "Default":              0x00,
            "Bayonetta 1":          0x01,
            "Dress (White)":        0x05,
            "Dress (Pink)":         0x06,
            "Young Bayonetta":      0x0D,
            "Nun Outfit":           0x13,
            "Witch Apprentice":     0x03,
            "Metal Witch":          0x02,
            "Umbran Gekka (Blue)":  0x16,
            "Umbran Gekka (White)": 0x15,
            "Umbran Gekka (Red)":   0x14,
            "Schoolgirl (Blue)":    0x17,
            "Schoolgirl (Yellow)":  0x18,
            "Schoolgirl (Red)":     0x19,
            "Police Cadet":         0x1B,
            "Police Officer":       0x1A,
            "Peach Dress":          0x1D,
            "Daisy Dress":          0x1E,
            "Link Suit":            0x1F,
            "Samus Armor":          0x20,
            "Fox Costume":          0x1C,
            "Peach Dress (Bayo 1)": 0x0F,
            "Daisy Dress (Bayo 1)": 0x10,
            "Link Suit (Bayo 1)":   0x11,
            "Samus Armor (Bayo 1)": 0x12
        },
        "Jeanne": {
            "Default":              0x07,
            "Jeanne (Bayo 1)":      0x21,
            "Elegant Outfit":       0x32,
            "Uniformed":            0x33,
            "Uniformed (Bayo 1)":   0x31,
            "Cutie J":              0x38,
            "Young Jeanne":         0x0E,
            "Nun Outfit":           0x27,
            "Witch Apprentice":     0x04,
            "Metal Witch":          0x22,
            "Umbran Gekka (Blue)":  0x2A,
            "Umbran Gekka (White)": 0x29,
            "Umbran Gekka (Red)":   0x28,
            "Schoolgirl (Blue)":    0x2B,
            "Schoolgirl (Yellow)":  0x2C,
            "Schoolgirl (Red)":     0x2D,
            "Police Cadet":         0x2F,
            "Police Officer":       0x2E,
            "Peach Dress":          0x34,
            "Daisy Dress":          0x35,
            "Link Suit":            0x36,
            "Samus Armor":          0x37,
            "Fox Costume":          0x30,
            "Peach Dress (Bayo 1)": 0x23,
            "Daisy Dress (Bayo 1)": 0x24,
            "Link Suit (Bayo 1)":   0x25,
            "Samus Armor (Bayo 1)": 0x26
        },
        "Balder": {
            "Unmasked":             0x08,
            "Masked":               0x09
        },
        "Rodin": {
            "Japan Style":          0x0A,
            "New York Style":       0x0B
        },
        "Rosa": {
            "Robes of Banishing":   0x0C
        }
    }
    global id_to_costume
    id_to_costume = {key: {sub_value: sub_key for sub_key, sub_value in value.items()} for key, value in costume_to_id.items()}
    global weapon_to_id
    weapon_to_id = {
        "Bayonetta": {
            "Love Is Blue":     0x00,
            "Rakshasa":         0x01,
            "Takemikazuchi":    0x02,
            "Alruna":           0x03,
            "Kafka":            0x04,
            "Chernobog":        0x05,
            "Chain Chomp":      0x06,
            "Undine":           0x07,
            "Salamandra":       0x08,
            "Tartarus":         0x09,
            "Sai Fung Kilgore": 0x0A,
            "Arwing":           0x0B,
            "Handguns":         0x0C,
            "Scarborough Fair": 0x0D,
            "Shuraba":          0x0E,
            "Rodin Rings":      0x0F,
            "Umbran Sisters":   0x10
        },
        "Jeanne": {
            "All 4 One":        0x00,
            "Rasetsu":          0x01,
            "Yagyu":            0x02,
            "Alruna":           0x03,
            "Samsa":            0x04,
            "Inferno Slayer":   0x05,
            "Chain Chomp":      0x06,
            "Rusalka":          0x07,
            "Agni":             0x08,
            "Tartarus":         0x09,
            "Sai Fung Kilgore": 0x0A,
            "Arwing":           0x0B,
            "Handguns":         0x0C,
            "Scarborough Fair": 0x0D,
            "Angel Slayer":     0x0E,
            "Rodin Rings":      0x0F,
            "Umbran Sisters":   0x10
        },
        "Balder": {
            "Balder's Glaive":  0x11
        },
        "Rodin": {
            "Rodin's Fists":    0x12
        },
        "Rosa": {
            "Unforgiven":       0x00,
            "Rakshasa":         0x01,
            "Takemikazuchi":    0x02,
            "Alruna":           0x03,
            "Kafka":            0x04,
            "Chernobog":        0x05,
            "Chain Chomp":      0x06,
            "Undine":           0x07,
            "Salamandra":       0x08,
            "Tartarus":         0x09,
            "Sai Fung Kilgore": 0x0A,
            "Arwing":           0x0B,
            "Handguns":         0x0C,
            "Scarborough Fair": 0x0D,
            "Shuraba":          0x0E,
            "Rodin Rings":      0x0F,
            "Umbran Sisters":   0x10
        }
    }
    global id_to_weapon
    id_to_weapon = {key: {sub_value: sub_key for sub_key, sub_value in value.items()} for key, value in weapon_to_id.items()}
    global accessory_to_id
    accessory_to_id = {
        "None":                  0x00,
        "Infernal Communicator": 0x02,
        "Pulley's Butterfly":    0x03,
        "Selene's Light":        0x04,
        "Star of Dinéta":        0x05,
        "Evil Harvest Rosary":   0x06,
        "Gaze of Despair":       0x07,
        "Moon of Mahaa-Kalaa":   0x08,
        "Eternal Testimony":     0x09,
        "Bracelet of Time":      0x0A,
        "Climax Brace":          0x0B,
        "Earrings of Ruin":      0x0C,
        "Climax Brace 2":        0x0D,
        "Mallet of Rewards":     0x0E,
        "Immortal Marionette":   0x0F
    }
    global id_to_accessory
    id_to_accessory = {value: key for key, value in accessory_to_id.items()}
    global chapter_to_id
    chapter_to_id = {
        "The End":                          (0x0110, 0x1CB2AE5F, "P110_START_EVENT"),
        "World of Chaos":                   (0x0120, 0x47E76A0A, "INTRO_EV"),
        "Noatun, The City of Genesis":      (0x0212, 0x63CBA5BA, "P212_EVENT"),
        "A Remembrance of Time":            (0x0230, 0x3671B3EE, "P230_EVENT"),
        "Paradiso - The Gates of Paradise": (0x0240, 0x096CAA4B, "P240_START_EVENT"),
        "The Two Meet":                     (0x024B, 0x08FE4269, "P24B_EVENT"),
        "The Cathedral of Cascades":        (0x0262, 0x1A8F77F6, "P262_SNAKE_EVENT"),
        "The Bridge to the Heavens":        (0x0280, 0x2F200B88, "P280_START_NEW"),
        "The Ark":                          (0x0340, 0x242DBEDF, "P340_EV3000"),
        "An Ancient Civilization":          (0x0430, 0x61BC954C, "P430_START"),
        "The Gates of Hell":                (0x0450, 0x27D39CCB, "P450_START"),
        "The Depths":                       (0x0510, 0x4DE5FBE7, "P510_START_EV"),
        "Inferno And Its Ruler":            (0x0560, 0x229E2174, "P560_COLISEUM"),
        "The Lumen Sage":                   (0x0580, 0x0DA559BE, "P580_FOREST1"),
        "Vigrid, City of Déjà Vu":          (0x0620, 0x03E0BD54, "P620_START"),
        "The Witch Hunts":                  (0x0640, 0x11D24E08, "WAR_GROUND"),
        "Truth":                            (0x0670, 0x6FD7EC18, "P670_EVENT"),
        "Sovereign Power":                  (0x0710, 0x3EC3F1DC, "P710_EVENT"),
        "Witch Trial I":                    (0x0A21, 0x0742B609, "PA21_SLAYER_01"),
        "Witch Trial II":                   (0x0A22, 0x1EA0D008, "PA22_SLAYER_01"),
        "Witch Trial III":                  (0x0A23, 0x5F2E0FC8, "PA23_SLAYER_01"),
        "Witch Trial IV":                   (0x0A24, 0x76151A4B, "PA24_SLAYER_01"),
        "Witch Trial V":                    (0x0A25, 0x379BC58B, "PA25_SLAYER_01")
    }
    global id_to_chapter
    id_to_chapter = {value[1]: key for key, value in chapter_to_id.items()}
    global checkpoint_to_id
    checkpoint_to_id = {
        "World of Chaos": {
            "Start":        (0x0120, 0x7EB66703, "BATTLE_A"),
            "Love Is Blue": (0x0120, 0x7C84D7C7, "BATTLE_A_HAS_BLUE"),
            "Glamor Intro": (0x0120, 0x67BF36B9, "BATTLE_B"),
            "Train Chase":  (0x0130, 0x363F4EFF, "CATCH_UP_EV"),
            "Belief":       (0x0130, 0x4C3D28C5, "VRS_10_MUCHI_B"),
            "Gomorrah":     (0x0140, 0x6CEEE7F5, "P140_BTL_OUT_BUILDING"),
            "Gomorrah 2":   (0x0140, 0x54D69232, "P140_BTL_TOP_BUILDING")
        },
        "Noatun, The City of Genesis": {
            "Start":        (0x0212, 0x1C5E2559, "P212_EVENT_END"),
            "Underwater":   (0x0216, 0x08626A84, "P216_IN"),
            "Shop Intro":   (0x0216, 0x3A180289, "P216_SHOP"),
            "Plaza":        (0x0220, 0x2905871B, "P220_PLAZA"),
            "Valiance":     (0x0228, 0x48F60F18, "P228_SAVE"),
            "Cathedral":    (0x0229, 0x070CAA7A, "P229_01"),
            "Loki Team Up": (0x0229, 0x03AADCBD, "P229_SAVE"),
            "To Glamor":    (0x022A, 0x483B4CA6, "P22A_SAVE3"),
            "Glamor Intro": (0x022D, 0x0E5AE2C9, "P22D_ATTACK"),
            "Glamor":       (0x022D, 0x04E41C92, "P22D_BTL")
        },
        "A Remembrance of Time": {
            "Start":         (0x0230, 0x12A6ECC6, "P230_START"),
            "Cathedral":     (0x0238, 0x174F0282, "P238_WAGIRI"),
            "Cathedral Top": (0x0238, 0x17292FD7, "P238_WAGIRI_SAVE"),
            "Belief":        (0x0238, 0x78C77DBD, "P238_WAGIRI_WALK2")
        },
        "Paradiso - The Gates of Paradise": {
            "Start":         (0x0240, 0x4051BFE9, "P240_TORNADO"),
            "Glamor Tunnel": (0x0240, 0x5632EF16, "P240_TORNADO_02"),
            "Glamor":        (0x0240, 0x74CE2098, "P240_AIR_BATTLE"),
            "Glamor 2":      (0x0240, 0x1568F545, "P240_AIR_BATTLE_02")
        },
        "The Two Meet": {
            "Start":       (0x024B, 0x7C438F6D, "P24B_EVENT_END"),
            "Door Break":  (0x024B, 0x2481F902, "P24B_BTL02"),
            "Urbane":      (0x024D, 0x4FF9287B, "P24D_START"),
            "Post Urbane": (0x024D, 0x14F6452E, "P24D_EVENT_END"),
            "To Balder":   (0x024D, 0x3056FCAE, "P24D_BTL03"),
            "Balder":      (0x0250, 0x53FFA0ED, "P250_BTL_02_START"),
            "Balder 2":    (0x0250, 0x7588AB59, "P250_BTL_03_START")
        },
        "The Cathedral of Cascades": {
            "Start":         (0x0262, 0x6044E76B, "P262_LAND"),
            "Graveyard":     (0x0266, 0x5DA6C22F, "P266_BTL"),
            "Loki Stairway": (0x0266, 0x3D97CB0B, "P266_TALK_END"),
            "Loki Escape":   (0x0275, 0x18464AD6, "P275_ROLL_START"),
            "Fire and Ice":  (0x0277, 0x365D2A31, "P277_TEKKYU_BATTLE")
        },
        "The Bridge to the Heavens": {
            "Start":   (0x0280, 0x4FCCF090, "P280_START"),
            "Valor 2": (0x0280, 0x2B86B1C5, "P280_WATER")
        },
        "The Ark": {
            "Start":           (0x0340, 0x0F18F19C, "P340_START"),
            "Insidius 2":      (0x0340, 0x21A0A1FD, "P340_MANTA_EVENT"),
            "Inside Insidius": (0x036B, 0x79770E7F, "P36B_START"),
            "To Balder":       (0x036B, 0x49E2ADB1, "P36B_BTL_END"),
            "Balder":          (0x0370, 0x4998AF85, "P370_BALDER_01"),
            "Balder 2":        (0x0370, 0x1D03A9A8, "P370_FLUX")
        },
        "An Ancient Civilization": {
            "Start":         (0x0430, 0x1224D57F, "P430_START_EV_END"),
            "Golem":         (0x0430, 0x0317DF97, "P430_GATE_NO_KEY"),
            "Church":        (0x0430, 0x125E8B8F, "P430_CHURCH"),
            "Halfway":       (0x0440, 0x46EAFC7E, "P440_FIRST_BTL"),
            "Courtyard":     (0x0440, 0x0005885C, "P440_GUARDIAN_BTL"),
            "Underwater":    (0x0440, 0x17AB90E5, "P440_WATER_BTL"),
            "Pride":         (0x0440, 0x2B3B6C92, "P440_GRAVE_BTL")
        },
        "The Gates of Hell": {
            "Start":         (0x0450, 0x04F4F17B, "P450_START_POLE_END"),
            "Cathedral Top": (0x0450, 0x3C680C54, "P450_PASS_BTL_01"),
            "Cathedral End": (0x0450, 0x600C1A5A, "P450_PASS_END"),
            "Prophet":       (0x0460, 0x7D1DFC05, "P460_BOSS")
        },
        "The Depths": {
            "Start":           (0x0510, 0x14CAF57F, "P510_START_EV_END"),
            "Phantasmaraneae": (0x0530, 0x4311E24D, "P530_MAJU"),
            "Resentment":      (0x0530, 0x1DD8C98E, "P530_BTL_IN"),
            "To Sloth":        (0x0530, 0x44760898, "P530_ACROSS_IVY"),
            "Sloth":           (0x0530, 0x113737D3, "P530_FLOATING_ISLAND"),
            "To Insidius":     (0x0530, 0x58142D7C, "P530_TO_COLISEUM_2")
        },
        "Inferno And Its Ruler": {
            "Start":     (0x0560, 0x758F117A, "P560_LADY_BOSS1"),
            "Alraune 2": (0x0560, 0x6C8640C0, "P560_LADY_BOSS2")
        },
        "The Lumen Sage": {
            "Start":           (0x0580, 0x57F1BD50, "P580_HELP"),
            "Father Balder":   (0x05A0, 0x06CA314E, "P5A0_BTL"),
            "Father Balder 2": (0x05A0, 0x6062B76B, "P5A0_BTL_B")
        },
        "Vigrid, City of Déjà Vu": {
            "Start":           (0x0620, 0x68703ECC, "PLAZA"),
            "Fortitudo":       (0x0620, 0x6999A5AC, "BATTLE_BOSS"),
            "Ship Escape":     (0x0620, 0x63AE3320, "BATTLE_SHIP_EV_END"),
            "Grace & Glory":   (0x0630, 0x10010E9E, "R604_DEL"),
            "Hand Fight":      (0x0630, 0x3929863A, "G_WALL_END"),
            "Lava Run":        (0x0630, 0x0034DE99, "LAVA_START"),
            "Across Beloved":  (0x0630, 0x58133EF6, "BELOVED_BRIDGE_END"),
            "Umbran Quarters": (0x0630, 0x1F24D5BB, "TALK")
        },
        "The Witch Hunts": {
            "Start":    (0x0640, 0x58FA0BF2, "WAR_GROUND_ON"),
            "Hill":     (0x0640, 0x6555B756, "WAR_GROUND_HILL"),
            "Bridge":   (0x0640, 0x603F679F, "WAR_GROUND_BRIDGE"),
            "Sapienta": (0x0640, 0x4E3728EB, "WAR_GROUND_BOSS"),
            "Worship":  (0x0650, 0x1E10EC82, "WAR_SKY"),
            "Iusticia": (0x0650, 0x3EFE663A, "BOSS")
        },
        "Truth": {
            "Start":       (0x0670, 0x6DF5C039, "P670_BTL"),
            "Temperantia": (0x0670, 0x194FF0CC, "P670_BOSS"),
            "Tower Fall":  (0x0680, 0x2AF9F552, "FALL_BTL"),
            "Loptr":       (0x0680, 0x3EFE663A, "BOSS"),
            "Loptr 2":     (0x0680, 0x3555260E, "BOSS_2"),
            "Ruins":       (0x06A0, 0x7140B320, "P6A0_ROOT"),
            "Ruins End":   (0x06A0, 0x6A1B470B, "P6A0_BTL02_END")
        },
        "Sovereign Power": {
            "Start":      (0x0710, 0x5A3F064E, "P710_PART_01"),
            "To Loptr":   (0x0720, 0x740D7807, "P720_FREE"),
            "Loptr":      (0x0720, 0x59666A36, "P720_BOSS_1ST"),
            "Aesir":      (0x0720, 0x56643574, "P720_BOSS_2ND_GROUND"),
            "Aesir 2":    (0x0720, 0x141D3DB5, "P720_BOSS_2ND_SKY"),
            "Aesir Down": (0x0720, 0x5E4E9F7D, "P720_BOSS_3RD")
        }
    }
    global no_checkpoint_id
    no_checkpoint_id = (0x0F02, 0x1F79558F, "start")
    global id_to_checkpoint
    id_to_checkpoint = {key: {sub_value[1]: sub_key for sub_key, sub_value in value.items()} for key, value in checkpoint_to_id.items()}
    global item_to_offset
    item_to_offset = {
        "Halos":                      0xA3B0,
        "Green Herb Lollipop":        0xA3EC,
        "Mega Green Herb Lollipop":   0xA3F4,
        "Purple Magic Lollipop":      0xA3FC,
        "Mega Purple Magic Lollipop": 0xA404,
        "Bloody Rose Lollipop":       0xA40C,
        "Mega Bloody Rose Lollipop":  0xA414,
        "Yello Moon Lollipop":        0xA41C,
        "Mega Yello Moon Lollipop":   0xA424,
        "Midas's Testament":          0xA434,
        "Red Hot Shot":               0xA444,
        "Witch Heart":                0xA2D8,
        "Moon Pearl":                 0xA36C
    }
    global item_to_range
    item_to_range = {
        "Halos":                      (0, 99999999),
        "Green Herb Lollipop":        (0, 99),
        "Mega Green Herb Lollipop":   (0, 99),
        "Purple Magic Lollipop":      (0, 99),
        "Mega Purple Magic Lollipop": (0, 99),
        "Bloody Rose Lollipop":       (0, 99),
        "Mega Bloody Rose Lollipop":  (0, 99),
        "Yello Moon Lollipop":        (0, 99),
        "Mega Yello Moon Lollipop":   (0, 99),
        "Midas's Testament":          (0, 99),
        "Red Hot Shot":               (0, 99),
        "Witch Heart":                (1, 25),
        "Moon Pearl":                 (8, 32)
    }

def read_from_save_file(save_path):
    with open(save_path, "rb") as save_file:
        #Endian check
        save_file.seek(endian_check_offset)
        value = int.from_bytes(save_file.read(4), "big")
        endian = "little" if value % 0x1000000 == 0 else "big"
        #Character
        save_file.seek(character_offset)
        character_id = int.from_bytes(save_file.read(4), endian)
        character = ""
        if character_id in id_to_character:
            character = id_to_character[character_id]
        status_config["Character"] = character
        #Costume
        save_file.seek(costume_offset)
        costume_id = int.from_bytes(save_file.read(4), endian)
        costume = ""
        if character in id_to_costume:
            if costume_id in id_to_costume[character]:
                costume = id_to_costume[character][costume_id]
        status_config["Costume"] = costume
        #Weapons
        save_file.seek(weapon_offset)
        for index in range(4):
            weapon_id = int.from_bytes(save_file.read(4), endian)
            weapon = ""
            if character in id_to_weapon:
                if weapon_id in id_to_weapon[character]:
                    weapon = id_to_weapon[character][weapon_id]
            status_config[f"Weapon {index + 1}"] = weapon
        #Accessories
        save_file.seek(accessory_offset)
        for index in range(3):
            accessory_id = int.from_bytes(save_file.read(4), endian)
            accessory = ""
            if accessory_id in id_to_accessory:
                accessory = id_to_accessory[accessory_id]
            status_config[f"Accessory {index + 1}"] = accessory
        #Chapter
        save_file.seek(chapter_index_offset[0])
        chapter_index = int.from_bytes(save_file.read(4), endian)
        chapter_index = -(chapter_index & 0x80000000) | (chapter_index & 0x7FFFFFFF)
        if chapter_index < 0:
            save_file.seek(chapter_offset + 4)
            chapter_id = int.from_bytes(save_file.read(4), endian)
            chapter = id_to_chapter[chapter_id] if chapter_id in id_to_chapter else ""
        else:
            chapter = list(chapter_to_id)[chapter_index]
        status_config["Chapter"] = chapter
        #Checkpoint
        save_file.seek(checkpoint_offset + 4)
        checkpoint_id = int.from_bytes(save_file.read(4), endian)
        checkpoint = ""
        if chapter in id_to_checkpoint:
            if checkpoint_id in id_to_checkpoint[chapter]:
                checkpoint = id_to_checkpoint[chapter][checkpoint_id]
        status_config["Checkpoint"] = checkpoint
        #Items
        for item in item_to_offset:
            save_file.seek(item_to_offset[item])
            item_config[item] = int.from_bytes(save_file.read(4), endian)

def write_to_save_file(save_path):
    with open(save_path, "r+b") as save_file:
        #Endian check
        save_file.seek(endian_check_offset)
        value = int.from_bytes(save_file.read(4), "big")
        endian = "little" if value % 0x1000000 == 0 else "big"
        #Character
        save_file.seek(character_offset)
        character = status_config["Character"]
        character_id = character_to_id[character]
        save_file.write(character_id.to_bytes(4, endian))
        #Costume
        save_file.seek(costume_offset)
        costume = status_config["Costume"]
        costume_id = costume_to_id[character][costume]
        save_file.write(costume_id.to_bytes(4, endian))
        #Weapons
        save_file.seek(weapon_offset)
        for index in range(4):
            weapon = status_config[f"Weapon {index + 1}"]
            weapon_id = weapon_to_id[character][weapon]
            save_file.write(weapon_id.to_bytes(4, endian))
        #Accessories
        save_file.seek(accessory_offset)
        for index in range(3):
            accessory = status_config[f"Accessory {index + 1}"]
            accessory_id = accessory_to_id[accessory]
            save_file.write(accessory_id.to_bytes(4, endian))
        #Chapter
        chapter = status_config["Chapter"]
        checkpoint = status_config["Checkpoint"]
        no_checkpoint = checkpoint == "None"
        chapter_index = list(chapter_to_id).index(chapter)
        chapter_id = chapter_to_id[chapter]
        save_file.seek(chapter_index_offset[0])
        save_file.write((0xFFFFFFFF if no_checkpoint else chapter_index).to_bytes(4, endian))
        save_file.seek(chapter_index_offset[1])
        save_file.write(chapter_index.to_bytes(4, endian))
        save_file.seek(chapter_offset)
        save_file.write((0).to_bytes(0x28, endian))
        save_file.seek(chapter_offset)
        save_file.write(chapter_id[0].to_bytes(4, endian))
        save_file.write(chapter_id[1].to_bytes(4, endian))
        save_file.write(str.encode(chapter_id[2]))
        #Checkpoint
        checkpoint_id = no_checkpoint_id if no_checkpoint else checkpoint_to_id[chapter][checkpoint]
        save_file.seek(checkpoint_offset)
        save_file.write((0).to_bytes(0x28, endian))
        save_file.seek(checkpoint_offset)
        save_file.write(checkpoint_id[0].to_bytes(4, endian))
        save_file.write(checkpoint_id[1].to_bytes(4, endian))
        save_file.write(str.encode(checkpoint_id[2]))
        #Items
        for item in item_to_offset:
            save_file.seek(item_to_offset[item])
            save_file.write(item_config[item].to_bytes(4, endian))
        save_file.seek(0xA2D0)
        health = item_config["Witch Heart"]*400
        save_file.write(health.to_bytes(4, endian))
        save_file.write(health.to_bytes(4, endian))