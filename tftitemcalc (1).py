def itemchecker(champion):
    
    # Items =================
    BB = 'Blue Buff'
    DeathCap = 'Death Cap'
    Gunblade = 'Gunblade'
    Bramble = 'Bramble Vest'
    IE = 'IE' 
    JG = 'Jeweled Gauntlet'
    RB = 'Rageblade'
    Zephyr = 'Zephyr'
    DC = 'Dragons Claw'
    Redemption = 'Redemption'
    HOJ = 'Hand of Justice'
    SOS = 'Spear of Shojin'
    WM = 'Warmogs'
    SS = 'Statikk Shiv'
    RFC = 'Rapid Firecannon'
    BT = 'Bloodthirster'
    Morello = 'Morellonomicon'
    FH = 'Frozen Heart'
    LW = 'Last Whisper' 
    RH = 'Runaans Hurricane'
    QS = 'Quick Silver'
    EON = 'Edge of Night'
    COP = 'Chalice of Power'
    BC = 'Banshees Claw'
    TR = 'Titans Resolve'
    DB = 'Deathblade'
    GS = 'Giant Slayer'
    IS = 'Ionic Spark'
    
    items = {'Ahri': {1: BB, 2: IE, 3: JG},
             'Alistar': {1: Bramble , 2: DC, 3: Redemption},
             'Ashe': {1: SOS, 2: RB, 3: HOJ},
             'Blitzcrank': {1: Bramble , 2: DC, 3: Zephyr},
             'Brand': {1: BB, 2: DeathCap, 3: Gunblade},
             'Braum': {1: Bramble, 2: DC, 3: WM},
             'Caitlyn': {1: SOS, 2: RB, 3: DeathCap},
             'Camille': {1: Bramble, 2: DC, 3: DeathCap},
             'ChoGath': {1: Bramble, 2: DC, 3: Redemption},
             'Corki': {1: SOS, 2: SS, 3: DeathCap},
             'Darius': {1: Bramble, 2: DC, 3: WM},
             'Draven': {1: RFC, 2: IE, 3: BT},
             'Ekko': {1: SOS, 2: Morello, 3: FH},
             'Ezreal': {1: LW, 2: IE, 3: RH},
             'Galio': {1: Bramble, 2: DC, 3: Redemption},
             'Gangplank': {1: LW, 2: IE, 3: RH},
             'Gnar': {1: Bramble, 2: DC, 3: WM},
             'Illaoi': {1: Bramble, 2: DC, 3: WM},
             'Irelia': {1: IE, 2: LW, 3: HOJ},
             'Jarvan': {1: Bramble, 2: DC, 3: WM},
             'Jayce': {1: IE, 2: LW, 3: RH},
             'Jhin': {1: IE, 2: LW, 3: QS},
             'Jinx': {1: RB, 2: EON, 3: RH},
             'Kaisa': {1: Morello, 2: QS, 3: SS},
             'Kassadin': {1: Bramble, 2: DC, 3: WM},
             'KhaZix': {1: IE, 2: HOJ, 3: Gunblade},
             'Leona': {1: Bramble, 2: DC, 3: WM},  
             'Lucian': {1: RB, 2: SS, 3: HOJ},
             'Lulu': {1: SOS, 2: COP, 3: BC},
             'Malzahar': {1: SOS, 2: Morello, 3: Gunblade},
             'Miss Fortune': {1: SOS, 2: DeathCap, 3: JG},
             'Morgana': {1: Morello, 2: Bramble, 3: DC},
             'Nocturne': {1: IE, 2: SOS, 3: QS},
             'Orianna': {1: COP, 2: DeathCap, 3: SOS},
             'Poppy': {1: Bramble, 2: DC, 3: WM},
             'Quimn': {1: IE, 2: LW, 3: QS},
             'Reksai': {1: RH, 2: BT, 3: TR},
             'Renata': {1: COP, 2: DeathCap, 3: SOS},
             'Sejuani': {1: Bramble, 2: DC, 3: WM},
             'Senna': {1: SOS, 2: RB, 3: DB},
             'Seraphine': {1: Morello, 2: SOS, 3: DeathCap},
             'Silco': {1: SOS, 2: SS, 3: COP},
             'Singed': {1: Bramble, 2: DC, 3: WM},
             'Sivir': {1: RB, 2: LW, 3: IE},
             'Swain': {1: QS, 2: GS, 3: DeathCap},
             'Syndra': {1: SOS, 2: JG, 3: IE},
             'Tahm Kench': {1: Bramble, 2: DC, 3: DeathCap},
             'Talon': {1: IE, 2: QS, 3: RFC},
             'Tryndamere': {1: LW, 2: IE, 3: QS},
             'Twitch': {1: IE, 2: LW, 3: RH},
             'Veigar': {1: BB, 2: JG, 3: IE},
             'Vex': {1: Bramble, 2: DC, 3: IS},
             'Vi': {1: Bramble, 2: DC, 3: WM},
             'Viktor': {1: SOS, 2: DeathCap, 3: JG},
             'Warwick': {1: TR, 2: QS, 3: SS},
             'Zac': {1: Bramble, 2: DC, 3: WM},
             'Zeri': {1: RB, 2: TR, 3: LW},
             'Ziggs': {1: SOS, 2: DeathCap, 3: JG},
             'Zillean': {1: SOS, 2: DeathCap, 3: COP},
             'Zyra': {1: SOS, 2: DeathCap, 3: JG}
             
             
                       
             
            
             
             

            
}
    
    
    return (f'{champion}\n1: {items[champion][1]}\n2: {items[champion][2]}\n3: {items[champion][3]}')

