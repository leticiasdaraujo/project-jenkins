import argparse

# ------------------------------------------------------------------------------------------------------ #
# # ------------------------------------- EXAMPLE TO APPLY JENKINS ------------------------------------# #
# ------------------------------------------------------------------------------------------------------ #

''' This application is an example to be used in Jenkins. 
It performs temperature conversion using command-line arguments. '''

def conversion_fah_to_celsius(fah):
    """Converts Fahrenheit to Celsius and returns a float."""
    return (fah - 32.0) / 1.8

def conversion_celsius_to_fah(celsius):
    """Converts Celsius to Fahrenheit and returns a float."""
    return (celsius * 1.8) + 32.0

def process_temperature(target_scale, temp_value):
    if target_scale == "C":
        result = conversion_fah_to_celsius(temp_value)
        print(f"The temperature in Celsius is: {result:.2f} C")
        
    elif target_scale == "F":
        result = conversion_celsius_to_fah(temp_value)
        print(f"The temperature in Fahrenheit is: {result:.2f} F")

# -------------------------------------------------------- MAIN ------------------------------------------------------ #
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script de conversao de temperatura para CI/CD (Jenkins).")
    
    parser.add_argument(
        "-t", "--target", 
        choices=['C', 'F'], 
        required=True, 
        help="Escala de destino: digite 'C' para Celsius ou 'F' para Fahrenheit."
    )
    
    parser.add_argument(
        "-v", "--value", 
        type=float, 
        required=True, 
        help="Valor numérico da temperatura a ser convertida."
    )
    
    args = parser.parse_args()

    process_temperature(args.target, args.value)