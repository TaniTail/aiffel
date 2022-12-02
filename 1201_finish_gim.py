import random
class BokGim:
	
	ingredient_list = ["와사비", "와사비", "와사비"\
		, "햄", "초콜릿", "참치", "치즈", "고구마케이크" "오이"\
        , "단무지", "김치", "크래미", "시금치", "당근", "쌈장", "우엉"\
        , "불닭볶음면", "연어", "계란", "아보카도", "돈까스", "삼겹살", "새우튀김"\
        , "오뎅", "불고기", "깻잎", "부침개", "묵은지", "청양고추", "마요네즈", "부추"\
        , "스팸", "소시지", "톳", "멸치볶음", "진미채", "시래기", "머스타드", "박고지"]
	
	type_list = ["김 김밥", "누드김밥", "유부초밥", "주먹밥"]

	def __init__(self, j, appearance, ingredient):
		self.n = j
		self.appearance = appearance
		self.ingredient = ingredient
		self.hp = 10
		self.status = '새 김밥'
	
	def bite(self): 
		self.hp = - 1

		if self.hp - 1 <= 0:
			self.status = '다먹고 이름만 남은 김밥'
		elif 1 <= self.hp <= 5:
			self.status = '반쯤 먹음'
		else:
			self.status = '새 김밥은 아님'
	
	def split(self):
			print(self.ingredient) 

	def change(self, k):
		if k in self.ingredient:
			k = random.sample(self.ingredient_list - self.ingredient)
		else:
			print("김밥에 있는 재료를 입력해주세요.")
			
def main():
    
    participant = []
    gimbap_table = []

    def join():
        name = (input("참가할 사람 이름을 입력하세요(모집마감을 원하시면 '끝'을 입력해주세요): "))
        if name == '끝':
            start()
        else:
            participant.append(name)
            print(participant)
            join()

    def make():
        j = random.randint(1, 5) # 1부터 5 사이의 난수 생성.재료개수
        appearance = random.choice(BokGim.type_list)
        ingredient = random.sample(BokGim.ingredient_list, j) #리스트
        gim = BokGim(j, appearance, ingredient)
        gimbap_table.append(gim)
        print("지금 김밥의 수 : " + str(len(gimbap_table)))
    
    def give_gim():
        list_in =random.sample(gimbap_table, len(participant)) #리스트
        dic = {}
        for i in range(len(participant)):
            dic[participant[i]] = list_in[i]

        print("김밥이 분배되었습니다. 와사비 당첨자는...")

        for i in range(len(participant)):
        
            if "와사비" in list_in[i].ingredient:
                print(participant[i]+ "입니다!")
            else:
                pass

    def start():

        x = input("1.join 2.make 3.give_gim")
        if x == "1":
            join()
        elif x == "2":
            n = int(input("몇 개 쌀까요? : "))
            for i in range(n):
                make()            
            print("다 쌌습니다. 지금 김밥은 " + str(len(gimbap_table)) + " 개 입니다.")
            start()
        elif x == "3":
            give_gim()

    start()


if __name__ == '__main__':
    main()
