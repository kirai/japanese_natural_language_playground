from pyknp import Jumanpp

jumanapp = Jumanpp()
j = jumanapp.analysis("寿司とケーキを食べたい")

print("\n------------------------")
print("Print list of objects:")
print("------------------------")
print(j.mrph_list())

print("\n------------------------------------------------------")
print("Print morpheme midashi from each object in the list:")
print("------------------------------------------------------")
print([morpheme.midasi for morpheme in j.mrph_list()])


print("\n------------------------------------------------------")
print("Print sushi detailed information:")
print("------------------------------------------------------")
morphemes = [morpheme for morpheme in j.mrph_list()]
sushi = morphemes[0]
print(sushi.imis)
print(sushi.genkei)
print(sushi.bunrui)
print(sushi.yomi)

print("\n------------------------------------------------------")
print("Filter food words:")
print("------------------------------------------------------")
j = jumanapp.analysis("お腹すいたよ。なんか、代官山でレストラン探してくれないのかい〜寿司,焼肉、アップル、りんご、ワイン、オレンジ、滑子")
food_morphemes = [morpheme.midasi for morpheme in j.mrph_list() if "食べ物" in morpheme.imis]
print(food_morphemes)

