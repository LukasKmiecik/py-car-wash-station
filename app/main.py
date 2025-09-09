class Car:
    def __init__(
            self,
            comfort_class,
            clean_mark,
            brand
    ):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    def info(self):
        print(f"comfort class to {self.comfort_class}")
        print(f"clean mark to {self.clean_mark}")
        print(f"brand to {self.brand}")


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center,
            clean_power,
            average_rating,
            count_of_ratings
    ):
        self.price = 0
        self.serve_cars_list: list[Car] = []
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]):
        price = 0.0

        for car in cars:
            difference = self.clean_power - car.clean_mark
            if difference > 0:
                price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(price, 2)

    def calculate_washing_price(self, car: Car):
        difference = self.clean_power - car.clean_mark
        if difference > 0:
            a = (car.comfort_class * difference * self.average_rating)
            return round((a / self.distance_from_city_center), 1)
        else:
            return 0.0

    def wash_single_car(self, car: Car):
        difference = self.clean_power - car.clean_mark
        if difference > 0:
            car.clean_mark = self.clean_power
            return True
        return False

    def rate_service(self, rating):
        old_avg = self.average_rating
        old_cnt = self.count_of_ratings

        new_cnt = old_cnt + 1
        new_avg = (old_avg * old_cnt + rating) / new_cnt

        self.count_of_ratings = new_cnt
        self.average_rating = round(new_avg, 1)
        return self.average_rating
