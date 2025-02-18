import json

with open("/Users/zagvozdkinaaa/PP2/week5/json/sample-data.json", "r") as json_file:
    data=json.load(json_file)

interfaces=data["imdata"]

print("Interface Status")
print("="*90)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-"*49, "-"*19, "-"*9, "-"*9)

for item in interfaces:
    attributes=item["l1PhysIf"]["attributes"]
    dn=attributes.get("dn", "")
    speed=attributes.get("speed", "inherit")
    mtu=attributes.get("mtu", "9150")
    print(f"{dn:<70} {speed:<10} {mtu:<10}")
