#TestSourcetree

class House:
    def __init__(self, location, house_type, deal_type, price, complemtion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = complemtion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트" ,"매매", "10억", "2010년")
house2 = House("서초", "오피스텔" ,"전세", "5억", "2007년")
house3 = House("마포", "빌라" ,"월세", "500 / 50", "2013년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

for house in houses:
    house.show_detail()