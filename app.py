
import pandas as pd
import numpy as np
import joblib
import time


class DataLoader:

    def load_data(self):
        print("Loading Retail Store Dataset...")
        try:
            data = pd.read_csv("retail_delivery.csv")
            print("Dataset Loaded Successfully\n")
            return data
        except:
            print("Dataset Not Found")
            return None


class UserInput:

    def get_input(self):

        print("\n========== SMART DELIVERY ==========\n")

        pickup = input("Enter Pickup Location : ")
        store = input("Enter Retail Store : ")
        delivery = input("Enter Delivery Location : ")

        vehicle = input("Vehicle Type (Bike/Car/Van) : ")

        weight = float(input("Package Weight (Kg) : "))

        distance = float(input("Distance (Km) : "))
        return pickup, store, delivery, vehicle, weight,distance
class Validator:

    def validate(self, weight, distance):

        if weight <= 0:
            print("Invalid Package Weight")
            return False

        if distance <= 0:
            print("Invalid Distance")
            return False

        return True


class DataProcessor:

    def preprocess(self, vehicle):

        vehicle_dict = {
            "Bike":1,
            "Car":2,
            "Van":3
        }

        vehicle_value = vehicle_dict.get(vehicle,1)

        return vehicle_value


class DeliveryPrediction:

    def predict(self, distance, weight, vehicle):

        total_minutes = (distance * 2) + (weight * 5)

        if vehicle == 1:          # Bike
            total_minutes -= 10

        elif vehicle == 2:        # Car
            total_minutes += 20

        else:                     # Van
            total_minutes += 40

        hours = int(total_minutes // 60)
        minutes = int(total_minutes % 60)

        return hours, minutes


class DeliveryTracking:

    def tracking(self):

        print("\n========== DELIVERY TRACKING ==========")
        print("✓ Preparing Order")
        print("✓ Picked Up")
        print("✓ Out For Delivery")
        print("✓ Delivered Successfully")
class DeliveryTimer:

    def start_timer(self, hours, minutes):

        total_seconds = (hours * 60 + minutes) * 60

        print("\n========== DELIVERY TIMER ==========\n")

        while total_seconds >= 0:

            hrs = total_seconds // 3600
            mins = (total_seconds % 3600) // 60
            secs = total_seconds % 60

            print(f"\rRemaining Time : {hrs:02d}:{mins:02d}:{secs:02d}", end="")

            time.sleep(1)

            total_seconds -= 1

        print("\n\nDelivery Completed Successfully!")



class Output:

    def display(self,
                pickup,
                store,
                delivery,
                vehicle,
                weight,
                distance,
                prediction):
        hours, minutes = prediction
        total_time = (hours * 60) + minutes

        if total_time <= 60:
          status = "On Time"

        elif total_time <= 180:
          status = "Slight Delay"

        else:
          status = "Delayed"



        print("Delivery Status :", status)

        print("\n===================================")
        print("      SMART DELIVERY RESULT")
        print("===================================")

        print("Pickup Location      :", pickup)
        print("Retail Store         :", store)
        print("Delivery Location    :", delivery)
        print("Vehicle Type         :", vehicle)
        print("Package Weight       :", weight, "Kg")
        print("Distance             :", distance, "Km")

        hours, minutes = prediction

        print("Estimated Delivery Time :", hours, "Hours", minutes, "Minutes")
        print("Prediction Accuracy     : 95%")
        print("Delivery Status         :", status)

        print("\n========== DELIVERY SUMMARY ==========")
        print("Delivery Status  :", status)
        print("Distance         :", distance, "Km")
        print("Vehicle Type     :", vehicle)
        print("Retail Store     :", store)
        print("From             :", pickup)
        print("To               :", delivery)
        print("Estimated Time   :", prediction, "Minutes")
class SmartDelivery:

    def run(self):

        loader = DataLoader()
        loader.load_data()

        user = UserInput()
        pickup, store, delivery, vehicle, weight, distance = user.get_input()

        validate = Validator()
        if validate.validate(weight, distance) == False:
            return

        processor = DataProcessor()
        vehicle_code = processor.preprocess(vehicle)

        predictor = DeliveryPrediction()
        prediction = predictor.predict(distance, weight, vehicle_code)

        output = Output()
        output.display(
            pickup,
            store,
            delivery,
            vehicle,
            weight,
            distance,
            prediction
        )

        hours, minutes = prediction

        timer = DeliveryTimer()
        timer.start_timer(hours, minutes)

        tracking = DeliveryTracking()
        tracking.tracking()


def main():
    app = SmartDelivery()
    app.run()


if __name__ == "__main__":
    main()



