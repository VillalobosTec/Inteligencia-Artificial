import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

temperatura = ctrl.Antecedent(np.arange(0, 41, 1), 'temperatura')
ropa = ctrl.Consequent(np.arange(0, 11, 1), 'ropa')


temperatura['frio'] = fuzz.trimf(temperatura.universe, [0, 0, 20])
temperatura['agusto'] = fuzz.trimf(temperatura.universe, [15, 25, 25])
temperatura['caliente'] = fuzz.trimf(temperatura.universe, [20, 40, 40])

ropa['sueter'] = fuzz.trimf(ropa.universe, [0, 0, 5])
ropa['agusto'] = fuzz.trimf(ropa.universe, [4, 5, 6])
ropa['fresca'] = fuzz.trimf(ropa.universe, [5, 10, 10])

regla1 = ctrl.Rule(temperatura['frio'], ropa['sueter'])
regla2 = ctrl.Rule(temperatura['agusto'], ropa['agusto'])
regla3 = ctrl.Rule(temperatura['caliente'], ropa['fresca'])

sistema_control_ropa = ctrl.ControlSystem([regla1, regla2, regla3])
sistema = ctrl.ControlSystemSimulation(sistema_control_ropa)

def recomendar_ropa(temp_actual):
    sistema.input['temperatura'] = temp_actual
    sistema.compute()
    recomendacion = sistema.output['ropa']
    if recomendacion <= 3:
        print(f"Con {temp_actual}°C, es recomendable usar sueter.")
    elif recomendacion <= 6:
        print(f"Con {temp_actual}°C, es recomendable usar ropa agusto.")
    else:
        print(f"Con {temp_actual}°C, es recomendable usar ropa fresca.")

temp_usuario = float(input("dime la temperatura actual (en °C) : "))

recomendar_ropa(temp_usuario)
