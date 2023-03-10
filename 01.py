player_name = input("请输入玩家名称：")
player_level = 1
player_hp = 100
player_attack = 10
player_defense = 5

print(f"欢迎 {player_name} 加入游戏！")

while True:
    enemy_hp = 50
    enemy_attack = 8
    enemy_defense = 3
    
    print("你遇到了一只恶魔！")
    
    while enemy_hp > 0:
        player_damage = player_attack - enemy_defense
        enemy_damage = enemy_attack - player_defense
        
        if player_damage > 0:
            enemy_hp -= player_damage
            print(f"你攻击了恶魔，恶魔剩余血量为 {enemy_hp} 点！")
        else:
            print("你的攻击被恶魔防御了！")
        
        if enemy_hp <= 0:
            print("你击败了恶魔！")
            player_level += 1
            player_hp += 20
            player_attack += 5
            player_defense += 2
            print(f"你升级了！你的等级提升到了 {player_level} 级！")
            print(f"你的生命值提升到了 {player_hp} 点！")
            print(f"你的攻击力提升到了 {player_attack} 点！")
            print(f"你的防御力提升到了 {player_defense} 点！")
            break
        
        if enemy_damage > 0:
            player_hp -= enemy_damage
            print(f"恶魔攻击了你，你的剩余生命值为 {player_hp} 点！")
        else:
            print("恶魔攻击被你防御了！")
        
        if player_hp <= 0:
            print("你被恶魔击败了，游戏结束！")
            exit()