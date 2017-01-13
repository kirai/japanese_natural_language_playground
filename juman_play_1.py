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
