import json

terraria = [
    [
        ["0002","0001","0001","0002"],
        ["0001","0003","0000","0001"],
        ["0001","0000","0003","0001"],
        ["0002","0001","0001","0002"]
    ],
    [
        ["ffff","0005","0005","ffff"],
        ["ffff","0006","0006","ffff"],
        ["ffff","ffff","ffff","ffff"],
        ["ffff","ffff","ffff","ffff"]
    ],
    [
        ["000a","0001","0001","000b"],
        ["000a","ffff","ffff","000b"],
        ["000a","ffff","ffff","000b"],
        ["000a","ffff","ffff","000b"]
    ],
    [
        ["000e","ffff","ffff","ffff"],
        ["ffff","ffff","ffff","ffff"],
        ["ffff","ffff","ffff","ffff"],
        ["ffff","ffff","ffff","ffff"]
    ],
]

with open('terraria.json', 'w', encoding='utf-8') as f:
    json.dump(terraria, f, ensure_ascii=False, indent=4)
