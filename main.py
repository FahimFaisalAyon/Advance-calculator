import socket

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
ARDUINO_IP = '192.168.0.103'  # Use localhost for the mock server
ARDUINO_PORT = 8080 # Port that matches the mock server
class Widgets(GridLayout):
    # Declare variables for each row
    a = StringProperty("")
    b = StringProperty("")
    c = StringProperty("")
    d = StringProperty("")
    e = StringProperty("")
    g = StringProperty("")
    usage = StringProperty("")
    WS = StringProperty("")
    Angle = StringProperty("")
    Len = StringProperty("")
    Dia = StringProperty("")
    twist = StringProperty("")
    h = StringProperty("")
    f = StringProperty("")# Add h as a property

    def click(self, field_id, variable_name):
        # Set the corresponding variable to the input text
        setattr(self, variable_name, self.ids[field_id].text)
        value = getattr(self, variable_name)
        print(f"Stored in '{variable_name}': {value}")

        # Send the variable and its value over Wi-Fi
        message = f"{variable_name}:{value}"
        self.send_data(message)

    def send_data(self, message):
        """Send data to the Arduino via Wi-Fi."""
        try:
            # Create a socket and connect to the mock Arduino
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ARDUINO_IP, ARDUINO_PORT))
                s.sendall(message.encode())
                print(f"Sent: {message}")
        except Exception as e:
            print(f"Failed to send data: {e}")

    def get_input_value(self, input_id):
        """Retrieve and convert the input value to float."""
        input_value = self.ids[f'input_field_{input_id}'].text
        if input_value.strip():  # Check if not empty
            try:
                return float(input_value)
            except ValueError:
                return None  # Return None if conversion fails
        return None  # Return None if input is empty

    def calculate_h(self):
        try:
            a = self.get_input_value('a')
            b = self.get_input_value('b')
            c = self.get_input_value('c')
            d = self.get_input_value('d')
            e = self.get_input_value('e')

            # Filter out None and zero values
            values = [x for x in (a, b, c, d, e) if x is not None and x != 0]

            if not values:
                self.ids.result_label_h.text = "Invalid input"
                return

            # Calculate h using the filtered values
            h = 1 / sum(1 / value for value in values)
            self.h = f"{h:.2f}"  # Format to 2 decimal places
            self.ids.result_label_h.text = f"h: {self.h}"  # Display h value

            # Send h value to Arduino
            self.send_data(f"h:{self.h}")

        except ZeroDivisionError:
            self.ids.result_label_h.text = "Undefined (division by zero)"
        except Exception as e:
            self.ids.result_label_h.text = f"Error: {str(e)}"

    def calculate_i(self):
        try:
            g = self.get_input_value('g')
            if g is not None:
                if g != 0:
                    i_value = 1 / g
                    # Update the display label with the calculated value of i
                    self.ids.result_label_i.text = f"{i_value:.2f}"  # Format to 2 decimal places
                else:
                    self.ids.result_label_i.text = "Undefined (g=0)"
            else:
                self.ids.result_label_i.text = "Invalid input"
        except Exception as e:
            self.ids.result_label_i.text = f"Error: {str(e)}"

class TheLabApp(App):
    def build(self):
        return Widgets()

if __name__ == "__main__":
    TheLabApp().run()