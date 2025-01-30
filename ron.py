from collections import Counter

def can_form_groups(tile_count):
    # 嘗試組成四個雀組
    for tile in sorted(tile_count.keys()):
        while tile_count[tile] > 0:
            # 檢查刻子
            if tile_count[tile] >= 3:
                tile_count[tile] -= 3
            # 檢查順子（只對數字牌適用）
            elif (tile + 1) in tile_count and (tile + 2) in tile_count:
                tile_count[tile] -= 1
                tile_count[tile + 1] -= 1
                tile_count[tile + 2] -= 1
            else:
                return False
    return True

def can_win(tiles):
    # 檢查牌數
    if len(tiles) != 14:
        print("牌數不正確. (!=14)")
        return False

    # 計算每種牌的數量
    tile_count = Counter(tiles)

    # 嘗試找到雀頭
    for tile in list(tile_count):
        if tile_count[tile] >= 2:
            # 去掉雀頭
            tile_count[tile] -= 2
            if can_form_groups(tile_count):
                return True
            # 恢復雀頭
            tile_count[tile] += 2

    return False


# 測試示例
# 手牌萬子 (1-9)、筒子 (11-19)、索子 (21-29)、字牌 (31-37)
hand = [1,1,1,15,15,15,36,36,36,24,25,26,9,9]

# 測試手牌
print("手牌:", hand)
if can_win(hand):
    print("可以和牌")
else:
    print("不可以和牌")