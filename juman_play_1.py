from pyknp import Jumanpp

jumanapp = Jumanpp()
j = jumanapp.analysis("ケーキを食べる")

print("\n------------------------")
print("Print list of objects:")
print("------------------------")
print(j.mrph_list())

print("\n------------------------------------------------------")
print("Print morpheme midashi from each object in the list:")
print("------------------------------------------------------")
print([morpheme.midasi for morpheme in j.mrph_list()])

