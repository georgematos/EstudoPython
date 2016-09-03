# -*- coding: utf-8 -*-
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        print "O destino solicitado não se encontra disponível, tente outro."
        exit()

def rental_car_cost(days):
    rent_day = 40
    rent_cost = days * rent_day
    if days >= 7:
        rent_cost -= 50
    elif days >= 3:
        rent_cost -= 20
    return rent_cost

def trip_cost(city, days, spending_money):
    city_cost = plane_ride_cost(city)
    hotel_cost_days = hotel_cost(days)
    rental_car_cost_days = rental_car_cost(days)

    total = spending_money + city_cost + hotel_cost_days + rental_car_cost_days
    return total

city = raw_input("Digite o destino: "); plane_ride_cost(city)
days = float(raw_input("Digite a quantidade de dias: "))
spending_money = float(raw_input("Digite o custo extra: "))

total = trip_cost(city, days, spending_money)

print "O custo total da sua viagem para %s será de $%.2f" % (city, total)